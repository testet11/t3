from time import process_time_ns
import requests
import base64 
from decouple import config


domain = "localhost:8000"
order_url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
auth_url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
PAYPALSECRETKEY="EIR-2tGzHYXXed5WY_INeuIToOA1qnL6yRYp0OdpG0yjCY8_-Z-NptwNLern9rwsFpzVFe6XqfyL2nYu"
PAYPALCLIENTID="AcjHTGur64TWf-OnkbMy_-cxbJ7eTtSKhpBI68-L6YrFTYRMfozsbRQJe0dolLlsiqWIpK0Fz3ArfSbG"
 
def PaypalToken():
    try:
        url = auth_url
        data = {
                    "client_id":config("PAYPALCLIENTID"),
                    "client_secret":config("PAYPALSECRETKEY"),
                    "grant_type":"client_credentials"
                }
        headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": "Basic {0}".format(base64.b64encode((config("PAYPALCLIENTID") + ":" + config("PAYPALSECRETKEY")).encode()).decode())
                }
        response = requests.post(url, data, headers=headers)
        if response.status_code == 200:
            print(response.json()["access_token"])
            with open('.paypaltoken', 'w') as token:
                
                print((response.json()["access_token"]))
                token.write((response.json()["access_token"]))
            return True
        return False
    except Exception as e:
        print(e)
        return False


def get_token():
    try:
        with open('.paypaltoken', 'r') as token:
            data = token.readline()
            print("ddd")
            return data
    except FileNotFoundError:
        if PaypalToken():
            with open('.paypaltoken', 'r') as token:
                data = token.readline()
                print("ss")
                return data
        else:
            return ''


def generatePayPalUrl(orderId,amount):
    try:
        token = get_token()
        headers = {"Content-Type": "application/json", "Authorization": 'Bearer ' + token}
        
        data = {"intent":"CAPTURE",
                "application_context": {
                    "return_url": domain+"/payment/paypalsuccess/",
                    "cancel_url": domain + "/payment/cancel/",
                    "landing_page": "BILLING",
                    "user_action": "CONTINUE"
                },
                "purchase_units":[
                    {"reference_id": orderId,
                        "amount":
                         {
                             "currency_code":"USD",
                             "value":str(amount)
                         }
                    }
                ]
                }
        response = requests.post(url=order_url, json=data, headers=headers)
        if response.status_code == 401:
            if PaypalToken():
                return "system_try_again"
            else:
                return "temporary error please try again letter"
        elif (response.status_code == 201) and response.json()["status"] == 'CREATED':
            return response.json()["links"][1]["href"]
        else:
            return response.content 
    except Exception as e:
        return e

#print(generatePayPalUrl("12333",12))
def verifyPayment(paymentToken):
    token = get_token()
    url= order_url+paymentToken+"/capture"
    headers = {"Content-Type": "application/json",
               "Authorization": 'Bearer ' + token}
    response = requests.post(url=url, headers=headers)
    if response.status_code == 401:
        if PaypalToken():
            dic = {
                "Status": "system_try_again",
            }
            return dic
        else:
            dic = {
                "Status": "NotPaid",
                "message": "temporary error please try again letter"
            }
            return dic
    if response.status_code == 422:
        dic = {
            "Status": "NotPaid",
            "message": "this payment token is already verified before you cant use "
                       "this payment token for new payment request"
        }
        return dic
    else:
        responseJson = response.json()
        if responseJson["status"] == 'COMPLETED':
            data = {
                "Status": "Paid",
                "orderId": responseJson["purchase_units"][0]["reference_id"],
                "transactionId": token,
                "totalAmount": float(responseJson["purchase_units"][0]["payments"]["captures"][0]["amount"]["value"])
            }
            return data
        dic = {
            "Status": "NotPaid",
            "message": "unknown please try letter or report problem"
        }
        return dic


