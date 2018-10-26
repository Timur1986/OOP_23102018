class phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def get_phone_info (self):
        return f'The phone {self.brand} {self.model} and cost {self.price} KGS'
        
    
if __name__ == '__main__':       
       
    x1 = input ('Type your phone: ')
    x2 = input ('Enter the model phone: ')
    x3 = input ('And so, it price: ')
    
    ph = phone (x1, x2, x3)
    print(ph.get_phone_info())
