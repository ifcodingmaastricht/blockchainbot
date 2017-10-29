import psycopg2

class Database:
    cursor = None
    connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect("dbname='cryptocurrencies' user='postgres' host='localhost' password='postgres'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Exception as e: print(e)

    def store(self, mid, bid, ask, last, low, high, volume, timestamp):
        self.cursor.execute("""INSERT INTO bitcoin.bitfinex VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""",
                    [mid, bid,ask, last,low, high, volume, timestamp])
    
