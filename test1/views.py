
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import fi
from urllib import request
from uuid import uuid4 
from datetime import datetime
from base64 import b64encode
from hashlib import sha256
import hmac
import random
import string 
# Create your views here.
from urllib.parse import parse_qs
import paypal
import json
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from . import models


CYBERSOURCE_SECRET_KEY="1aafc984713c4d6a9aa201c0d271a5a0117041614e3e44e7b8cf34c4b33bfad76dc18f2681504919a573a9a7a6fb5cbbfe9f6ec1e50c471c922c08d5e94d85898cb29301efed48f889861ef10442e94319bd2a1d4c0d47c091723fdc6f493c9a0e65a308c4e541c3a3aba1db8d535125fa1abb85e71c483db688e6a3aae651a7"

class av(APIView): 
    @staticmethod
    def post(request, *args, **kwargs):
        data = request.data  

        f = fi()
        f.a = "data"
        f.save()
        signed_fileds = (data.get("signed_field_names")).split(",")
        f.b = signed_fileds
        unsigned_string = ""
        for filed in signed_fileds:
            unsigned_string += f'{filed}={data.get(filed)},'
        unsigned_string = unsigned_string[:-1] 
        f.c = unsigned_string
        digest = hmac.new(
            CYBERSOURCE_SECRET_KEY.encode(),
            msg=unsigned_string.encode(),
            digestmod=sha256,
        ).digest()
        print(b64encode(digest).decode())
        print(str(data.get("signature")))
        f.d = b64encode(digest).decode()
        f.e = data.get("signature")
        if b64encode(digest).decode() == str(data.get("signature")):
            f.f = "1"
            print(1)
        else:
            f.f = "2"
            print(2)
        f.save()
        return HttpResponse(b64encode(digest).decode())

@csrf_exempt
def a(request):  
    data = b'req_ship_to_surname=rome&req_card_number=xxxxxxxxxxxx1111&req_locale=en&req_ship_to_forename=romeo&signature=uG%2FeRLhdUgGaqzT3QXQ%2BWzZVbnnWgdETrMX2Ugc3caU%3D&req_card_type_selection_indicator=1&auth_trans_ref_no=7219916746LQGBEZ&req_bill_to_surname=rome&req_bill_to_address_city=ad&req_card_expiry_date=12-2022&req_bill_to_address_postal_code=125542&req_bill_to_phone=%2B2519115522&card_type_name=Visa&reason_code=100&auth_amount=2.01&auth_response=100&bill_trans_ref_no=7219916746LQGBEZ&req_bill_to_forename=romeo&req_payment_method=card&request_token=Axj%2F%2FwSTZh5llWEZvW3CABEg3ZMXLli2btG0yjHhRbSiOQjskNgFRHIR2SG2kCMkizhk0ky9GLO9R4MCcmzDzLKsIzetuEAA5xux&req_device_fingerprint_id=54dbc1f5160a4c98821b2a015853a870&auth_time=2022-08-16T011430Z&req_amount=2.01&req_bill_to_email=e%40gmail.com&auth_avs_code_raw=I1&transaction_id=6606124699426081304002&req_currency=USD&req_card_type=001&decision=ACCEPT&req_ship_to_address_country=GB&req_ship_to_phone=%2B2519115522&message=Request+was+processed+successfully.&signed_field_names=transaction_id%2Cdecision%2Creq_access_key%2Creq_profile_id%2Creq_transaction_uuid%2Creq_transaction_type%2Creq_reference_number%2Creq_amount%2Creq_currency%2Creq_locale%2Creq_payment_method%2Creq_bill_to_forename%2Creq_bill_to_surname%2Creq_bill_to_email%2Creq_bill_to_phone%2Creq_bill_to_address_line1%2Creq_bill_to_address_city%2Creq_bill_to_address_country%2Creq_bill_to_address_postal_code%2Creq_ship_to_forename%2Creq_ship_to_surname%2Creq_ship_to_phone%2Creq_ship_to_address_line1%2Creq_ship_to_address_city%2Creq_ship_to_address_country%2Creq_ship_to_address_postal_code%2Creq_card_number%2Creq_card_type%2Creq_card_type_selection_indicator%2Creq_card_expiry_date%2Ccard_type_name%2Creq_device_fingerprint_id%2Cmessage%2Creason_code%2Cauth_avs_code%2Cauth_avs_code_raw%2Cauth_response%2Cauth_amount%2Cauth_code%2Cauth_trans_ref_no%2Cauth_time%2Crequest_token%2Cbill_trans_ref_no%2Csigned_field_names%2Csigned_date_time&req_transaction_uuid=1e85249d-ef09-4093-887f-a61f2cbad350&auth_avs_code=X&auth_code=888888&req_ship_to_address_postal_code=125542&req_bill_to_address_country=GB&req_transaction_type=sale&req_access_key=1ab344542a273aca8764448fd499f77a&req_profile_id=3E461628-D9B5-45E8-9D93-0684DDD852B3&req_reference_number=0UYDHVEJI27SQWS&req_ship_to_address_city=ad&req_ship_to_address_line1=adiss&signed_date_time=2022-08-16T01%3A14%3A30Z&req_bill_to_address_line1=adiss'
    data = parse_qs(data.decode('utf-8')) 
    signed_fileds = (data.get("signed_field_names"))[0].split(",")
    unsigned_string = ""
    for filed in signed_fileds:
        unsigned_string += f'{filed}={data.get(filed)[0]},'
    unsigned_string = unsigned_string[:-1] 
    digest = hmac.new(
        CYBERSOURCE_SECRET_KEY.encode(),
        msg=unsigned_string.encode(),
        digestmod=sha256,
    ).digest()
    print(b64encode(digest).decode())
    print(str(data.get("signature")[0]))
    if b64encode(digest).decode() == str(data.get("signature")[0]):
        print(1)
    else:
        print(2)

    return HttpResponse(digest)
def b(request): 
    return render(request,"index.html")