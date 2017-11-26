import yaml

config = yaml.safe_load(open("config.yml"))

class Account:
    COL_BALANCE_BITCOINS=1
    COL_BALANCE_FIAT=2
    COL_PASSWORD=3

    def __init__(self, db, accountId=None):
        self.db = db
        self.accountId = accountId
        self.balanceBitcoins = 0.0
        self.balanceFiat = 0.0
        self.password = ''
        self.fetch()

    def fetch(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT id, balance_bitcoins, balance_fiat, password FROM accounts WHERE id = %s", [self.accountId])
        row = cursor.fetchone()
        if row:
            self.__copyRowToVariables(row)
        return row

    def exists(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT id, balance_bitcoins, balance_fiat, password FROM accounts WHERE id = %s", [self.accountId])
        return None != cursor.fetchone()

    def create(self):
        if not self.exists():
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO accounts (balance_bitcoins, balance_fiat, password) VALUES (%s, %s, %s) RETURNING id", [self.balanceBitcoins, self.balanceFiat, self.password])
            self.accountId = cursor.fetchone()[0]

    def update(self):
        if self.exists():
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE accounts SET balance_bitcoins = %s, balance_fiat = %s, password = %s WHERE id = %s", [self.balanceBitcoins, self.balanceFiat, self.password, self.accountId])

    def __copyRowToVariables(self, row):
        self.balanceBitcoins = row[self.COL_BALANCE_BITCOINS]
        self.balanceFiat = row[self.COL_BALANCE_FIAT]
        self.password = row[self.COL_PASSWORD]
