 
import requests
d = {"req_transaction_uuid":"02e4f057-f1fe-47bd-91c5-7b9772170d36",
"req_card_number":"1234","card_type_name":"visa",
"req_device_fingerprint_id":"232322",
"message":"accepted","decision":"ACCEP"}
#d = {"status":"PROCESSED","tracenumber":"469cd03e-1216-481d-8999-c2b4e917701f"}
sta = requests.post("https://api.ashewa.com/payments/boa-hook/",
data=d)
print(sta.status_code)
print(sta.content)
print(sta.json)



"""
{"req_transaction_uuid":"02e4f057-f1fe-47bd-91c5-7b9772170d36",
"req_card_number":"1234","card_type_name":"visa",
"req_device_fingerprint_id":"232322",
"message":"accepted","decision":"ACCEPT"}


"""





"""
da = {"sender":{"name":"abebe","mobile_number":"251911223344","account_number":"123456"},
"beneficiary":{"account_number":"12345","mobile_number":"251912332211"},
"transaction":{"amount_in_cents":5700,"operation_type":"no","client_transaction_id":"151609ae-01cc-46f5-8675-70257ec63c2f","customer_care_code":"12","operation_type":"tr"},
"transaction_account":{"balance_after_in_cents":"1234"},
"end_user_message":"151609ae-01cc-46f5-8675-70257ec63c2f",
}
"""
"""query = mutation{tokenAuth(username:"adminapi",password:"admin")
{
user{
  username,
  firstName
}
  token
}
}"""
"""
url = 'http://localhost:8000/graphql'
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)
json_data = json.loads(r.text)
print(json_data["data"])

"""
 