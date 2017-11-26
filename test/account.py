from database.database import Database
from server.account import Account

db = Database()
db.connect()

print("Initialize Account() without an id into variable `account`...")
account = Account(db)
print("account.exists(): {}".format(account.exists())) # prints None

print("Create a row for it in the database...")
account.create()
print("account.fetch(): {}".format(account.fetch())) # print [id, 0, 0, '']
print("account.accountId: {}".format(account.accountId)) # prints id

print("Try setting the balance to 123.0...")
account.balanceBitcoins = 123.0
print("account.balanceBitcoins: {:f}".format(account.balanceBitcoins))
print("Try updating the row in the database...")
account.update()
print("account.balanceBitcoins: {:f}".format(account.balanceBitcoins))

print("OK, now try fetching the row to see if we have the correct changes...")
account.fetch()

print("account.balanceBitcoins: {:f}".format(account.balanceBitcoins)) # prints 123.0
