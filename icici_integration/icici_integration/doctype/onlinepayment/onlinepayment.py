# Copyright (c) 2022, SOUL ltd and contributors
# For license information, please see license.txt

from jpype import startJVM, shutdownJVM, java, addClassPath, JClass, JInt
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/TokenClass.jar")
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/CommerceConnect.jar")
startJVM(convertStrings=False)
import webbrowser
from urllib.request import urlopen
import frappe
from frappe.model.document import Document
from urllib.request import urlopen
import json
from cryptography.fernet import Fernet
from urllib.parse import unquote

class OnlinePayment(Document):
    def on_submit(doc): 
        getSessionToken(doc,doc.name,doc.amount)
        # getDecryptedData(url)
        getTransactionDetails(doc,doc.name)  
        # dataDecrypt(doc)
       
def getTransactionDetails(doc,name):   
    getDoc=frappe.get_doc("ICICI Settings")
    merchantId = getDoc.merchantid
    key=getDoc.key
    iv=getDoc.iv
    merchantTxnId=name
    fpTransactionId=""
    apiURL="https://test.fdconnect.com/FirstPayL2Services/getTxnInquiryDetail" 
    try: 
        tokenclass = JClass('TokenClass')
        resultData = tokenclass.inquiryTest(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                                            java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                                            java.lang.String("%s"% merchantTxnId),
                                            java.lang.String("%s"% fpTransactionId)) 
        print("\n\n\n\n\n")
        print(resultData) 
        print(type(resultData))
        resultData = json.loads(str(resultData))
        print(type(resultData))
        print("Started reading nested JSON array")
        print(resultData["fpTransactionId"])
        print(resultData["saleTxnDetail"]["merchantTxnId"])
        print(resultData["saleTxnDetail"]["transactionStatus"])
        print(frappe.local.login_manager.user)
        frappe.db.set_value("OnlinePayment",str(resultData["saleTxnDetail"]["merchantTxnId"]),"fptxnid",str(resultData["fpTransactionId"]))
        # frappe.db.sql(""" update `tabOnlinePayment` set fptxnid='%s' where name='%s' """%(str(resultData["fpTransactionId"]),str(resultData["saleTxnDetail"]["merchantTxnId"])))
        frappe.db.set_value("OnlinePayment",str(resultData["saleTxnDetail"]["merchantTxnId"]),"transaction_status",str(resultData["saleTxnDetail"]["transactionStatus"]))           
        frappe.db.set_value("OnlinePayment",str(resultData["saleTxnDetail"]["merchantTxnId"]),"transactionstatusdescription",str(resultData["saleTxnDetail"]["transactionStatusDescription"]))           
      
        frappe.db.commit() 
        doc.fptxnid =  str(resultData["fpTransactionId"]) 
        doc.transaction_status =  str(resultData["saleTxnDetail"]["transactionStatus"])
        doc.transactionstatusdescription =  str(resultData["saleTxnDetail"]["transactionStatusDescription"])
    except Exception as e: 
        print(repr(e))
    return str(resultData) 
        
@frappe.whitelist()        
def getSessionToken(doc,name,amount):  

    getDoc=frappe.get_doc("ICICI Settings")
    merchantId = getDoc.merchantid
    key=getDoc.key      
    iv=getDoc.iv
    configId= getDoc.configid
    apiURL="https://test.fdconnect.com/FirstPayL2Services/getToken"     
    amountValue=amount          
    currencyCode="INR" 
    merchantTxnId=name  
    transactionType="sale"  
    # nURL=frappe.utils.get_url()        

    # resultURL="http://10.0.160.184:8000/paymentreturn?id=" + name    #2VM approach:working
    
    # resultURL="http://10.0.163.42:8000/paymentreturn?id=" + name    #1VM ipaddress:working*****
    
    resultURL="https://demo.soulunileaders.com/paymentreturn?id=" + name

    try:

        tokenclass = JClass('TokenClass') 
        res = tokenclass.getToken(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                            java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                            java.lang.String("%s"% amountValue),java.lang.String("%s"% currencyCode),java.lang.String("%s"% merchantTxnId),
                            java.lang.String("%s"% transactionType),java.lang.String("%s"% resultURL))
        print("\n\n\n\n\n")
        print(res)                             
        print(frappe.local.login_manager.user)                 
        if str(res) != None:

            newURL= "https://test.fdconnect.com/Pay/?sessionToken=" + str(res) + "&configId="+configId;             
            # webbrowser.open(newURL)
        else :
            frappe.throw("Session has expired. Please create new transaction")  
                    
    except Exception as err:
        print("Exception: {err}")

    return str(res)

# def dataDecrypt(doc)   :

     
#     url="https://test.fdconnect.com/FirstPayL2Services/redirectToMerchantUrl?merchantId=470000012765500&encData=h2sUPU86ytjDciY1EEAPceGB9NqBD0eBJXzoBQVfQlTNmuquLkkt6DpiqmVPVyJszr4i98qR87jmWd3rMFvpTKZQ9r52zaWb%2BkUUN%2FURzKKJhkjqmuGaGVWyUvwwraoXq8I5k7xlvKORJ9AwOFnyP%2F%2Fy3c0ozcavVkOhpVJ0ECGnpq%2FPSzW7DJvDRC8NiRRo18k4qiyuw6iyg%2FFUjRXNd%2Fil2zKO8Li%2FBtDV7zYabRfilY0XsSKapu67BReOJPe6%2BjB%2BEKpE54OzUGqv%2B3apFxSkLLfti%2BrpX4sKbajOBfP73qUEbe8kzlZJnFcDXFhNJQmUSHZ1w8nt42fI2f8illKcPpfmAYb3w8EzhDd0fYJXPxUUTypiLp5lCGCTg2tppYpLbuXdF5lz8HNnLVH3ctNFAow2m%2B8bK7EFkTWyZm0nmFJ4fNBwIQfGhZHMOXBjyyClviMYvYeiGa2%2F%2BRbdztz5CvhxVvvFsQQmfEcj4vXrg%2F2OCiy6wfZhtInB0b4WYmYfoYGqB0aolZdgWUTIL6AxsyTGha9CeK8r0AWXRz5VtIxmzL5HKJb%2BqZpRWVH1Id%2FshS4KW1AZpaUN50vqfoFvQrESqcNI2nt1gFzsse9opeT%2BB2Jn%2Bmw1Tqbydqg%2FLukiUuNTIayeYa%2F3GYphMhFUNEyZeaPR5h6wgOqyadreSo3VffHkkrarV5D7%2BOR3j55YbtZDBwrFunU3Sv2%2BRs9U5KHvvHedUaxUK37Rdj5tUM4%2BgVx7ZOvHnl2wOwW0J6ixHExssalp5zJoRHF5pIWOjOSKraM50QiqCDBPgTtPXR3RzcOZYrFOmhdy92wfC%2F1M3kjGcm2LolAe6tnjRYmtPSNfBAwtWfeEsiXEZWe4ugp%2FVN4sQrPkrhpO0Y1L6hZzwhXF%2FjqnBC%2BAx5%2FkWfKhqSP7VTjRNS0Sl2gcMrm0MkZnpYBu2oQEbmLyz4V%2B&fpTxnId=2022080154780219&resultURL=https://merchantresposneurl"
#     url = unquote(url)
#     print(url)
        
@frappe.whitelist()  
# def getDecryptedData(doc,name):
def getDecryptedData(doc,encData,fdcTxnId):  
    print("\n\n\n")
    print("ok")
    print(doc)
    getDoc=frappe.get_doc("ICICI Settings")
    merchantId = getDoc.merchantid
    apiURL="https://test.fdconnect.com/FirstPayL2Services/decryptMerchantResponse" 
    try: 
        tokenclass = JClass('TokenClass')
        resData = tokenclass.getDecryptResponse(java.lang.String("%s"% merchantId), java.lang.String("%s"% encData),
                                            java.lang.String("%s"%fdcTxnId),java.lang.String("%s"% apiURL)) 
        print("\n\n\n\n\n")
        print(resData) 
        print(type(resData))
        resData = json.loads(str(resData))
        print(type(resData))
        print("Started reading nested JSON array")
        
    except Exception as e: 
        print(repr(e))
    return str(resData)    


    