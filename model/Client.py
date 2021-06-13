class Client:
    def __init__(self, name:str, cc:str) -> None:
        self.name_ = name
        self.cc_ = cc
    
    def get_name(self):
        return self.name_
    
    def get_cc(self):
        return self.cc_