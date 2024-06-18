import requests
from datetime import datetime, timedelta
from sensitive_data import SensitiveData
class FlightSearch:

    def __init__(self):

        self.secret_data=SensitiveData()
        self.apikey = self.secret_data.tequila_apikey

    def search_flight(self, name_of_city, stopovers):
        tomorrow = datetime.now() + timedelta(days=1)
        max = datetime.now() + timedelta(days=6*30)
        headers = {"apikey": self.apikey}
        params = {"fly_from": "SOF",
                       "fly_to": name_of_city,
                       "date_from": str(tomorrow.day)+"/"+str(tomorrow.month)+"/"+str(tomorrow.year),
                       "date_to": str(max.day)+"/"+str(max.month)+"/"+str(max.year),
                       "nights_in_dst_from": 4,
                       "nights_in_dst_to": 7,
                       "flight_type": "round",
                       "one_for_city": 1,
                       "max_stopovers": stopovers,
                       "curr": "GBP"}

        search_url = "https://tequila-api.kiwi.com/v2/search"
        search_response = requests.get(url=search_url, headers=headers, params=params)
        search_response.raise_for_status()
        data = search_response.json()
        print(data)
        return data
