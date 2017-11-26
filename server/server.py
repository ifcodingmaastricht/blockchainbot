from flask import Flask, jsonify
from exchange import Exchange
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


app = Flask('Fake Exchange Server')
exchange = Exchange()


@app.route('/price')
def get_price():
    price = exchange.get_last_sell_price()
    return "{}".format(price)


@app.route('/balance')
def get_balance():
    price = exchange.get_balance()
    return jsonify(
        total=price,
        cash=exchange.cash,
        bitcoin=exchange.bit_coin
    )


@app.route('/buy/<float:bitcoinamount>')
def buy(bitcoinamount):
    status = exchange.buy_bit_coin(bitcoinamount)
    return "{}".format(status)


@app.route('/sell')
def sell():
    status = exchange.sell_bit_coin()
    return "{}".format(status)


app.run(debug=True)
