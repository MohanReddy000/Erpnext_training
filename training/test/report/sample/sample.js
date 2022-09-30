// Copyright (c) 2022, m and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sample"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options" : "Customer",
			"width": "80",
			"reqd": 0
		},
		{
			"fieldname":"status",
			"label": __("Status"),                  
			"fieldtype": "Select",
			"options" :["","Draft","To Deliver and Bill","Overdue","To Deliver"],
			"width": "80",
			"reqd": 0
		},
		

	]
};
