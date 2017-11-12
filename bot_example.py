import time
from exchange.fake import Exchange

print('Starting bot example...')
exchange = Exchange()
old_price = exchange.get_last_sell_price()
net_worth_start = exchange.get_balance()


def show_total_net_worth():
    print('#bitcoins: ', exchange.bit_coin, 'cash: ', exchange.cash)
    print('Profit: ', exchange.get_balance() - net_worth_start)


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
