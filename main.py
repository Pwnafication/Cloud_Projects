
import requests
import random
import time

NIX_API_APP_ID = "31883f7d"
NIX_API_APP_KEY = "008f3a8d6d0707b98f341c6e4e090d28"

NIXstatic_URL = "https://trackapi.nutritionix.com"
exerciseEP = "/v2/natural/exercise"

headers = {
    "x-app-id": NIX_API_APP_ID,
    "x-app-key": NIX_API_APP_KEY
}

parameters = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

request = requests.post(f"{NIXstatic_URL}{exerciseEP}", headers=headers, json=parameters)
data = request.json()

print(request)
print(data)