# Copyright (c) 2022, SOUL ltd and contributors
# For license information, please see license.txt

from jpype import startJVM, shutdownJVM, java, addClassPath, JClass, JInt
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/TokenClass.jar")
addClassPath("/opt/bench/frappe-bench/apps/icici_integration/icici_integration/icici_integration/doctype/onlinepayment/CommerceConnect.jar")
# startJVM(convertStrings=False)
startJVM(convertStrings=True)  #is used for the proper conversion of java.lang.String to Python string literals
import webbrowser
from urllib.request import urlopen
import frappe
from frappe.model.document import Document
from urllib.request import urlopen
import json
import datetime


class OnlinePayment(Document):
	def on_submit(doc): 
		
		getTransactionDetails(doc,doc.name)  
		frappe.msgprint("Your Transaction is completed. Your Transaction Id is " + doc.transactionid)
	   
	   
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
		   
		frappe.db.set_value("OnlinePayment",transactionDetailsData["saleTxnDetail"]["merchantTxnId"],"transactionid",transactionDetailsData["fpTransactionId"])
		frappe.db.set_value("OnlinePayment",transactionDetailsData["saleTxnDetail"]["merchantTxnId"],"transaction_status",transactionDetailsData["saleTxnDetail"]["transactionStatus"])        
		frappe.db.set_value("OnlinePayment",transactionDetailsData["saleTxnDetail"]["merchantTxnId"],"transaction_status_description",transactionDetailsData["saleTxnDetail"]["transactionStatusDescription"])         
		frappe.db.commit() 

		doc.transactionid=transactionDetailsData["fpTransactionId"] 
		doc.transaction_status=transactionDetailsData["saleTxnDetail"]["transactionStatus"]
		doc.transaction_status_description=transactionDetailsData["saleTxnDetail"]["transactionStatusDescription"]
			   
	except Exception as err:
		print(repr(err))

	return str(transactionDetailsData) 
  

		
@frappe.whitelist()        
def getSessionToken(name,amount):  
	print("\n\n\n\n")
	print(getDoc)

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
	

	# resultURL="http://10.0.160.184:8000/paymentreturn?id=" + name   #local     
	
	resultURL="https://paymentkp.eduleadonline.com/paymentreturn?id=" + name  #server

	try:
		tokenclass = JClass('TokenClass') 
		tokenId = tokenclass.getToken(java.lang.String("%s"% merchantId), java.lang.String("%s"% key),
							java.lang.String("%s"%iv),java.lang.String("%s"% apiURL),
							java.lang.String("%s"% amountValue),java.lang.String("%s"% currencyCode),java.lang.String("%s"% merchantTxnId),
							java.lang.String("%s"% transactionType),java.lang.String("%s"% resultURL))
		print("\n\n\n\n")
		if str(tokenId) != None:
			newURL= "https://test.fdconnect.com/Pay/?sessionToken=" + str(tokenId) + "&configId="+configId;             
		   
		else :
			frappe.throw("Session has expired. Please create new transaction")  
					
	except Exception as err:
		print(repr(err))

	return {"TokenId":str(tokenId),"configId":configId}


@frappe.whitelist()
def getDecryptedData(doc,encData=None,fdcTxnId=None):  
	getDoc=frappe.get_doc("ICICI Settings")
	merchantId = getDoc.merchantid
	apiURL="https://test.fdconnect.com/FirstPayL2Services/decryptMerchantResponse" 
	try:
		
		if encData!=None and fdcTxnId!=None:
			tokenclass = JClass('TokenClass')
			decData = tokenclass.getDecryptResponse(java.lang.String("%s"% merchantId), java.lang.String("%s"% encData),
													java.lang.String("%s"%fdcTxnId),java.lang.String("%s"% apiURL))             
			decData = json.loads(str(decData))
			
			# if decData["merchantTxnId"]!= None:
			# id= frappe.get_doc("OnlinePayment",decData["merchantTxnId"])

			# print("id-----?",id)
			if (decData["transactionStatus"]=="FAILED"):
				ct = datetime.datetime.now()                
			else:
				ct=decData["transactionDateTime"]
	except Exception as e: 
		print(repr(e))
	# if decData!=None:
	#     return {"transactionid":decData["fpTransactionId"],"transaction_status":decData["transactionStatus"],
	#             "transaction_status_description":decData["transactionStatusDescription"],"datetime":ct}
	if decData==None:
		pass
	# elif decData["errorCode"] != None:
	# 	pass			
	else:
		return {"transactionid":decData["fpTransactionId"],"transaction_status":decData["transactionStatus"],
						"transaction_status_description":decData["transactionStatusDescription"],"datetime":ct}

# @frappe.whitelist()
# def submission(doc): 
# 	print("\n\n\n\n\n")
# 	print ("doc--->",doc)
# 	if doc!=None:
# 		submitDoc=frappe.get_doc("OnlinePayment",doc)
# 		print ("submitDoc--->",submitDoc)
# 		submitDoc.save()
# 		submitDoc.submit()

