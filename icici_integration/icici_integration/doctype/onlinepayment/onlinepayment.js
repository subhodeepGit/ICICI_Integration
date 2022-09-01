// Copyright (c) 2022, SOUL ltd and contributors
// For license information, please see license.txt
frappe.ui.form.on("OnlinePayment", "refresh", function(frm){
	frm.add_custom_button("Online Payment", function(){
 
	 frappe.call({		  
		 method: "icici_integration.icici_integration.doctype.onlinepayment.onlinepayment.getSessionToken",		        
		 args: {
			 
			 name:frm.doc.name,
			 amount:frm.doc.amount,
 
	   },
		   
		 callback: function(r) {
			 var sessionId=r.message["TokenId"]
			 var configId=r.message["configId"]				
			 window.open("https://test.fdconnect.com/Pay/?sessionToken=" + sessionId + "&configId="+ configId,"_self")
			  
		   }
	   });
 
	 });

	 frappe.ui.form.on('OnlinePayment', {
		refresh(frm) { 
			if(frm.doc.docstatus==1){
			frm.remove_custom_button('Online Payment');
			}
		}
	})
 }); 
 
 
 frappe.ui.form.on("OnlinePayment", "onload", function(frm) {
 	
	
	 var  queryString = window.location.search;
	 var urlParams = new URLSearchParams(queryString);
	 var fpTxnId = urlParams.get('fpTxnId');
	 var encData = urlParams.get('encData')
	

	 frappe.call({		  
		method: "icici_integration.icici_integration.doctype.onlinepayment.onlinepayment.getDecryptedData",		        
		args: {
			doc:frm.doc,
			encData:encData,
			fdcTxnId:fpTxnId
			

	  },
		  
		callback: function(r) {
		   
		  }
	  });

	
 
 	});  
		 
	   
 
	 