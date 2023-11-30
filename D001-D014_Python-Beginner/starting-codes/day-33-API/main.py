"""oi"""
import requests
import datetime as dt

MY_LAT = -5.794560
MY_LONG = -35.210400

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()['iss_position']
# longitude = data['longitude']
# latitude = data['latitude']
#
# position = (latitude, longitude)
#
# print(position)


parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]


print(sunrise)
print(dt.datetime.now())
