# Copyright (c) 2022, m and contributors
# For license information, please see license.txt

import frappe
from frappe import _



def execute(filters=None):
	conditions = get_conditions(filters)
	columns = get_columns()
	data = get_data(filters,conditions)
	return columns,data
def get_columns():
	columns = [
		{
			"fieldname": "name",
			"label": _("Sales Order"),
			"fieldtype": "Link",
			"options": "Sales Order",
			"width": 160
		},
		{
			"fieldname": "transaction_date",
			"label": _("transaction_date"),
			"fieldtype": "Date",
			"width": 120
		},
		{
			"fieldname": "delivery_date",
			"label": _("Delivery Date"),
			"fieldtype": "Date",
			"width": 120

		},
		{
			"fieldname":"customer",
			"label": _("Customer"),
			"fieldtype": "Link",
			"options" : "Customer",
			"width": "160"

		},
		{
			"fieldname":"customer_type",
			"label": _("Customer Type"),
			"fieldtype": "Select",
			"options" :["Company","dividual"],
			"width": "100"
			
		},
		{
			"fieldname":"customer_group",
			"label": _("Customer Group"),
			"fieldtype": "Link",
			"options" : "Customer Group",
			"width": "100"
		},
		{
			"fieldname":"item_code",
			"label": _("Item code"),
			"fieldtype": "Data",
			"width": "120"

		},
		{
			"fieldname":"rate",
			"label": _("Item Rate"),
			"fieldtype": "Currency",
			"width": "100"

		},
		{
			"fieldname":"qty",
			"label": _("Quantity"),
			"fieldtype": "Float",
			"width": "100",
		},
		{
			"fieldname":"amount",
			"label": _("Amount"),
			"fieldtype": "Currency",
			"width": "80"
		},
		{
			"fieldname":"status",
			"label": _("Status"),
			"fieldtype": "Select",
			"options" :["","Draft","To Deliver and Bill","Overdue"],
			"width": "100"
		},
		{
			"fieldname":"parent",
			"label": _("Sales Invoice Name"),
			"fieldtype": "Link",
			"options" : "Sales Invoice",
			"width": "100"

		}
	]
	return columns
def get_data(filters,conditions):
	data = frappe.db.sql(f"""Select  so.name,so.transaction_date,so.delivery_date,so.customer,c.customer_type,so.customer_group,soi.item_code,
	soi.rate,soi.qty,soi.amount,so.status,
	(SELECT GROUP_CONCAT( DISTINCT si.parent ) FROM `tabSales Invoice Item` si where si.sales_order=so.name group by si.sales_order) as "parent"
	from `tabSales Order` as so 
	Left join `tabSales Order Item` as soi on so.name=soi.parent
	inner join `tabCustomer` as c on so.customer=c.customer_name
	where {conditions} """.format(conditions=conditions),as_dict = True)
	
	return data


def get_conditions(filters):
	conditions = ""
	if filters.get('from_date') and filters.get('to_date'):
		conditions += " so.transaction_date between '{0}' and '{1}'".format(filters.get('from_date'), filters.get('to_date'))
	if filters.get('customer'):
		conditions += " AND  so.customer = '{}'".format(filters.get('customer'))
	if filters.get('status'):
		conditions += " AND  so.status = '{}'".format(filters.get('status'))
	
	return conditions
