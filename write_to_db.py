import json
import urllib.request
import time
import psycopg2

### READ OUT VALUES FROM THE INTERNET
var = urllib.request.urlopen('https://api.bitfinex.com/v1/pubticker/btcusd') 
html = var.read()
bitfinexBtcusd = (json.loads(html))

# SET functions 
def getTransactionfee():
    return transaction * currentPrice

def getTotalNetWorth():
    return walletDollar + (walletBitcoin * oldPrice)

def showTotalNetWorth():
    print ('Total bitcoin:', walletBitcoin, 'walletDollar', walletDollar)
    print ('Total networth:', getTotalNetWorth(), 'profit', getTotalNetWorth() - totalNetWorthStart )

### SET variables
walletBitcoin = 20.0
walletDollar = 100000.0
firstrun = True
transaction = 0.002
oldPrice = currentPrice = initPrice = float (bitfinexBtcusd['last_price'])
totalNetWorthStart = getTotalNetWorth()

## WRITE VALUES TO DATABASE
try:
    conn = psycopg2.connect("dbname='cryptocurrencies' user='postgres' host='localhost' password='postgres'")
    conn.autocommit = True
except:
    print ("I am unable to connect to the database.")
cur = conn.cursor()

## Simulator
print ('Starting simulator...')
while True:
    cur.execute("""INSERT INTO bitcoin.bitfinex VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""", 
        [bitfinexBtcusd ['mid'], bitfinexBtcusd ['bid'],bitfinexBtcusd ['ask'], bitfinexBtcusd ['last_price'],
        bitfinexBtcusd ['low'], bitfinexBtcusd ['high'], bitfinexBtcusd ['volume'], bitfinexBtcusd ['timestamp']])

    currentPrice = float(bitfinexBtcusd['last_price'])
    midPrice = float(bitfinexBtcusd['mid'])

    print ('old;',oldPrice,'currentPrice;',currentPrice)

    if currentPrice > (oldPrice*1.005) and walletBitcoin > 0:
        print ("sell")
        walletBitcoin = walletBitcoin - 1
        walletDollar = walletDollar + currentPrice - getTransactionfee()
    elif currentPrice < (oldPrice*0.995) and walletDollar >0:
        print ("buy")
        walletBitcoin = walletBitcoin + 1
        walletDollar = walletDollar - currentPrice - getTransactionfee()

    showTotalNetWorth()

    cur.execute("SELECT * FROM bitcoin.bitfinex")
    for record in cur:
        print (record)

    time.sleep(300)
