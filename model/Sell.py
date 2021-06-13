from .Client import Client
from .Product import Product

import numpy as np

from functools import reduce

class Sell:
    def __init__(self, client:Client, products:list) -> None:
        self.client_ = client
        self.products_ = np.array(products, dtype=Product)
        self.IVA = 0.19
        self.subtotal = 0
        self.total = 0
