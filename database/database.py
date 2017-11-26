import psycopg2
import yaml


class Database:
    cursor = None
    connection = None
    config = yaml.safe_load(open("config.yml"))

    def connect(self):
        try:
            connection_string = "dbname='" + self.config['database']['database'] + "' "
            connection_string += "user='" + self.config['database']['username'] + "' "
            connection_string += "host='" + self.config['database']['host'] + "' "
            connection_string += "password='" + self.config['database']['password'] + "'"

            self.connection = psycopg2.connect(connection_string)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def store(self, mid, bid, ask, last, low, high, volume, timestamp):
        self.cursor.execute("""INSERT INTO """ + self.config['database']['schema'] + """.bitfinex VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""",
                            [mid, bid, ask, last, low, high, volume, timestamp])

    def getSampleData(self):
        self.cursor.execute("""SELECT last_price, timestamp FROM """ + self.config['database']['schema'] + """.bitfinex""")
        results = []
        for record in self.cursor:
            results.append([record[0], record[1]])
        return results
