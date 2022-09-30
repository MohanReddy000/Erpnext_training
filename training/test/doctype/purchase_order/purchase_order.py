import frappe
def on_submit(doc,method):
    for i in doc.items:
        i.sample_pur =doc.sample_purchase