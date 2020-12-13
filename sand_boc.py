# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#user_input = input("Please enter a name: ")

class RentalShop:
    stock = {"Hb":{'quantity':4,'price':{'week':30,'week+':25}},
         'Sed':{'quantity':3,'price':{'week':50,'week+':40}},
         'SUV':{'quantity':3,'price':{'week':100,'week+':90}}} 
    #def __init__(self):
        

    def display_inventory_and_prices(self):
        return self.stock
    
    def process_rent_request(self,car_type,days):
        self.stock[car_type]['quantity'] -=1
        print('You have rented {} for {} days'.format(car_type,days))
        print(self.stock)
        
    def process_return_request(self,car_type,days):
        days=int(days)
        self.stock[car_type]['quantity'] +=1
        if days<7:
            rate = self.stock[car_type]['price']['week']
        else:rate = self.stock[car_type]['price']['week+']
        charge = rate * days
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
        self.car_type=input('car type')
        self.days=input('days')
        self.shop.process_rent_request(self.car_type,self.days)
        
    def return_car(self):
        self.shop.process_return_request(self.car_type,self.days)

        
        
""""Here I'd like to use the input to create some sort of class instance name, and also declare the instance's name"""
'''

def main_menu():
    
    user_input=input('enter name')

    customer_db[user_input]=customer

'''
my_object=Customer('dave')
my_other_object=Customer('john')
print(my_object)
print(my_object.inquire())
print(my_object.rent_car())
print(my_other_object.rent_car())
print(my_other_object.return_car())
print(my_object.return_car())
#print(my_object.return_car())

    