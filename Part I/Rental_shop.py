#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:15 2020

@author: datasandwich
"""

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