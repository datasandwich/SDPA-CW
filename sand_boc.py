# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#user_input = input("Please enter a name: ")

class RentalShop:
    def __init__(self):
        self.stock = {"Hb":{'quantity':4,'price':30},
                      'Sed':{'quantity':3,'price':50},
                      'SUV':{'quantity':3,'price':100}}    

    def display_inventory_and_prices(self):
        return self.stock
    
    def process_rent_request(self,car_type,days):
        self.stock[car_type]['quantity'] -=1
        print('You have rented {} for {} days'.format(car_type,days))
        print(self.stock)
        
    def process_return_request(self,car_type,days):
        print(days)
        self.stock[car_type]['quantity'] +=1
        rate = self.stock[car_type]['price']
        charge = rate * int(days)
        print('Bill:',
              '\nType: ',car_type,
              '\nPeriod: ',days,
              '\nRate: ',rate,
              '\nCharge: ',charge)
        print(self.stock)
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.shop = RentalShop()
        
    def inquire(self):
        print(self.shop.display_inventory_and_prices())
    
    def rent_car(self):
        car_type=input('car type')
        days=input('days')
        self.shop.process_rent_request(car_type,days)
        
    def return_car(self):
        car_type=input('car type')
        days=input('days')
        self.shop.process_return_request(car_type,days)

        
        
""""Here I'd like to use the input to create some sort of class instance name, and also declare the instance's name"""
my_object =Customer(name='dave')

print(my_object)
print(my_object.inquire())
print(my_object.rent_car())
print(my_object.return_car())


    