frappe.ui.form.on("Sales Order", {
	onload:function(frm) {
        //console.log("mohan")
        
		 
        if(frm.doc.status==='To Deliver and Bill'){
            frm.add_custom_button('Sales Invoice Fetch', function(){
                frm.trigger("sales");
            });
            // frm.refresh();
            
        }
        
    },
	/*sales_order: function(frm){
		var enable = frm.get_field("firmware_version").df.readonly;
		frm.toggle_enable('firmware_version', enable);
	}*/
    

    sales:function(frm){
        console.log("something")
        
        frappe.call({
             method:"training.test.doctype.sales_order.sales_order.sales_inv",
             args:{"sales_order":frm.doc.name},
             callback:function(r){
                if(r.message) {
                    console.log(r.message)
                    cur_frm.clear_table("sales_invoice_created")
                    
                    for(var i=0;i<r.message.length;i++){
                        var child = cur_frm.add_child("sales_invoice_created");
                        child.sales_invoice=r.message[i].parent;
                        child.total_qty=r.message[i].total_qty;
                    
                    }
                    
                    refresh_field("sales_invoice_created")
                    //for(var i=0;i<r.message.length;i++){
                      //  frappe.msgprint( +r.message[i]['SalesInvoice'])
                    //}
                    frm.save();
        
                    
                    
                 }
 
             }
         
         })
     }
        
});
    