import frappe
# For license information, please see license.txt

from jpype import startJVM, shutdownJVM, java, addClassPath, JClass, JInt
# if jpype.isJVMStarted() is False:
#  startJVM(convertStrings=False)
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/TokenClass.jar")
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/CommerceConnect.jar")
# startJVM(convertStrings=False)
import jpype.imports
import webbrowser
from urllib.request import urlopen
from frappe.model.document import Document
from frappe.utils import get_url
import requests 
from urllib.request import urlopen
import json
from selenium import webdriver

@frappe.whitelist(allow_guest=True)
def receive_post_data(**kwargs):
    # data=frappe.request
    print("\n\n\n\n\n")
    # print(data)
    kwargs=frappe._dict(kwargs)
    print("kwargs",kwargs)
    print(kwargs['merchantId'])
    print(kwargs['encData'])
    print(kwargs['fpTxnId'])
    print("i am ok")
    apiURL="https://test.fdconnect.com/FirstPayL2Services/decryptMerchantResponse"
    name=kwargs['MerchantTxnId']
    

    tokenclass = JClass('TokenClass') 
    res = tokenclass.getDecryptResponse(java.lang.String(kwargs['merchantId']), java.lang.String(kwargs['encData']),
                                java.lang.String(kwargs['fpTxnId']),java.lang.String("%s"% apiURL))

    import webbrowser
    from frappe.utils import get_url
    url=get_url("{0}{1}".format("/app/onlinepayment/",name))
    print(url)
    webbrowser.open(url)  # Go to example.com                                
                               
    
    return
