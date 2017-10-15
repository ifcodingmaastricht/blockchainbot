
import json
import urllib.request
import time

walletBitcoin = 0.0
walletDollar = 100000.0
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
    return walletDollar + (walletBitcoin * currentPrice)

def showTotalNetWorth():
    print ('Total bitcoin:', walletBitcoin, 'walletDollar', walletDollar)
    print ('Total networth:', getTotalNetWorth(), 'profit', getTotalNetWorth() - totalNetWorthStart )

totalNetWorthStart = getTotalNetWorth()

while True:
    currentPrice = getSellPrice()
    print ('old;',oldPrice,'currentPrice;',currentPrice)
    if currentPrice > oldPrice and walletBitcoin > 0:
        print ("sell")
        walletBitcoin = walletBitcoin - 1
        walletDollar = walletDollar + currentPrice - getTransectionfee()
    elif currentPrice < oldPrice and walletDollar >0:
        print ("buy")
        walletBitcoin = walletBitcoin + 1
        walletDollar = walletDollar - currentPrice - getTransectionfee()
    showTotalNetWorth()
    
    oldPrice = currentPrice
 
    time.sleep(3)
