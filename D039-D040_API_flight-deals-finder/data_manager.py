"""This class is responsible for talking to the Google Sheet.
"""
import requests
import os

SHEETY_KEY = os.environ.get('SHEETY_KEY')


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Reads the information on the Google sheet and returns the table as a dictionary

         :return: self.destination_data - The spreadsheet in a dict format
         """
        response = requests.get(
            url=f"https://api.sheety.co/{SHEETY_KEY}/flightDeals/prices"
        ).json()
        self.destination_data = response['prices']
        return self.destination_data
