import pyzmail
from imapclient import IMAPClient

sender = []
subject = []
body = []


def setLastMessages(email, password):
    server = IMAPClient('imap.gmail.com', use_uid=True, ssl=True)
    server.login(email, password)
    # select_info = server.select_folder('Inbox')

    unseenMessages = server.search(['UNSEEN'])
    # unseenMessages = server.search(['SINCE', '21-Oct-2019'])

    rawMessage = server.fetch(unseenMessages, ['BODY[]', 'FLAGS'])

    sender.clear()
    subject.clear()
    body.clear()
    for msgNum in unseenMessages:
        message = pyzmail.PyzMessage.factory(rawMessage[msgNum][b'BODY[]'])
        sender.append(message.get_address('from'))
        subject.append(message.get_subject())
        body.append(message.text_part.get_payload().decode(message.text_part.charset))


def getBody():
    return body


def getSubject():
    return subject


def getSender():
    return sender
