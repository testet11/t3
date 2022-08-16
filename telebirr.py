import json
from urllib import response
import requests 
import requests 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import json
import hashlib
import time
import base64

app_key = "76aa2b8e19344591b49743078241dd19"
app_id = "ff64a3d481f240ea82e9b3b36ea2da2f"
code = "220183" 
u = "http://196.188.120.3:11443/service-openup/toTradeWebPay"


r = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzSVfsyn6ZGzL0aMhl3DS5i2BS0LP73eNERLOoHet6eQtQYkya9zC3asz0COPUheHshC7//kktgM7CqIJXpOgh07zTidb6R0/8vHaVYsZ1zMXuoeMiK1V99ClitJkkwNyWlif3pWgk03Ys0x8JgKAqcGmbQcQQTFgmJVhxAZiiqG6ryWxZ7+Wn3QeZeQXFxIkl2N59lIkKa5o+9pcHUq4jV+NGly9HQPDJBPIqtWRdNy5Ki9uowx1/K2s/Gerpk9NPEADKlbd8vGBbep5dYOeAWb1+x9RhjbSYN6qlNyhyhCnckx12fYKhCLo+X0jtJGoNeFl8haHr0wo7P343ertPwIDAQAB"
def encrypt(data):
    message = json.dumps(data).encode('utf-8')
    public_key = RSA.importKey(open('public.key').read())
    encryptor = PKCS1_v1_5.new(public_key)
    
    length = 117
    offset = 0
    res = []
    
    while len(message) - offset > 0:
        if len(message) - offset > length:
            res.append(encryptor.encrypt(message[offset:offset + length]))
        else:
            res.append(encryptor.encrypt(message[offset:]))

        offset += length

    return base64.b64encode(b''.join(res)).decode('utf8')


def generate_string(ussd_data) -> str:
    ussd_data['appKey'] = app_key
    final_string = ""

    for key in sorted(ussd_data.keys()):
        if ussd_data[key] is None or ussd_data[key] == "":
            continue
        final_string += f'{key}={ussd_data[key]}&'

    return final_string[:-1]  # removing trailing &


def get_signature(data):
    signer = hashlib.new('sha256')
    signer.update(generate_string(data).encode())
    return hashlib.sha256(generate_string(data).encode()).hexdigest()

def create_transaction():
    data = {
        'appId': app_id,
        'nonce': time.time().__int__().__str__(),
        'notifyUrl': "127.0.0.1",
        'outTradeNo': str("123412"),
        'receiveName': "eu",
        'returnUrl': 'https://ashewa.com',
        'shortCode': code,
        'subject': "e PAYMENT",
        'timeoutExpress': '3600',
        'timestamp': time.time().__int__().__str__(),
        'totalAmount': 5,
    }

    request_data = {
        'appid': app_id, 
        'sign': get_signature(data),
        'ussd': encrypt(data)
    }
    result = requests.request(
            'POST',
            u,
            json=request_data
        )

    print(result.content)
    print(result.status_code)
    print(result.json)

create_transaction()

"""
b'{"code":103011,"newCode":"103011","data":null,"message":"The OutTradeNo of request parameter must be unique. The OutTradeNo parameter already exists in the system","dateTime":1660203344516,
"path":"/toTradeWebPay","errorDetails":{},"extraData":{}}'


b'{"code":200,"newCode":"200","data":{"toPayUrl":"http://196.188.120.3:11443/ammwebpay/#/?transactionNo=202208111044451557634108718776322"},"message":"Operation successful","dateTime":1660203885619,
"path":null,"errorDetails":{},"extraData":{}}'


"""