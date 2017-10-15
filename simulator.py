
import json
import urllib.request
import time


# function buy sell
# function get price 
# variable wallet
# variable old price

walletBitcoin = 100.0
walletDollar = 100000.0
firstrun = True
currentPrice = 0
print ('start')
def getMidPrice():
    with urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') as response:
        html = response.read()
    return float(json.loads(html)['mid'])
oldPrice = getMidPrice()

def getTotalNetWorth():
    return walletDollar + (walletBitcoin * currentPrice)

def showTotalNetWorth():
    print ('Total networth:', getTotalNetWorth(), 'profit', getTotalNetWorth() - totalNetWorthStart )

totalNetWorthStart = getTotalNetWorth()

while True:
    currentPrice = getMidPrice()
    print ('old;',oldPrice,'currentPrice;',currentPrice)
    if currentPrice > oldPrice:
        print ("sell")
        walletBitcoin = walletBitcoin - 1
        walletDollar = walletDollar + currentPrice
        
    elif currentPrice < oldPrice:
        print ("buy")
        walletBitcoin = walletBitcoin + 1
        walletDollar = walletDollar - currentPrice
    showTotalNetWorth()
    
    oldPrice = currentPrice
 
    time.sleep(3)
    
     


#test = json.loads(html)
#print (test['mid'], old_price)
