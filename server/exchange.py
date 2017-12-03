import json
import urllib.request
from database.database import Database

class Exchange:
    cash = 100000
    bit_coin = 0
    bit_coin_current_price = None
    transaction_fee = 0.002

    def __init__(self):
        self.db = Database()
        self.bit_coin_current_price = self.get_last_sell_price()

    def get_last_sell_price(self):
        with urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') as response:
            html = response.read()
            self.bit_coin_current_price = float(json.loads(html)['last_price'])
        return self.bit_coin_current_price

    def buy_bit_coin(self, bitcoinamount):
        if self.cash > (self.bit_coin_current_price * bitcoinamount + self.calculate_transaction_fee(bitcoinamount)):
            self.bit_coin = self.bit_coin + bitcoinamount
            self.cash -= self.bit_coin_current_price*bitcoinamount
            self.cash -= self.calculate_transaction_fee(bitcoinamount)
            return 'You bought the following amount of bitcoin: %s for %s €' %(str(bitcoinamount), str(self.bit_coin_current_price*bitcoinamount))
        else:
            return "Can't spend money you don't have, friend"

    def sell_bit_coin(self, bitcoinamount):
        if self.bit_coin >= bitcoinamount:
            self.bit_coin = self.bit_coin - bitcoinamount
            self.cash += self.bit_coin_current_price * bitcoinamount
            self.cash -= self.calculate_transaction_fee(bitcoinamount)
            return 'You sold the following amount of bitcoin: %s for %s €' %(str(bitcoinamount), str(self.bit_coin_current_price*bitcoinamount))
        else:
            return 'Fancy having that many coins...'

    def get_balance(self, account_id):
        return self.cash + (self.bit_coin * self.bit_coin_current_price)

    def calculate_transaction_fee(self,bitcoinamount):
        return self.transaction_fee * self.bit_coin_current_price*bitcoinamount
