import requests
import os
from datetime import datetime


USER = "tuzaum"
TOKEN = os.environ.get('TOKEN')
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Water Graph",
    "unit": "milliliter",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2000"
}

response = requests.post(url=add_pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)
