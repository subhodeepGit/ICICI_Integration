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

class OnlinePayment(Document):
    def validate(self):
        print("\n\n\n")
        print("Going to calc.py file")
        print("\n\n\n")
        
       
        getDoc=frappe.get_doc("ICICI Settings")
        merchantId = getDoc.merchantid
        print("\n\n\n")
        print(merchantId)        
        key=getDoc.key      
        iv=getDoc.iv
        apiURL="https://test.fdconnect.com//FirstPayL2Services/getToken"     
        amountValue=self.amount
        print("\n\n\n")
        print(amountValue)      
        currencyCode="INR" 
        merchantTxnId=self.name  
        transactionType="sale"          
        resultURL="http://erp.soul.com:8000/app/onlinepayment/"+self.name
        
        print(resultURL)
        try:

            tokenclass = JClass('TokenClass') 
            res = tokenclass.getToken(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
                                java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
                                java.lang.String("%s"% amountValue),java.lang.String("%s"% currencyCode),java.lang.String("%s"% merchantTxnId),
                                java.lang.String("%s"% transactionType),java.lang.String("%s"% resultURL))
            print(res)
            newURL= "https://test.fdconnect.com//Pay/?sessionToken=" + str(res) + "&configId=PageId2022021713158"; 
            # windows.location.redirect()            
            webbrowser.open_new_tab(newURL) 
            # status=tokenclass.getDecryptResponse()
            
        except Exception as err:
            print("Exception: {err}")

           