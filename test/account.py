from database.database import Database
from server.account import Account

db = Database()
db.connect()

account = Account(db)
print(account.fetch()) # prints None

account.create()
print(account.fetch()) # print [id, 0, 0, '']

print(account.accountId) # prints id

account.balanceBitcoins = 123.0
print("account.balanceBitcoins: {:f}".format(account.balanceBitcoins))
account.update()
print("account.balanceBitcoins: {:f}".format(account.balanceBitcoins))

account.fetch()

print(account.balanceBitcoins) # prints 123
