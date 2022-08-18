import requests
SHEETY_PRICES_ENDPOINT='https://api.sheety.co/6f932cb935bb5af9b4509e5d84644f2e/copyOfFlightDeals/prices'


class DataManager:

    def shetty_body(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        # return data
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
                json=new_data
            )
            print(response.text)
