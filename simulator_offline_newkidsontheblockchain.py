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


def sell():
    global walletBitcoin
    # print ("sell")
    walletBitcoin = walletBitcoin - 1
    cash_wallet.collect(currentPrice)
    cash_wallet.give(getTransectionfee())

def buy():
    global walletBitcoin
    # print ("buy")
    walletBitcoin = walletBitcoin + 1
    cash_wallet.give(currentPrice)
    cash_wallet.give(getTransectionfee())



# Remove first price datapoint because we don't need it anymore
dataset.pop(0)

results = []

smallestWindow = 2
biggestWindow = len(dataset)

for windowSize in range(smallestWindow,biggestWindow):
    window = []
    for i in range(0, windowSize):
        window.append(0.0)

    currentIteration = 0
    oldAverage = 0
    trend = 0

    lastTransactionPrice = initPrice

    print("Running test for window size")
    print(windowSize)

    totalBuys = 0
    totalSells = 0

    # Now iterate over all consequitive datapoints
    for currentPrice in dataset:
        window.append(currentPrice)
        window.pop(0)

        currentIteration = currentIteration + 1

        if currentIteration == windowSize:
            currentAverage = round(sum(window) / len(window), 2)
            oldAverage = currentAverage

        if currentIteration > windowSize:
            currentAverage = round(sum(window) / len(window), 2)

            didSomething = False

            oldTrend = trend

            if currentPrice > currentAverage:
                trend = 1
            elif currentPrice < currentAverage:
                trend = -1
            else:
                trend = 0

            # smartness
            if trend != oldTrend:
                if trend == 1:
                    if currentAverage < oldAverage:
                        if lastTransactionPrice < (currentPrice + currentPrice * transection):
                            if walletBitcoin > 0:
                                sell()
                                totalSells += 1
                                lastTransactionPrice = currentPrice
                                didSomething = True
                elif trend == -1:
                    if currentAverage > oldAverage:
                        if lastTransactionPrice > (currentPrice + currentPrice * transection):
                            buy()
                            totalBuys += 1
                            lastTransactionPrice = currentPrice
                            didSomething = True

            oldAverage = currentAverage

            # if not didSomething:
            #     print("did nothing")

    print("Total buys")
    print(totalBuys)

    print("Total sells")
    print(totalSells)

    showTotalNetWorth()

    results.append(getTotalNetWorth())

    continue

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

print(results)
print(results.index(max(results)))
