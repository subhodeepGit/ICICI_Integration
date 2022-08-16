frappe.ready(function() {
	frappe.web_form.after_load = () => {
		frappe.web_form.on('transaction_id', (field,value)=>{
			let data=frappe.web_form.get_values();
			let id=frappe.web_form.get_values();
			let session_id= id.transaction_id;
			alert(session_id);
			
			if (data.transaction_id !=0){
				// window.open("https://test.fdconnect.com/Pay/?sessionToken=FFQISRISKYWMJHX2IMS&configId=PageId2022021713158")
				// window.open("https://test.fdconnect.com/Pay/?sessionToken=" + session_id + "&configId=PageId2022021713158")
				window.location.replace("https://test.fdconnect.com/Pay/?sessionToken=" + session_id + "&configId=PageId2022021713158","_self")


		
			}
		});
	}
	
	
})






