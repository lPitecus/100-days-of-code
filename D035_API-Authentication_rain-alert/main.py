import requests
import os
from twilio.rest import Client

# TODO: descobrir como rodar o script todo dia pela manhã

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
SMS_API_KEY = os.environ.get('SMS_API_KEY')
SMS_SID = os.environ.get('SMS_SID')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
MY_LAT = -5.779257
MY_LONG = -35.200916

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()['hourly']

# coletar os códigos de clima das próximas 12 horas
weather_next_twelve_hours = [int(item['weather'][0]['id']) for item in weather_data[:12]]

# checar se em algum momento do dia irá chover
for item in weather_next_twelve_hours:
    if item < 700:
        account_sid = SMS_SID
        auth_token = SMS_API_KEY
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="Vai chover hoje. Coloque o guarda chuva no carro.",
                from_=TWILIO_NUMBER,
                to=os.environ.get('MY_NUMBER')
            )
        print(message.status)
        break
print(weather_next_twelve_hours)
