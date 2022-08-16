// Copyright (c) 2022, SOUL ltd and contributors
// For license information, please see license.txt
  frappe.ui.form.on("OnlinePayment", "pay", function(frm) {
	frappe.call({
	  
		  method: "icici_integration.icici_integration.doctype.onlinepayment.onlinepayment.getSessionToken",
		  args: {
			  name:frm.doc.name,
			  amount:frm.doc.amount,
	  },
		  
		  callback: function(r) {
			 
			var res=r.message;
			//var res=frm.doc.amount;   //Testing method
			// alert(res);
			// window.open("http://10.0.160.184:8000/payment-details?new=1&transaction_id="+res,"_self")

			// window.open("http://localhost:8000/payment-details?new=1&transaction_id="+res,"_self")  
			//  redirect to Web form 

			window.open("https://test.fdconnect.com/Pay/?sessionToken=" + res + "&configId=PageId2022021713158","_self")
			 
		  }
	  });

	});  


	// frappe.ui.form.on('OnlinePayment', {
	// onload: function(frm) {
	// 	frappe.call({
	  
	// 		method: "icici_integration.icici_integration.doctype.onlinepayment.onlinepayment.InqueryTransaction",
	// 		args: {
	// 			name:frm.doc.name
	// 	},
			
	// 		callback: function(r) {
											   
	// 			var res=r.message;
	// 			if (res!=undefined){
	// 				alert(res);

	// 			}
	// 			else{
	// 				// alert("No Data Found");
	// 			}
			  
			   
	// 		}
	// 	});
	// 	}
		
	// });
  

	frappe.ui.form.on("OnlinePayment", "click", function(frm) {
		// alert("Clicked")
		frappe.call({
					  
				method: "icici_integration.icici_integration.doctype.onlinepayment.onlinepayment.InqueryTransaction",				
				args: {
					name:frm.doc.name
			},
				
				callback: function(r) {
					// alert("Inquery")											   
					var res=r.message;
					// alert(res);
									  
				   
				}
			});
	
	});
			
		
	  

	
