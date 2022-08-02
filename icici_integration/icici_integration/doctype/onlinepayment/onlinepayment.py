# Copyright (c) 2022, SOUL ltd and contributors
# For license information, please see license.txt

from jpype import startJVM, shutdownJVM, java, addClassPath, JClass, JInt
# if jpype.isJVMStarted() is False:
#  startJVM(convertStrings=False)
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/TokenClass.jar")
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/CommerceConnect.jar")
startJVM(convertStrings=False)
import jpype.imports
import webbrowser
from urllib.request import urlopen
import frappe
from frappe.model.document import Document
from frappe.utils import get_url
import requests 
from urllib.request import urlopen
import json



class OnlinePayment(Document):
    def validate(self):
        getDoc=frappe.get_doc("ICICI Settings")
        merchantId = getDoc.merchantid
        key=getDoc.key      
        iv=getDoc.iv
        apiURL="https://test.fdconnect.com//FirstPayL2Services/getToken"     
        amountValue=self.amount          
        currencyCode="INR" 
        merchantTxnId=self.name  
        transactionType="sale"          
        Udf="123456"  # user variable
        # resultURL="http://localhost:8000/app/onlinepayment/"+self.name
        resultURL="http://localhost:8000/api/method/icici_integration.icici_integration.doctype.api.receive_post_data"
        # resultURL="http://demokp.eduleadonline.com/api/method/icici_integration.icici_integration.doctype.api.receive_post_data"
        
        try:

            tokenclass = JClass('TokenClass') 
            res = tokenclass.getTokenNew(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                                java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                                java.lang.String("%s"% amountValue),java.lang.String("%s"% currencyCode),java.lang.String("%s"% merchantTxnId),
                                java.lang.String("%s"% transactionType),java.lang.String("%s"% resultURL), java.lang.String("%s"% Udf))
                                         
                                
            if str(res) !="None":

                newURL= "https://test.fdconnect.com//Pay/?sessionToken=" + str(res) + "&configId=PageId2022021713158"; 
                # webbrowser.open(newURL) 
                webbrowser.open(newURL, new=0)
            else :
                frappe.throw("Session has expired. Please create new transaction")  
            
            
        except Exception as err:
           

            frappe.throw (err)



           