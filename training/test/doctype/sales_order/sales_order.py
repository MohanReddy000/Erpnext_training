from multiprocessing import Condition
import frappe
#from frappe.model.document import Document
@frappe.whitelist()
def sales_inv(sales_order):
    #sales_order=%(sales_order)s
    query = """ select DISTINCT sii.parent,so.total_qty from `tabSales Order` as so inner join `tabSales Invoice Item` as sii on so.name=sii.sales_order where so.name={sales_order} """.format(sales_order)
    data=frappe.db.sql(query,as_dict=1)
    return data
