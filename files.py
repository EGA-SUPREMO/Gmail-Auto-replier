import json
import objcrypt


def writeEncJSON(key):
    data = {}

    with open('config.cg', 'w') as outfile:
        crypter = objcrypt.Crypter(key, 'cbc')
        json_file = json.dumps(data, ensure_ascii=False)
        enc_json = crypter.encrypt_json(json_file)
        outfile.write(enc_json)
        outfile.close()


def writeJSON():
    data = {}
    data['config'] = []
    data['config'].append({
        'email': '@gmail.com',
        'password': '',
        'keywords': ['mother', 'worried'],
        'white_list': ['@gmail.com'],
        'data_emails': ['', '', ''],
        'websites': ''
    })

    with open('temp.tm', 'w') as outfile:
        json_file = json.dumps(data, ensure_ascii=False)
        outfile.write(json_file)
        outfile.close()


def readEncJSON(key):
    with open('config.cg', 'r') as json_file:
        crypter = objcrypt.Crypter(key, 'cbc')
        str_json = json_file.read()
        data = crypter.decrypt_json(str_json)
        dec_json = json.loads(data)
        return dec_json['config']


def readJSON():
    with open('temp.tm', 'r') as json_file:
        str_json = json_file.read()
        data = str_json
        read_json = json.loads(data)
        return read_json['config']
