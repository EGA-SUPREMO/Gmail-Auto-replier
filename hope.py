import easyimap

host = 'imap.gmail.com'
user = 'cxiesestro@gmail.com'
password = input('password: ')
mailbox = 'INBOX.subfolder'
imapper = easyimap.connect(host, user, password, mailbox, ssl=False, port=143)

email_quantity = 3
emails_from_your_mailbox = imapper.listids(limit=email_quantity)
imapper.quit()
print(emails_from_your_mailbox)