"""This class is responsible for talking to the Flight Search API.
"""

import requests
from datetime import datetime
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
# noinspection SpellCheckingInspection
TEQUILA_KEY = os.environ.get('TEQUILA_KEY')


class FlightSearch:

    @staticmethod
    def get_city_code(city_name: str) -> str:
        headers = {
            "apikey": TEQUILA_KEY
        }

        parameters = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        code = data['locations'][0]['code']
        return code

    @staticmethod
    def check_flights(origin_city_code, destination_city_code, from_date: datetime,
                      to_date: datetime) -> FlightData:
        headers = {
            "apikey": TEQUILA_KEY
        }

        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"

        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()['data'][0]

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['cityFrom'],
            origin_airport=data['flyFrom'],
            destination_city=data['cityTo'],
            destination_airport=data['flyTo'],
            out_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0]
        )
        return flight_data
