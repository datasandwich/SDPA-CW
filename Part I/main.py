#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:03:19 2020

@author: datasandwich
"""

#from Customer import Customer
#from Rental_shop import RentalShop
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
        
customers={}
def hm(customers):
    customer_name=input("Please enter your name: ")
    customers[customer_name]=Customer(customer_name)
    display_menu(customer_name)
       
def display_menu(customer_name):
     print('Current customer: {}'.format(customer_name),
           '\nInquire [1]'
           '\nRent a car [2]'
           '\nReturn a car [3]')
     user_input=int(input())
     if user_input==1:
         customers[customer_name].inquire()
         display_menu(customer_name)
     elif user_input==2:
         customers[customer_name].rent_car()
         print('{} logged out'.format(customer_name))
         hm(customers)
     elif user_input==3:
         customers[customer_name].return_car()
         print('{} logged out'.format(customer_name))
         hm(customers)
     else: 
         print('Enter 1, 2 or 3')
         display_menu(customer_name)
            
hm(customers)