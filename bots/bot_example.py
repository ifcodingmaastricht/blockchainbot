import time
import bots.exchange.ifcoding

print('Starting bot example...')
exchange = bots.exchange.ifcoding.Exchange()
old_price = exchange.get_last_sell_price()
net_worth_start = 100000


def show_total_net_worth():
    balance = exchange.get_balance()
    print('#bitcoins: ', balance['bitcoin'], 'cash: ', balance['cash'])
    print('Profit: ', balance['total'] - net_worth_start)


while True:
    current_price = exchange.get_last_sell_price()
    print('old: ', old_price, ' current price: ', current_price)
    if current_price > old_price:
        print("sell")
        exchange.sell_bit_coin()
    elif current_price < old_price:
        print("buy")
        exchange.buy_bit_coin()

    show_total_net_worth()
    old_price = current_price
    time.sleep(5)
