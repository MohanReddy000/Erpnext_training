// Copyright (c) 2022, m and contributors
// For license information, please see license.txt

frappe.ui.form.on('Details', {
	 refresh: function(frm) {

	 },
	/*before_save:function(frm){
		frappe.msgprint("Saved sucessfully")
	},*/
	after_save:function(frm){
		frappe.msgprint("Saved sucessfully123")
	},
	phno:function(frm,cdt,cdn){
		frappe.model.set_value(cdt, cdn, 'addres',frm.doc.phno);
		
	
		//console.log(l)
		console.log("mohan");

	},
	addres:function(frm,cdt,cdn){
		$.each(frm.doc.training, function(idx, row){
			row.addr = frm.doc.addres;
		});
		frm.refresh()
	},
	setup: function(frm) {
		frm.set_query("customer", function() {
			return {
				filters: [
					["Customer","customer_group", "in", ["Individual"]]
				]
			}
		});
	},
	
	

});
frappe.ui.form.on('Training', {
	training_add:function(frm,cdt,cdn){
		var d = locals[cdt][cdn];
		console.log("added")
		frm.refresh()

	}
	
})

