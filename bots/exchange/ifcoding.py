import json
import urllib.request


class Exchange:
    server_url = 'http://localhost:5000'

    def get_last_sell_price(self):
        with urllib.request.urlopen(self.server_url + '/price') as response:
            price = response.read()
        return float(price)

    def buy_bit_coin(self):
        with urllib.request.urlopen(self.server_url + '/buy') as response:
            status = response.read()
        return status

    def sell_bit_coin(self):
        with urllib.request.urlopen(self.server_url + '/sell') as response:
            status = response.read()
        return status

    def get_balance(self):
        with urllib.request.urlopen(self.server_url + '/balance') as response:
            data = json.loads(response.read())
        return data

