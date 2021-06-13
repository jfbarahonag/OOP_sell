#from model import Client, Product, Sell
from model import *

c_1 = Client("Ana", "1012")
c_2 = Client("Maria", "2022")

products = {
    1 : Product("001", "Pants", 1230),
    2 : Product("002", "Shirt", 1200),
    3 : Product("003", "Shirt", 2000),
    4 : Product("004", "Shirt", 3500),
    5 : Product("005", "Shirt", 1450),
    6 : Product("006", "Shirt", 980),
}

sell_1 = Sell(c_1, [products[1], products[2], products[3], products[6]])
sell_2 = Sell(c_2, [products[3], products[4], products[5], products[1]])


print(sell_1.bill())
print(sell_2.bill())