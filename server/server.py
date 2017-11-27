from flask import Flask, jsonify, Blueprint
import exchange
app = Flask('Fake Exchange Server')
exchange = exchange.Exchange()



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


@app.route('/buy')
def buy():
    status = exchange.buy_bit_coin()
    return "{}".format(status)


@app.route('/sell')
def sell():
    status = exchange.sell_bit_coin()
    return "{}".format(status)


app.run(debug=True)
