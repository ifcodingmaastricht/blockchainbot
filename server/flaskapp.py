from flask import Flask, jsonify, Blueprint
from .exchange import Exchange


def create_app():

    app = Flask('Fake Exchange Server')
    exchange = Exchange()

    @app.route('/')
    def get_index():
        return 'Hello, World!'

    @app.route('/price')
    def get_price():
        price = exchange.get_last_sell_price()
        return "{}".format(price)


    @app.route('/balance')
    def get_balance():
        account_id = 1
        price = exchange.get_balance(account_id)
        return jsonify(
            total=price,
            cash=exchange.cash,
            bitcoin=exchange.bit_coin
        )


    @app.route('/buy/<float:bitcoinamount>')
    def buy(bitcoinamount):
        status = exchange.buy_bit_coin(bitcoinamount)
        return "{}".format(status)


    @app.route('/sell/<float:bitcoinamount>')
    def sell(bitcoinamount):
        status = exchange.sell_bit_coin(bitcoinamount)
        return "{}".format(status)


    return app
