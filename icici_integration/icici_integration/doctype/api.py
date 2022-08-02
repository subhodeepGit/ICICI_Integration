import frappe
from jpype import startJVM, shutdownJVM, java, addClassPath, JClass, JInt
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/TokenClass.jar")
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/CommerceConnect.jar")
import jpype.imports
import webbrowser
from urllib.request import urlopen
from frappe.model.document import Document
from frappe.utils import get_url

@frappe.whitelist(allow_guest=True)
def receive_post_data(**kwargs):
    # data=frappe.request
    kwargs=frappe._dict(kwargs)
    print("kwargs",kwargs)
    # print(kwargs['merchantId'])
    apiURL="https://test.fdconnect.com/FirstPayL2Services/decryptMerchantResponse"
    name=kwargs['MerchantTxnId']
    

    tokenclass = JClass('TokenClass') 
    res = tokenclass.getDecryptResponse(java.lang.String(kwargs['merchantId']), java.lang.String(kwargs['encData']),
                                java.lang.String(kwargs['fpTxnId']),java.lang.String("%s"% apiURL))
   
   
    url=get_url("{0}{1}".format("/app/onlinepayment/",name))
    webbrowser.open(url)  # Go to example.com                                
                            
    
    # return
