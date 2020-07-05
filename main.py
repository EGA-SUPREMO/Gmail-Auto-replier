import receive
import files
import time
import send
import random
from datetime import datetime
from urllib.request import urlopen


def contains_word(s, w):
    return f' {s} ' in f' {w} '


res = urlopen('http://just-the-time.appspot.com/')
result = res.read().strip()
resultStr = result.decode('utf-8')

OnlineUTCTime = datetime.strptime(resultStr, '%Y-%m-%d %H:%M:%S')

try:
    data = files.readJSON()[0]
except Exception:
    files.writeJSON()
    data = files.readJSON()[0]

while True:
    print('next')
    try:
        receive.setLastMessages(data["email"], data["password"])
        texts = receive.getBody()
        sender = receive.getSender()
        subject = receive.getSubject()

        hasKeywords = False

        for i in range(len(texts)):
            for emlist in data["white_list"]:
                if emlist == sender[i][1]:
                    for word in data["keywords"]:
                        print(contains_word(word, texts[i]))
                        if word not in texts[i]:
                            hasKeywords = False
                            break
                        else:
                            hasKeywords = True

                    if hasKeywords:
                        randomEmail = data["data_emails"][random.randint(0, len(data["data_emails"]) - 1)]

                        time.sleep(random.randint(120, 300))
                        if OnlineUTCTime.day < 24:
                            send.sendEmail(data["email"], data["password"], sender[0][1], subject[0], randomEmail)
                        break
    except Exception as ignored:
        print(ignored)
    time.sleep(322)
