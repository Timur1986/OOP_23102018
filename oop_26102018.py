class CoffeeMachine:
    def __init__(self, coffee, sugar, milk):
        self.coffee = 100
        self.sugar = 100
        self.milk = 100
     
    def __subtract_coffee (self, coffee):
        self.coffee -= coffee
        
    def __subtract_sugar (self, sugar):
        self.sugar -= sugar
    
    def __subtract_milk (self, milk):
        self.milk -= milk
             
    def make_coffee (self, coffee, sugar, milk):
        if self.coffee >= coffee:
            self.__subtract_coffee(coffee)
            print('Coffee ready!')
        else:
            print ('Not enough coffee in the machine. Please, put in the box ' + str(coffee - self.coffee)+ ' gram')
        if self.sugar >= sugar:
            self.__subtract_sugar(sugar)
        else:
            print('Not enough sugar in the machine. Please, put in the box ' + str(sugar - self.sugar) + ' gram')
        if self.milk >= milk:
            self.__subtract_milk(milk)
        else:
            print('Not enough milk in the machine. Please, put in the box ' + str(milk - self.milk) + ' ml')

if __name__ == '__main__':
  
    coffee = int(input('Type the coffee gram: '))
    sugar = int(input('How much sugar gram: '))
    milk = int(input('Milk ml: '))

    coff_mash = CoffeeMachine (coffee, sugar, milk)
    coff_mash.make_coffee(coffee, sugar, milk)
    
