import unittest

from database.database import Database
from server.account import Account

class TestServerAccount(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.db.connect()

    def tearDown(self):
        self.db.close()

    def test_init(self):
        account = Account(self.db)
        self.assertIsInstance(account, Account)

        account2 = Account(self.db, 1)
        self.assertIsInstance(account, Account)

    def test_exists(self):
        account = Account(self.db, 123)
        account.destroy()
        self.assertFalse(account.exists())
        account.create()
        self.assertTrue(account.exists())

    def test_destroy(self):
        account = Account(self.db, 123)
        account.create()
        self.assertTrue(account.exists())
        account.destroy()
        self.assertFalse(account.exists())

    def test_create(self):
        account = Account(self.db)
        self.assertFalse(account.exists())
        accountId = account.create()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT id FROM accounts WHERE id = %s LIMIT 1", [accountId])
        self.assertIsNotNone(cursor.fetchone())

    def test_update(self):
        account = Account(self.db)
        accountId = account.create()
        self.assertTrue(account.balanceBitcoins == 0.0)
        account.balanceBitcoins = 543.0
        account.update()

        account2 = Account(self.db, accountId)
        self.assertTrue(account2.balanceBitcoins == 543.0)

    def test_create_update_fetch_init(self):
        account = Account(self.db)
        self.assertIsInstance(account.create(), int)
        account.balanceBitcoins = 123.0
        account.update()
        account.fetch()
        self.assertTrue(account.balanceBitcoins == 123.0)
        # create new instance and test it
        self.assertTrue(Account(self.db, account.accountId).balanceBitcoins == 123.0)
