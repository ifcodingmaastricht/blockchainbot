import yaml
import json
import urllib.request
import time
from wallet import Wallet
from database.database import Database

config = yaml.safe_load(open("config.yml"))

f = open('dataset.txt', 'r')
dataset = f.readlines()
dataset = [float(i) for i in dataset]

walletBitcoin = 0.0
cash_wallet = Wallet()
firstrun = True
transection = 0.002

print ('Starting simulator...')

def getSellPrice():
    with urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') as response:
        html = response.read()
    return float(json.loads(html)['last_price'])


oldPrice = currentPrice = initPrice = dataset[0]



def getTransectionfee():
    return transection * currentPrice

def getTotalNetWorth():
    return cash_wallet.cash + (walletBitcoin * currentPrice)

def showTotalNetWorth():
    print ('Total bitcoin:', walletBitcoin, 'walletDollar', cash_wallet.cash)
    print ('Total networth:', getTotalNetWorth(), 'profit', getTotalNetWorth() - totalNetWorthStart )

totalNetWorthStart = getTotalNetWorth()

dataset.pop(0)
recent_prices = []
last_buy = 0
steps = 40

def sell(prices):
    if prices[0] < prices[steps-2]:
        if prices[steps-1] < prices[steps-2]:
            return True
    return False

min_price = 100000
max_price = 0

# Now iterate over all consequitive datapoints
for currentPrice in dataset:
    print ('old;',oldPrice,'currentPrice;',currentPrice,'min',min_price,'max',max_price)
    recent_prices.append(currentPrice)

    min_price = min(min_price, currentPrice)
    max_price = max(max_price, currentPrice)


    # nets 11281.58
    #
    if len(recent_prices) > steps-1:
        if sell(recent_prices) and walletBitcoin > 0:
            print ("sell")
            if last_buy + getTransectionfee() > currentPrice:
                walletBitcoin = walletBitcoin - 1
                cash_wallet.collect(currentPrice)
                cash_wallet.give(getTransectionfee())
        elif cash_wallet.cash > 0:
            print ("buy")
            walletBitcoin = walletBitcoin + 1
            cash_wallet.give(currentPrice)
            cash_wallet.give(getTransectionfee())
            last_buy = currentPrice

    # nets 134388.25
    #
    # if currentPrice == 5375.8:
    #     # buy
    #     number_we_afford = cash_wallet.cash / currentPrice
    #     walletBitcoin = walletBitcoin + number_we_afford
    #     cash_wallet.give(currentPrice * number_we_afford)
    #     cash_wallet.give(getTransectionfee())
    #     last_buy = currentPrice
    # elif currentPrice == 6310.0:
    #     # sell at max
    #     cash_wallet.collect(currentPrice * walletBitcoin)
    #     cash_wallet.give(getTransectionfee())

    showTotalNetWorth()
    if len(recent_prices) > steps:
            recent_prices.pop(0)
    oldPrice = currentPrice
