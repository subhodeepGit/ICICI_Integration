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
        getSessionToken(doc.name,doc.amount)
        getTransactionDetails(doc,doc.name)  
       
       
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
        transactionDetailsData = tokenclass.inquiryTest(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                                            java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                                            java.lang.String("%s"% merchantTxnId),
                                            java.lang.String("%s"% fpTransactionId)) 
        
        transactionDetailsData = json.loads(str(transactionDetailsData))       
        frappe.db.set_value("OnlinePayment",str(transactionDetailsData["saleTxnDetail"]["merchantTxnId"]),"fptxnid",str(transactionDetailsData["fpTransactionId"]))
        # frappe.db.sql(""" update `tabOnlinePayment` set fptxnid='%s' where name='%s' """%(str(transactionDetailsData["fpTransactionId"]),str(transactionDetailsData["saleTxnDetail"]["merchantTxnId"])))
        frappe.db.set_value("OnlinePayment",str(transactionDetailsData["saleTxnDetail"]["merchantTxnId"]),"transaction_status",str(transactionDetailsData["saleTxnDetail"]["transactionStatus"]))           
        frappe.db.set_value("OnlinePayment",str(transactionDetailsData["saleTxnDetail"]["merchantTxnId"]),"transactionstatusdescription",str(transactionDetailsData["saleTxnDetail"]["transactionStatusDescription"]))           
      
        frappe.db.commit() 
        doc.fptxnid =  str(transactionDetailsData["fpTransactionId"]) 
        doc.transaction_status =  str(transactionDetailsData["saleTxnDetail"]["transactionStatus"])
        doc.transactionstatusdescription =  str(transactionDetailsData["saleTxnDetail"]["transactionStatusDescription"])
    except Exception as e: 
        print(repr(e))
    return str(transactionDetailsData) 
        
@frappe.whitelist()        
def getSessionToken(name,amount):  

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
    
     

    # resultURL="http://10.0.160.184:8000/paymentreturn?id=" + name    #2VM approach:working
    
    # resultURL="https://demo.soulunileaders.com/paymentreturn?id=" + name

    resultURL="https://paymentkp.eduleadonline.com/paymentreturn?id=" + name

    

    
    try:

        tokenclass = JClass('TokenClass') 
        tokenId = tokenclass.getToken(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                            java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                            java.lang.String("%s"% amountValue),java.lang.String("%s"% currencyCode),java.lang.String("%s"% merchantTxnId),
                            java.lang.String("%s"% transactionType),java.lang.String("%s"% resultURL))
        
        if str(tokenId) != None:
            newURL= "https://test.fdconnect.com/Pay/?sessionToken=" + str(tokenId) + "&configId="+configId;             
           
        else :
            frappe.throw("Session has expired. Please create new transaction")  
                    
    except Exception as err:
        print("Exception: {err}")

    return {"TokenId":str(tokenId),"configId":configId}


@frappe.whitelist()
def getDecryptedData(doc,encData=None,fdcTxnId=None):  
   
    getDoc=frappe.get_doc("ICICI Settings")
    merchantId = getDoc.merchantid
    apiURL="https://test.fdconnect.com/FirstPayL2Services/decryptMerchantResponse" 
    try: 
        if (encData!=None and fdcTxnId!=None):

            tokenclass = JClass('TokenClass')
            decData = tokenclass.getDecryptResponse(java.lang.String("%s"% merchantId), java.lang.String("%s"% encData),
                                                java.lang.String("%s"%fdcTxnId),java.lang.String("%s"% apiURL)) 
            
            decData = json.loads(str(decData))
            
            frappe.db.set_value("OnlinePayment",decData["merchantTxnId"],"fptxnid",decData["fpTransactionId"])
            frappe.db.set_value("OnlinePayment",decData["merchantTxnId"],"transaction_status",decData["transactionStatus"])          
            frappe.db.set_value("OnlinePayment",decData["merchantTxnId"],"transactionstatusdescription",decData["transactionStatusDescription"])           
        
            frappe.db.commit() 
            doc.fptxnid =  decData["fpTransactionId"]
            doc.transaction_status = decData["transactionStatus"]
            doc.transactionstatusdescription = decData["transactionStatusDescription"]
                
        
        
    except Exception as e: 
        print(repr(e))
    return str(decData)    


    