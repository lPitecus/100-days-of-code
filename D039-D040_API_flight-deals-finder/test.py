from datetime import datetime, timedelta
import requests
import os

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_KEY = os.environ.get('TEQUILA_KEY')
tomorrow = datetime.now() + timedelta(days=1)
tomorrow_date = str(tomorrow.strftime("%d/%m/%Y"))
six_months = datetime.now() + timedelta(days=6*30)
six_months_date = str(six_months.strftime("%d/%m/%Y"))


def get_flight_data(city_code: str):
    headers = {
        "apikey": TEQUILA_KEY
    }

    parameters = {
        "fly_from": "LON",
        "fly_to": city_code,
        "date_from": tomorrow_date,
        "date_to": six_months_date,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "curr": "GBP"

    }
    response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['data'][0]['price']


print(get_flight_data("BER"))
