import unittest
import server.flaskapp

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = server.flaskapp.create_app().test_client()

    def test_get_index(self):
        rv = self.app.get('/')
        assert b'Hello, World!' in rv.data

    def test_get_price(self):
        rv = self.app.get('/price')

    def test_get_balance(self):
        rv = self.app.get('/balance')

    def test_post_buy(self):
        rv = self.app.post('/buy')

    def test_post_sell(self):
        rv = self.app.post('/sell')
