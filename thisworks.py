import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('cxiesestro@gmail.com', 'secretPlease')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.
result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

# fetch the email body (RFC822) for the given ID
result, data = mail.fetch(latest_email_id, "(RFC822)") 

raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads

import email
email_message = email.message_from_string(str(raw_email))
 
#print (email_message['To'])
 
print (email.utils.parseaddr(email_message['From']))
 
#print (email_message.items()) # print all headers
print(email_message.get_payload(decode=True))
# note that if you want to get text content (body) and the email contains
# multiple payloads (plaintext/ html), you must parse each message separately.
# use something like the following: (taken from a stackoverflow post)
def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    print(email_message_instance.get_payload())
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload(decode=True)

body = ""

if email_message.is_multipart():
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        # skip any text/plain (txt) attachments
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
# not multipart - i.e. plain text, no attachments, keeping fingers crossed
else:
    body = email_message.get_payload(decode=True)
