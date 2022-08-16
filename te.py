from urllib import request
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
#print(create_sha256_signature("bcd=456,abc=132"))
#print(create_sha256_signature("transaction_id=6606124699426081304002,decision=ACCEPT,req_access_key=1ab344542a273aca8764448fd499f77a,req_profile_id=3E461628-D9B5-45E8-9D93-0684DDD852B3,req_transaction_uuid=1e85249d-ef09-4093-887f-a61f2cbad350,req_transaction_type=sale,req_reference_number=0UYDHVEJI27SQWS,req_amount=2.01,req_currency=USD,req_locale=en,req_payment_method=card,req_bill_to_forename=romeo,req_bill_to_surname=rome,req_bill_to_email=e@gmail.com,req_bill_to_phone=+2519115522,req_bill_to_address_line1=adiss,req_bill_to_address_city=ad,req_bill_to_address_country=GB,req_bill_to_address_postal_code=125542,req_ship_to_forename=romeo,req_ship_to_surname=rome,req_ship_to_phone=+2519115522,req_ship_to_address_line1=adiss,req_ship_to_address_city=ad,req_ship_to_address_country=GB,req_ship_to_address_postal_code=125542,req_card_number=xxxxxxxxxxxx1111,req_card_type=001,req_card_type_selection_indicator=1,req_card_expiry_date=12-2022,card_type_name=Visa,req_device_fingerprint_id=54dbc1f5160a4c98821b2a015853a870,message=Request was processed successfully.,reason_code=100,auth_avs_code=X,auth_avs_code_raw=I1,auth_response=100,auth_amount=2.01,auth_code=888888,auth_trans_ref_no=7219916746LQGBEZ,auth_time=2022-08-16T011430Z,request_token=Axj//wSTZh5llWEZvW3CABEg3ZMXLli2btG0yjHhRbSiOQjskNgFRHIR2SG2kCMkizhk0ky9GLO9R4MCcmzDzLKsIzetuEAA5xux,bill_trans_ref_no=7219916746LQGBEZ,signed_field_names=transaction_id,decision,req_access_key,req_profile_id,req_transaction_uuid,req_transaction_type,req_reference_number,req_amount,req_currency,req_locale,req_payment_method,req_bill_to_forename,req_bill_to_surname,req_bill_to_email,req_bill_to_phone,req_bill_to_address_line1,req_bill_to_address_city,req_bill_to_address_country,req_bill_to_address_postal_code,req_ship_to_forename,req_ship_to_surname,req_ship_to_phone,req_ship_to_address_line1,req_ship_to_address_city,req_ship_to_address_country,req_ship_to_address_postal_code,req_card_number,req_card_type,req_card_type_selection_indicator,req_card_expiry_date,card_type_name,req_device_fingerprint_id,message,reason_code,auth_avs_code,auth_avs_code_raw,auth_response,auth_amount,auth_code,auth_trans_ref_no,auth_time,request_token,bill_trans_ref_no,signed_field_names,signed_date_time,signed_date_time=2022-08-16T01:14:30Z"))
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


"""
uG/eRLhdUgGaqzT3QXQ+WzZVbnnWgdETrMX2Ugc3caU=
uG/eRLhdUgGaqzT3QXQ+WzZVbnnWgdETrMX2Ugc3caU=

b'req_ship_to_surname=rome&req_card_number=xxxxxxxxxxxx1111&req_locale=en&
req_ship_to_forename=romeo&
signature=uG%2FeRLhdUgGaqzT3QXQ%2BWzZVbnnWgdETrMX2Ugc3caU%3D&
req_card_type_selection_indicator=1&auth_trans_ref_no=7219916746LQGBEZ&
req_bill_to_surname=rome&req_bill_to_address_city=ad&req_card_expiry_date=12-2022&
req_bill_to_address_postal_code=125542&req_bill_to_phone=%2B2519115522&
card_type_name=Visa&reason_code=100&auth_amount=2.01&
auth_response=100&bill_trans_ref_no=7219916746LQGBEZ&
req_bill_to_forename=romeo&req_payment_method=card&
request_token=Axj%2F%2FwSTZh5llWEZvW3CABEg3ZMXLli2btG0yjHhRbSiOQjskNgFRHIR2SG2kCMkizhk0ky9GLO9R4MCcmzDzLKsIzetuEAA5xux&
req_device_fingerprint_id=54dbc1f5160a4c98821b2a015853a870&
auth_time=2022-08-16T011430Z&req_amount=2.01&req_bill_to_email=e%40gmail.com&
auth_avs_code_raw=I1&transaction_id=6606124699426081304002&req_currency=USD&
req_card_type=001&decision=ACCEPT&req_ship_to_address_country=GB&
req_ship_to_phone=%2B2519115522&message=Request+was+processed+successfully.&
signed_field_names=transaction_id%2Cdecision%2Creq_access_key%2Creq_profile_id%2Creq_transaction_uuid%2Creq_transaction_type%2Creq_reference_number%2Creq_amount%2Creq_currency%2Creq_locale%2Creq_payment_method%2Creq_bill_to_forename%2Creq_bill_to_surname%2Creq_bill_to_email%2Creq_bill_to_phone%2Creq_bill_to_address_line1%2Creq_bill_to_address_city%2Creq_bill_to_address_country%2Creq_bill_to_address_postal_code%2Creq_ship_to_forename%2Creq_ship_to_surname%2Creq_ship_to_phone%2Creq_ship_to_address_line1%2Creq_ship_to_address_city%2Creq_ship_to_address_country%2Creq_ship_to_address_postal_code%2Creq_card_number%2Creq_card_type%2Creq_card_type_selection_indicator%2Creq_card_expiry_date%2Ccard_type_name%2Creq_device_fingerprint_id%2Cmessage%2Creason_code%2Cauth_avs_code%2Cauth_avs_code_raw%2Cauth_response%2Cauth_amount%2Cauth_code%2Cauth_trans_ref_no%2Cauth_time%2Crequest_token%2Cbill_trans_ref_no%2Csigned_field_names%2Csigned_date_time&
req_transaction_uuid=1e85249d-ef09-4093-887f-a61f2cbad350&auth_avs_code=X&auth_code=888888&
req_ship_to_address_postal_code=125542&req_bill_to_address_country=GB&req_transaction_type=sale&
req_access_key=1ab344542a273aca8764448fd499f77a&req_profile_id=3E461628-D9B5-45E8-9D93-0684DDD852B3&
req_reference_number=0UYDHVEJI27SQWS&req_ship_to_address_city=ad&req_ship_to_address_line1=adiss&
signed_date_time=2022-08-16T01%3A14%3A30Z&req_bill_to_address_line1=adiss'
"""
