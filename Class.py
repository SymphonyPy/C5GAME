class Merchant(object):
    def __init__(self, address, name, price, amount):
        self.url = "https://www.c5game.com" + address
        self.name = name
        self.price = float(price)
        self.amount = int(amount)

    def print(self):
        print("name:" + self.name)
        print("price:" + str(self.price))
        print("amount:" + str(self.amount))
        print("url:" + self.url)
        print()
