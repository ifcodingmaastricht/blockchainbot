
import json
import urllib.request
import time
from wallet import Wallet
from database import Database

db = Database()
db.connect()

walletBitcoin = 0.0
cash_wallet = Wallet()
firstrun = True
transection = 0.002

print ('Starting simulator...')

def getMidPrice():
    with urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') as response:
        html = response.read()
    return float(json.loads(html)['mid'])

def getSellPrice():
    with urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') as response:
        html = response.read()
    return float(json.loads(html)['last_price'])


oldPrice = currentPrice = initPrice = getSellPrice()

def getTransectionfee():
    return transection * currentPrice

def getTotalNetWorth():
    return cash_wallet.cash + (walletBitcoin * currentPrice)

def showTotalNetWorth():
    print ('Total bitcoin:', walletBitcoin, 'walletDollar', cash_wallet.cash)
    print ('Total networth:', getTotalNetWorth(), 'profit', getTotalNetWorth() - totalNetWorthStart )

totalNetWorthStart = getTotalNetWorth()



while True:
    var = urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') 
    html = var.read()
    bitfinexBtcusd = (json.loads(html))
    
    db.store(bitfinexBtcusd ['mid'], bitfinexBtcusd ['bid'],bitfinexBtcusd ['ask'], bitfinexBtcusd ['last_price'],
        bitfinexBtcusd ['low'], bitfinexBtcusd ['high'], bitfinexBtcusd ['volume'], bitfinexBtcusd ['timestamp'])

    currentPrice = getSellPrice()
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
 
    time.sleep(300)
