from database.database import Database
from server.account import Account

db = Database()
db.connect()

account = Account(db, 1)
