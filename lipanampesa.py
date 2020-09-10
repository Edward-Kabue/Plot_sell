import base64
import keys
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth


#print(datetime.now())
#2020-09-10 12:21:56.749222  
unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)


data_to_encode = keys.business_shortCode+keys.lipa_na_mpesa_passkey + formatted_time
encoded_string =base64.b64encode(data_to_encode.encode())
print(encoded_string)

decoded_string = encoded_string.decode()
print(decoded_string)

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  
#{ "access_token": "5prbZG8hMtQAW5R8WGASwgzqTbcK", "expires_in": "3599"}
json_response = r.json() 

my_access_token = json_response['access_token']

def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_string ,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "10",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://ibuylocal.co.ke/",
        "AccountReference": "12345678 ",
        "TransactionDesc": "pay with mpesa "
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

lipa_na_mpesa()