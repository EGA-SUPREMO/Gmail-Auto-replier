import imaplib, email, base64


def fetch_messages(username, password):
    messages = []
    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    conn.login(username, password)
    conn.select()
    typ, data = conn.uid('search', None, 'ALL')
    print("hey")
    for num in data[0].split():
        typ, msg_data = conn.uid('fetch', num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                messages.append(str(email.message_from_string(str(response_part[1]))))
        typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
    return messages

fetch_messages('cxiesestro@gmail.com', 'secretPlease')