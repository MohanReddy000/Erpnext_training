import frappe
def before_save(doc,method=None):
    frappe.sendmail(recipients="mr881789@gmail.com",
        sender = "mohan.k@promantia.com",
		subject="Sales invoice is Submitted",
		message= "succesfully submited sales invoice"
        )



'''def send_email_to_party(self):
    content = frappe.render_template( {
		'recipient_name': self.recipient_name,
		'email': self.email
	    #put here the variables in the template
	}) 
frappe.sendmail(
		recipients = self.email, #this is the email to your recipient as you want
		sender = "your_sender_email",
		subject = "The subject of your email",
		content = content,
		now = True
	)'''