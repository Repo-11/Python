
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('dylan1699', 'sheety_hello1699')

SHEETY_PRICES_ENDPOINT ="https://api.sheety.co/2658c77738c4c9f61f9f9e00fabef8f4/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,auth =("dylan1699","sheety_hello1699"))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=("dylan1699", "sheety_hello1699")
            )
            print(response.text)
