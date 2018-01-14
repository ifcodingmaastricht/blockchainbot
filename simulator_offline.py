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




# Remove first price datapoint because we don't need it anymore
dataset.pop(0)

# Now iterate over all consequitive datapoints
for currentPrice in dataset:
    print ('old;',oldPrice,'currentPrice;',currentPrice)
    if currentPrice > oldPrice and walletBitcoin > 0:
        print ("sell")
        walletBitcoin = walletBitcoin - 1
        cash_wallet.collect(currentPrice)
        cash_wallet.give(getTransectionfee())
    elif currentPrice < oldPrice and cash_wallet.cash > 0:
        print ("buy")
        walletBitcoin = walletBitcoin + 1
        cash_wallet.give(currentPrice)
        cash_wallet.give(getTransectionfee())
    showTotalNetWorth()

    oldPrice = currentPrice

    # Don't sleep anymore because we don't pull data from the internet
    # anymore in this version of the code.
    # time.sleep(config['simulator']['seconds_between_refresh'])
