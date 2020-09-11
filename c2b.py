import requests
import keys
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token


def register_url():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = { 
        "ShortCode": keys.ShortCode,
        "ResponseType": " completed ",
        "ConfirmationURL": "https://ibuylocal.co.ke/confirmation",
        "ValidationURL": "https://ibuylocal.co.ke/confirmation"}
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

     
def simulate_c2b_transaction():
    my_access_token = generate_access_token()
    
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = { 
        "ShortCode":keys.ShortCode,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"2",
        "Msisdn":keys.test_msidn,
        "BillRefNumber":"123456" }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)
simulate_c2b_transaction