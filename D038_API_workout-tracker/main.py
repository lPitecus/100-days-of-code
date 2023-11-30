import os
import requests
from datetime import datetime


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
post = "https://trackapi.nutritionix.com/v2/natural/exercise"

prompt = input("What did you do today?: ")

nutrimix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

text_parameters = {
    "query": prompt,
    "gender": "male",
    "weight_kg": 80.0,
    "height_cm": 170,
    "age": 30
}

response_nutrimix = requests.post(url=post, json=text_parameters, headers=nutrimix_headers)
data_nutrimix = response_nutrimix.json()
print(data_nutrimix)

today = datetime.now()

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for item in data_nutrimix["exercises"]:
    data_to_post = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": item["name"].title(),
            "duration": int(item["duration_min"]),
            "calories": int(item["nf_calories"])
        }
    }
    response_sheety_post = requests.post(
        url=SHEETY_ENDPOINT, json=data_to_post,
        headers=sheety_headers)
    print(response_sheety_post.text)

