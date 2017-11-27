import unittest

from database.database import Database

class TestDatabaseDatabase(unittest.TestCase):
    def test_init(self):
        db = Database()
        self.assertIsInstance(db, Database)

    def test_connect(self):
        db = Database()
        db.connect()
        self.assertIsNotNone(db.connection)
        self.assertIsNotNone(db.connection.cursor())

    def test_close(self):
        db = Database()
        db.connect()
        db.close()

    def test_getSampleData(self):
        db = Database()
        db.connect()
        self.assertIsNotNone(db.getSampleData())
