from xml.dom.minidom import Document
from . import __version__ as app_version

app_name = "training"
app_title = "test"
app_publisher = "m"
app_description = "test d"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mr"
app_license = "MIT"
fixtures=[
{
"dt": "Custom Field",
        "filters": [
         [
             "name", "in", [
		        "Sales Order-category"
                "Sales Order-sales_type"
                "Purchase Order-itemtype"
                "Sales Invoice-email"
		        "Sales Order-sample_order"

]
]
]
},
{
"dt": "Property Setter",
        "filters": [
         [
             "name", "in", [
		"Make"
]
]
]
},
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/training/css/training.css"
# app_include_js = "/assets/training/js/training.js"

# include js, css files in header of web template
# web_include_css = "/assets/training/css/training.css"
# web_include_js = "/assets/training/js/training.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "training/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
	"Sales Order" : "test/doctype/sales_order/sales_order.js"
	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "training.install.before_install"
# after_install = "training.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "training.uninstall.before_uninstall"
# after_uninstall = "training.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "training.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
	"Sales Order":{
		#"before_update_after_submit" : "training.test.doctype.salesorder.salesorder.before_update_after_submit",
		#"on_submit" : "training.test.doctype.salesorder.auto_sales_invoice.on_submit"
	},
	"Purchase Order":{
		"on_submit" : "training.test.doctype.purchase_order.purchase_order.on_submit",
		#"on_submit" :"training.test.doctype.purchase_order.auto_purchase_invoice.on_submit"
	},
	"Purchase Receipt": {
		#"on_submit": "training.test.doctype.purchase_order.send_mail.on_submit"
		"on_submit" :"training.test.doctype.salesorder.databaseapi.on_submit"
	}
}
#doc_events = {
#	"Purchase Order":{
#		"on_submit" : "training.test.doctype.purchase_order.purchase_order.on_submit",
#		"on_submit" :"training.test.doctype.purchase_order.auto_purchase_invoice.on_submit"
#	}
#}

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"training.tasks.all"
#	],
#	"daily": [
#		"training.tasks.daily"
#	],
#	"hourly": [
#		"training.tasks.hourly"
#	],
#	"weekly": [
#		"training.tasks.weekly"
#	]
#	"monthly": [
#		"training.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "training.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "training.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "training.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"training.auth.validate"
# ]

