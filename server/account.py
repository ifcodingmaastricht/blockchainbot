import config

config = config.load()

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
        cursor.execute("SELECT id, balance_bitcoins, balance_fiat, password FROM bitcoin.accounts WHERE id = %s", [self.accountId])
        row = cursor.fetchone()
        if row:
            self.__copyRowToVariables(row)
        return row

    def exists(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT id, balance_bitcoins, balance_fiat, password FROM bitcoin.accounts WHERE id = %s", [self.accountId])
        return None != cursor.fetchone()

    def create(self):
        if not self.exists():
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO bitcoin.accounts (balance_bitcoins, balance_fiat, password) VALUES (%s, %s, %s) RETURNING id", [self.balanceBitcoins, self.balanceFiat, self.password])
            self.accountId = cursor.fetchone()[0]
            return self.accountId

    def update(self):
        if self.exists():
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE bitcoin.accounts SET balance_bitcoins = %s, balance_fiat = %s, password = %s WHERE id = %s", [self.balanceBitcoins, self.balanceFiat, self.password, self.accountId])

    def destroy(self):
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM bitcoin.accounts WHERE id = %s", [self.accountId])

    def __copyRowToVariables(self, row):
        self.balanceBitcoins = float(row[self.COL_BALANCE_BITCOINS])
        self.balanceFiat = float(row[self.COL_BALANCE_FIAT])
        self.password = row[self.COL_PASSWORD]
