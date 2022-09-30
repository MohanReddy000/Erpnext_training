import frappe

def on_submit(doc,method=None):
    new_sheet=frappe.get_doc(dict(doctype= "Sales Invoice",
    customer_name=doc.customer_name,
    customer=doc.customer,
    sales_type=doc.sales_type,
    transaction_date=doc.transaction_date,
    delivery_date=doc.delivery_date,
    contact_mobile=doc.contact_mobile,
    due_date=doc.delivery_date
    ))
    for val in doc.items:
        new_sheet.append('items',{
        'item_code':val.item_code,
        'delivery_date':val.delivery_date,
        'item_name':val.item_name,
        'description':val.description,
        'gst_hsn_code':val.gst_hsn_code,
        'qty':val.qty,
        'stock_uom':val.stock_uom,
        'conversion_factor':val.conversion_factor,
        })
    for i in doc.taxes:
        new_sheet.append('taxes',{
        'charge_type':i.charge_type,
        'description':i.description,
        'account_head':i.account_head,
        'rate':i.rate,
        'tax_amount':i.tax_amount,
        'total':i.total
        })
    
    new_sheet.insert(ignore_mandatory=True)
            