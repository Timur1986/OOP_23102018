# Task_2
class student:
    def __init__ (self, name, lastname, department, year_of_entrance):
        self.name = ''
        self.lastname = ''
        self.department = ''
        self.year_of_entrance = ''
        
    def get_student_info (self, a, b, c, d):
        self.name = self.name + a
        self.lastname = self.lastname + b
        self.department = self.department + c
        self.year_of_entrance = self.year_of_entrance + d
        
ivanov = student('Вася', 'Иванов', 'на факультет: Программирование.', 'поступил в 2017 году')
ivanov.get_student_info('Вася', 'Иванов', 'поступил в 2017 году', 'на факультет: Программирование.')
print(ivanov.name, ivanov.lastname, ivanov.department, ivanov.year_of_entrance)
print()

# Task_3
class car:
    def __init__(self, make, model, year, odometer, fuel, road):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
        self.road = 900
        
    def drive (self):
        self.__add_distance(300)
        self.__subtract_fuel(30)
        
    def __add_distance (self, distance):
        self.odometer += distance
        if self.odometer < 700:
            print('Let\'s drive!!!')
        
    def __subtract_fuel (self, km):
        self.fuel -= km
        if self.fuel <= 0:
            print('Need more fuel, please, fill more!')

new_car = car('Honda', 'CR-V', 2008, 0, 70, 900)
print(f'{new_car.make} {new_car.model} {new_car.year} {new_car.odometer} {new_car.fuel} {new_car.road}')
print('And Go to the adventure!!!')
new_car.drive()
print(new_car.odometer, new_car.fuel)
new_car.drive()
print(new_car.odometer, new_car.fuel)
new_car.drive()
print(new_car.odometer, new_car.fuel)
print()

# Task_1
import random

print ('''Presenter:
Welcome to our show game!
Today, we are playing 'Guess the number'!
And the first member Jon Fucker.

Jon:
Hello my friend!

Presenter:
You should guess the number between 1 and 7 in our lotto. Annnnddd START!!!''')
print()

number = int(input('Jon, chose number:'))
res = random.randint (1, 7)
print('Lotto\'s number:')
print(res)

if number <= res:
    print('The entered number is less than the specified, try again!')
elif number >= res:
    print('The number you entered is greater than the specified, try again!')
elif number == res:
    print('You guess the number. Congratulations')
else:
    print('Stop game!')

