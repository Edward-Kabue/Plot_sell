import base64
import keys
import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
from datetime import datetime
from encoding import generate_password


#print(datetime.now())
#2020-09-10 12:21:56.749222  
unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)

data_to_encode = (keys.business_shortCode+keys.lipa_na_mpesa_passkey + formatted_time)

encoded_string =base64.b64encode(data_to_encode.encode())
    #print(encoded_string)

decoded_string = encoded_string.decode()





my_access_token = generate_access_token()

def lipa_na_mpesa():
    access_token = generate_access_token()
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