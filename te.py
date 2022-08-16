from uuid import uuid4 
from datetime import datetime
from base64 import b64encode
from hashlib import sha256
import hmac
import random
import string 

CYBERSOURCE_SECRET_KEY1="31f8a7e61407480b952437777626740088c973acf76f454f88054b99dc40a91d0d24c81bc34d473a953cf0bbc728f407a418767fb4d14c889dc12621a5b847ca8b427fc12e434343bf3d38905810fd2d0530267ac6af44d39dd91b6c36e4b1afe4ae879493c5431781b36b8639f7c69218eb4154ca884d77a7c218ee1c6db206"
CYBERSOURCE_ACCESS_KEY1="907bc1a9ba323023a6d842724ea56b26"
CYBERSOURCE_PROFILE_ID1="AEC708A3-1CEE-4AD7-9D34-E65BE1BBF88F"

CYBERSOURCE_SECRET_KEY2="84afd04c7eac4ae6afef29613dee522a93a8c45fb52e41c99270c38de0224daa49fb6bbc570646319067f0143283758c4c52857d8c514e059d0add5e3edab018a9af5f81bb33438cb4261491d091e8979e31a00e2ba04f3bb9867c6a6d007f492e3ca72a2c8340b2acc4abd2e9f071329e9c724bdce14e54bf05a3d86427ac21"
CYBERSOURCE_ACCESS_KEY2="3b9f042401853f2f90398d63a90637d9"
CYBERSOURCE_PROFILE_ID2="52F5EB44-3A64-441F-AC15-F4B60C4A4482"


CYBERSOURCE_SECRET_KEY="1aafc984713c4d6a9aa201c0d271a5a0117041614e3e44e7b8cf34c4b33bfad76dc18f2681504919a573a9a7a6fb5cbbfe9f6ec1e50c471c922c08d5e94d85898cb29301efed48f889861ef10442e94319bd2a1d4c0d47c091723fdc6f493c9a0e65a308c4e541c3a3aba1db8d535125fa1abb85e71c483db688e6a3aae651a7"
CYBERSOURCE_ACCESS_KEY="1ab344542a273aca8764448fd499f77a"
CYBERSOURCE_PROFILE_ID="3E461628-D9B5-45E8-9D93-0684DDD852B3"
def generate_mbirr_reference():
    return ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(15))


def create_sha256_signature(message):
    digest = hmac.new(
        CYBERSOURCE_SECRET_KEY.encode(),
        msg=message.encode(),
        digestmod=sha256,
    ).digest()

    return b64encode(digest).decode()


def sign_boa_fields(fields):
    fields['signed_date_time'] = str(datetime.utcnow().isoformat(timespec='seconds')) + 'Z'
    signed_field_names = [key for key in fields]
    signed_field_names.append('unsigned_field_names')
    fields['unsigned_field_names'] = ''
    signed_field_names.append('signed_field_names')
    fields['signed_field_names'] = ','.join(signed_field_names)

    data_to_sign = [f'{key}={value}' for key, value in fields.items()]
    print(data_to_sign)

    return {
        **fields,
        'signature': create_sha256_signature(','.join(data_to_sign))
    }



def boa(price): 
    data = {
        "profile_id": CYBERSOURCE_PROFILE_ID,
        "access_key": CYBERSOURCE_ACCESS_KEY,
        "amount": str(2.01),
        "locale": "en",
        "currency": "USD",
        "transaction_type": "sale",
        "reference_number": generate_mbirr_reference(),
    }
    
    data["transaction_uuid"] = str(uuid4())
    print(data)
    signed_data = sign_boa_fields(data)

    return signed_data

print(boa(2))