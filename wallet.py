class Wallet:
    cash = 100000

    def give(self, amount):
        self.cash -= amount

    def collect(self, amount):
        self.cash += amount
