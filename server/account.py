import yaml

config = yaml.safe_load(open("config.yml"))

class Account:
    def __init__(self, db, account_id=None):
        self.db = db

    def fetch():
        self.db.connection.cursor().execute("""SELECT id, balance_bitcoins, balance_fiat, password FROM accounts""")
        self.row = self.db.connection.cursor().fetchone()
