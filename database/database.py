import psycopg2
import config

class Database:
    cursor = None
    connection = None
    config = config.load()

    def connect(self):
        try:
            connection_string = "dbname='" + self.config['database']['database'] + "' "
            connection_string += "user='" + self.config['database']['username'] + "' "
            connection_string += "host='" + self.config['database']['host'] + "' "
            connection_string += "password='" + self.config['database']['password'] + "'"

            self.connection = psycopg2.connect(connection_string)
            self.connection.autocommit = True
        except Exception as e:
            print(e)

    def close(self):
        self.connection.close()

    def store(self, mid, bid, ask, last, low, high, volume, timestamp):
        self.connection.cursor().execute("""INSERT INTO """ + self.config['database']['schema'] + """.bitfinex VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""",
                            [mid, bid, ask, last, low, high, volume, timestamp])

    def getSampleData(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT last_price, timestamp FROM """ + self.config['database']['schema'] + """.bitfinex""")
        results = []
        for record in cursor:
            results.append([record[0], record[1]])
        return results
