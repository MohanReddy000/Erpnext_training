
import frappe
def before_update_after_submit(doc,method):
    #doc=frappe.get_doc("Sales Order","SAL-ORD-2022-00009")

    
    for i in doc.items:
        i.sample_ord = doc.sample_order
        '''print(frappe.db.get_value("Sales Order","SAL-ORD-2022-00009","sample_order"))
    if frappe.ui.form.on(“Sales Order”, {on_submit: function(frm) {if(frm.doc.sample_order ==True){doc.db.update(Sample_ord);
}
}
});  '''

