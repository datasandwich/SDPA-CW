#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:15 2020

@author: datasandwich
"""

class RentalShop:
    stock = {"Hb":{'quantity':4,'price':{'week':30,'week+':25}},
         'Sed':{'quantity':3,'price':{'week':50,'week+':40}},
         'SUV':{'quantity':3,'price':{'week':100,'week+':90}}} 
    #def __init__(self):
        

    def display_inventory_and_prices(self):
        print('Stock list: ')
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