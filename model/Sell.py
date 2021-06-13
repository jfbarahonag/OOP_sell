from .Client import Client
from .Product import Product

import numpy as np

from functools import reduce

class Sell:
    def __init__(self, client:Client, products:list) -> None:
        self.client_ = client
        self.products_ = np.array(products, dtype=Product)
        self.IVA_ = 0
        self.subtotal_ = float(0)
        self.total_ = float(0)

    def bill(self):
        
        prices = list(map(lambda product: product.get_price(), self.products_))
        self.subtotal_ = reduce(lambda x,y: x+y, prices)
        self.IVA_ = round(0.19 * self.subtotal_, 2)
        self.total_ = self.subtotal_ +self.IVA_
        
        output = ''
        output += '-------------------------------------------------\n'
        output += f'Client [{self.client_.get_name()}]\n'
        output += f'C.C. [{self.client_.get_cc()}]\n'
        output += '-------------------------------------------------\n'
        output += f'Code\tName\tPrice\n'
        for product in self.products_:
            output += f'{product.get_code()}\t{product.get_name()}\t{product.get_price()}\n'
        output += '-------------------------------------------------\n'
        output += f'Subtotal = {self.subtotal_}\n'
        output += f'IVA = {self.IVA_}\n'
        output += f'Total = {self.total_}\n'
        output += '-------------------------------------------------\n'

        return output