import psycopg2
import yaml


class Database:
    cursor = None
    connection = None
    config = yaml.safe_load(open("config.yml"))

    def connect(self):
        try:
            connection_string = "dbname='cryptocurrencies' "
            connection_string += "user='" + self.config['database']['username'] + "' "
            connection_string += "host='localhost' "
            connection_string += "password='" + self.config['database']['password'] + "'"

            self.connection = psycopg2.connect(connection_string)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def store(self, mid, bid, ask, last, low, high, volume, timestamp):
        self.cursor.execute("""INSERT INTO bitcoin.bitfinex VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""",
                            [mid, bid, ask, last, low, high, volume, timestamp])

