import base64
import keys


from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

  

def generate_password(formatted_time):

    data_to_encode = (keys.business_shortCode+keys.lipa_na_mpesa_passkey + formatted_time)

    encoded_string =base64.b64encode(data_to_encode.encode())
    #print(encoded_string)

    decoded_string = encoded_string.decode()
    #print(decoded_string)
    return decoded_string