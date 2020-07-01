import yagmail

def sendEmail(email, passw, receiver, esubject, body):
	yag = yagmail.SMTP(email, passw)
	yag.send(
	    to=receiver,
	    subject=esubject,
	    contents=body
	)