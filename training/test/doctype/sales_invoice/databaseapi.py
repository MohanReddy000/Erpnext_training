import frappe
def on_submit(doc,method):
    #f=frappe.db.sql(""" select employee_name,employment_type,company,gender,date_of_birth,date_of_joining,designation from `tabEmployee` where status="Active"  """,as_dict=True)
    #print(f)

    fo=frappe.db.sql(""" select DISTINCT item_name,item_code,rate,amount from `tabSales Invoice Item`,`tabSales Invoice` where status="Draft" and posting_date BETWEEN '2022-08-01' and sysdate()""")
    print(fo)