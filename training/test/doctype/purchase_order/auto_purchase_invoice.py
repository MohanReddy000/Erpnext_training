import frappe
def on_submit(doc,method):
    sr_doc=frappe.get_doc(dict(doctype = 'Purchase Receipt',
    supplier_name=doc.supplier_name,
    transaction_date=doc.transaction_date,
    schedule_date=doc.schedule_date,
    supplier_address=doc.supplier_address,
    ))
    for val in doc.items:
        sr_doc.append('items', {
        'item_code':val.item_code,
        'item_name':val.item_name,
        'description':val.description,
        'qty':val.qty,
        'stock_uom':val.stock_uom,
        'uom':val.uom,
        'rate':val.rate,
        'expense_account':'Legal Expenses - P',
        'purchase_order':doc.name
        })
    for i in doc.taxes:
        sr_doc.append('taxes',{
        'charge_type' : i.charge_type,
        'account_head' : i.account_head,
        'rate' : i.rate,
        'tax_amount' : i.tax_amount,
        'total' : i.total,
        })
        
    sr_doc.save()
