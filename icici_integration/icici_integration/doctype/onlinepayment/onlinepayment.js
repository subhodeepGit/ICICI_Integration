// Copyright (c) 2022, SOUL ltd and contributors
// For license information, please see license.txt
frappe.ui.form.on("OnlinePayment",{
	pay: function(frm) {
 
	 frappe.call({		  
		 method: "icici_integration.icici_integration.doctype.onlinepayment.onlinepayment.getSessionToken",		        
		 args: {
			 doc:frm.doc,
			 name:frm.doc.name,
			 amount:frm.doc.amount,
 
	   },
		   
		 callback: function(r) {
			//  alert(JSON.stringify(r))			 
			 var res=r.message;
			//  alert(res);
			 // redirect to Web form 
			//  window.open("http://10.0.160.184:8000/payment-details?new=1&transaction_id="+res,"_self")
			 // window.open("http://localhost:8000/payment-details?new=1&transaction_id="+res,"_self")  
			
			 window.open("https://test.fdconnect.com/Pay/?sessionToken=" + res + "&configId=PageId2022021713158","_self")
			  
		   }
	   });
 
	 }
 }); 
	   
 
 frappe.ui.form.on("OnlinePayment", "onload", function(frm) {
 	
	//  alert ("hello");
	 var  queryString = window.location.search;
	//  alert (queryString);
	 var urlParams = new URLSearchParams(queryString);
	 var fpTxnId = urlParams.get('fpTxnId');
	 var encData = urlParams.get('encData')
	 alert (fpTxnId)
	 alert(encData)

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
		 
	   
 
	 