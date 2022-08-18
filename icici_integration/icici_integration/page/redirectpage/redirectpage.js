// frappe.pages['redirectpage'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'REDIRECT',
// 		single_column: true
// 	});
// }
frappe.pages['redirectpage'].on_page_load = function(wrapper) {
	new PageContent(wrapper);
};
PageContent = Class.extend({
	init:function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'You are redirecting to merchant site...',
			single_column: true
		});

		this.make();
	},

	make: function(){
		let htmlContent = 
  ` <div class="card">
    <div class="card-body">
		<figure class="text-center">
		<p class="h1">Instruction for Filling PBAS Form</p>
		</figure>
	  <ul>
     <h4> <li>This form is categorised in four sections:</li></h4>
			<ul>
			<h5><li>
				General Information
			</li>
			<li>
				Category A: Teaching
			</li>
			<li>
				Category B: Administrative And Students Related Activities.
			</li>
			<li>
				Category C: Academic And Research Activities.
			</li></h5>
			</ul>
     <h4><li>General Information</li></h4>
	 <ul>
			<h5><li>
				Employee will able to view his details like Name, Department, Designation, Date of Joining, Educational Qualification and so on.
			<li>
				Employee needs to enter the current appraisal year.
			</li>
	 </ul>
	 <h4><li>Category A: Teaching</li></h4>
	 <ul>
			<h5>
			<li>
				Employee needs to select the respective course from the dropdown in course field.
			<li>
				Employee needs to fill the level (example:UG,PG,Ph.D,etc) and the mode of teaching (example:Lecture,Seminar,Tutorials & Practicals).
			</li>
			<li>
				Employee needs to enter the number of classess alloted to him and the number of classes he/she conducted. On the basis of this the employee will be able to see his/her Percentage of classess taken and the Grade.
			</li>
			<li>
			Grading Criteria (Based on Percentage of Class Conducted)
			</li>
			<ul>
			<li>
			Good - 80% & Above.
			</li>
			<li>
			Satisfactory - Below 80% but 70% & Above
			</li>
			<li>
			Not Satisfactory - Less than 70%
			</li>
			</ul>
	
     
    </ul>
	<h4> <li>
	  Category B-Administrative and Student Related Activities
	  </li></h4>
	  <ul>
			<h5>
			<li>
			In Administrative Responsibility table and Student Related Co curricular Extension Table:
			</li>
			<ul>
			<li>
			Employee needs to fill the Nature of the Job such as :-
			</li>
			<ul>
			<li>
			DEAN
			</li>
			<li>
			DIRECTOR
			</li>
			<li>
			CHAIRPERSON CO-ORDINATORS
			</li>
			<li>
			WARDEN ETC.
			</li>
			</ul>
			<li>
			Employee neeeds to fill the From Date, To Date and Duration(Day/Hr).
			</li>
			<li>
			Employee needs to select the Grading Criteria on the basis of:
			</li>
			<ul><li>Good - Involved in at least 3 Activities</li></ul>
			<ul><li>Satisfactory - Involved in 1-2 Activities</li></ul>
			<ul><li>Not Satisfactory - Not Involved in any of the Activities</li></ul>
			</ul>
	 </ul>
	 <ul>
	 <h5>
	 <li>
	 In Examination Duties Assigned And Performed:
	 </li>
	 <ul>
	 <li>
	 Employee needs to fill the types of Examination Duties, Assigned Duties, From and To Date, Duration(Day/Hr)
	 </li>
	 <li>
	 Employee needs to select the Grading Criteria on the basis of:
	 </li>
	 <ul><li>Good - Involved in at least 3 Activities</li></ul>
	 <ul><li>Satisfactory - Involved in 1-2 Activities</li></ul>
	 <ul><li>Not Satisfactory - Not Involved in any of the Activities</li></ul>
	 </ul>
</ul>
<h4> <li>
	  Category C-Academic and Research Activities 
	  </li></h4>
	  <ul>
			<h5>
			<li>
			In Research Paper Indexed in UGC-Care list Table:
			</li>
			<ul>
			<li>
			Employee needs to fill the Title of the paper, Name of the Journal, No. of Authors, Author Type(single/first/corresponding/co-author), Thomson Reuters Impact Factor, WoS URL Link, Research Score Claimed.
			</li>
			<li>
			After filling the Research Score Claimed, the employee can able to see his/her Final Research Score Claimed.
			</li>
			<ul>
			<li>
			Score for Journal Papers indexed in UGC – CARE list : 15
			</li>
			<li>
			The score may be augmented with Thomson ─ 
			</li>
			<ul><li>Reuters Impact factor < 1: +5</li>
			<li>etween 1 and 2: +10</li>
			<li>between 2 and 5: +15</li>
			<li>between 5 and 10: +20 and above 10: +25</li>
			</ul>
			<li>
			For Joint publications - Two authors: 70 % of total value of publication for each author. 
			</li>
			<ul><li>For more than two authors: 70% of total value for First / Corresponding author and 30% of total value of publication for each the joint authors.</li></ul>
			</ul>
			
	 </ul>
	 <ul>
	 <h5>
	 <li>
	 In Publications other than research papers table:
	 </li>
	 <ul>
	 <li>
	 Employee needs to fill the Title of the Book,	Name of the Publisher, Author Type(single/First/corresponding/co-author), Research Score Claimed, etc.		   
	 </li>
	 <li>
			After filling the Research Score Claimed, the employee can able to see his/her Final Research Score Claimed.
	</li>
	 <li>
	 Employee needs to select the level(International/National) and on the basis of this the level score will be automatically generated.
	 </li>
	 
	 </ul>
</ul>
		<a class="btn btn-primary" href="http://pbas.soulunileaders.com:8000/app/self-appraisal-form" role="button">Proceed to Self Appraisal</a>
		</div>
		</div>
		`;
    <script>
		const queryString = window.location.search;
		const urlParams = new URLSearchParams(queryString);
		const fpTxnId = urlParams.get('fpTxnId');
		const enData = urlParams.get('encData');
		const docname = urlParams.get('id');
		// alert (fpTxnId);
		// alert (enData);

		// window.open("http://localhost:8000/app/onlinepayment/"+ docname +"?"+ "fptxnid="+ fpTxnId,"_self");
		window.open("http://localhost:8000/app/onlinepayment/"+ docname ,"_self");

		// window.open("http://10.0.163.42:8000/app/onlinepayment/"+ docname +"?"+ "fpTxnId="+ fpTxnId,"_self");
	</script>
		$(frappe.render_template( htmlContent, this )).appendTo(this.page.main)
	},

});