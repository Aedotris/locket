import requests
from locket import Auth, LocketAPI
import json


auth = Auth('email', 'password') 
token = auth.get_token()

api = LocketAPI(token)

account_info = api.GetAccountInfo()
# print(json.dumps(account_info, indent=4))  
momment = api.getLastMoment()
print(momment)