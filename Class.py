import re
import requests as rs


class Merchant(object):
    def __init__(self, address, name, price, amount):
        self.url = "https://www.c5game.com" + address
        self.name = name
        self.price = float(price)
        self.amount = int(amount)

    def Get_Details(self):
        html = rs.get(self.url).content
        pattern = re.compile('''<input type=.*? name=".*?" value="(\d+)">''')
        num = re.findall(pattern, str(html))[0]
        sec_url = "https://www.c5game.com/api/product/sale.html?id=" + num + "&quick=&gem_id=0&page=1"
        return rs.get(sec_url).json()["body"]["items"]

    def print(self):
        print("name:" + self.name)
        print("price:" + str(self.price))
        print("amount:" + str(self.amount))
        print("url:" + self.url)
        print()
