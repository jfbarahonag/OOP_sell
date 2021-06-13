class Product:
    def __init__(self, code:str, name:str, price:float) -> None:
        self.code_ = code
        self.name_ = name
        self.price_ = price

    def get_code(self):
        return self.code_

    def get_name(self):
        return self.name_

    def get_price(self):
        return self.price_