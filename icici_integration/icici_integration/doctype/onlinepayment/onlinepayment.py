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



class OnlinePayment(Document):
    def on_submit(doc):  
        
        getDoc=frappe.get_doc("ICICI Settings")
        merchantId = getDoc.merchantid
        key=getDoc.key
        iv=getDoc.iv
        merchantTxnId=doc.name
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
            
            frappe.db.set_value("OnlinePayment",str(resultData["saleTxnDetail"]["merchantTxnId"]),"fptxnid",str(resultData["fpTransactionId"]))
            # frappe.db.sql(""" update `tabOnlinePayment` set fptxnid='%s' where name='%s' """%(str(resultData["fpTransactionId"]),str(resultData["saleTxnDetail"]["merchantTxnId"])))
                                                        
           
        except Exception as e: 
            print(repr(e))
        return str(resultData)
       

    # @frappe.whitelist()
    # def InqueryTransaction(name):

    #     getDoc=frappe.get_doc("ICICI Settings")
    #     merchantId = getDoc.merchantid
    #     key=getDoc.key      
    #     iv=getDoc.iv
    #     merchantTxnId=name
    #     fpTransactionId=""
    #     apiURL="https://test.fdconnect.com/FirstPayL2Services/getTxnInquiryDetail"  

    #     print("\n\n\n\n\n") 
    #     print(getDoc)
    #     print(merchantId)
    #     print(key)
    #     print(iv)
    #     print(merchantTxnId)
    #     print(apiURL)

    #     try:

    #         tokenclass = JClass('TokenClass') 
    #         resultData = tokenclass.inquiryTest(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
    #                                             java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
    #                                             java.lang.String("%s"% merchantTxnId),
    #                                             java.lang.String("%s"% fpTransactionId))

    #         print("\n\n\n\n\n") 
    #         print(resultData)
    #         # print("Started reading nested JSON array")
    #         # status = resultData["saleTxnDetail"]["transactionStatus"]
    #         # print(status)


    #     except Exception as err:
    #         print("Exception: {err}") 
    #     return str(resultData)
    #     # return status

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
    nURL=frappe.utils.get_url()

    
   
    # resultURL="http://10.0.160.184:8000/paymentreturn?id=" + name    #2VM approach:working
    
    resultURL="http://10.0.163.42:8000/paymentreturn?id=" + name    #1VM ipaddress:working*****
    # resultURL="http://demokp.eduleadonline.com/paymentreturn?id=" + name    


    # resultURL="http://10.0.163.147:8000/redirectpage?id=" + name   
   

    # resultURL="http://localhost:8000/api/method/icici_integration.icici_integration.doctype.api.receive_post_data"
    # resultURL="http://demokp.eduleadonline.com/api/method/icici_integration.icici_integration.doctype.api.receive_post_data"

    try:

        tokenclass = JClass('TokenClass') 
        res = tokenclass.getToken(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                            java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                            java.lang.String("%s"% amountValue),java.lang.String("%s"% currencyCode),java.lang.String("%s"% merchantTxnId),
                            java.lang.String("%s"% transactionType),java.lang.String("%s"% resultURL))
                            
        if str(res) !="None":

            newURL= "https://test.fdconnect.com/Pay/?sessionToken=" + str(res) + "&configId="+configId; 
        
            # webbrowser.open(newURL)
        else :
            frappe.throw("Session has expired. Please create new transaction")  
        
        
    except Exception as err:
        print("Exception: {err}")

    return str(res)
    
    
    
