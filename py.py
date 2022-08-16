import requests


d = {'profile_id': 'AEC708A3-1CEE-4AD7-9D34-E65BE1BBF88F', 'access_key': '907bc1a9ba323023a6d842724ea56b26', 'amount': '2.00', 'locale': 'en', 'currency': 'USD', 'transaction_type': 'sale', 'reference_number': 'RBTGN09NRO3U0LV', 'transaction_uuid': '1569c697-07d8-44e4-bcc7-10cb49b66525', 'signed_date_time': '2022-08-09T07:31:31Z', 'unsigned_field_names': '', 'signed_field_names': 'profile_id,access_key,amount,locale,currency,transaction_type,reference_number,transaction_uuid,signed_date_time,unsigned_field_names,signed_field_names', 'signature': '3WwhdgNKaErVE3eiqe6G8lVH75SfGzlUE2IeByw54KM='}
sta = requests.post("https://testsecureacceptance.cybersource.com/pay",data=d)

print(sta.status_code)
print(sta.content)

