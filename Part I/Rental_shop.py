#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:15 2020

@author: datasandwich
"""

class RentalShop:
    stock = {"Hatchback":{'quantity':4,'price':{'week':30,'week+':25}},
         'Sedan':{'quantity':3,'price':{'week':50,'week+':40}},
         'SUV':{'quantity':3,'price':{'week':100,'week+':90}}} 
    #def __init__(self):
        
    def display_inventory():
        print("Stock list: \n\n")
        print("{} | {}".format('Car type','Quantity'))
        car_type=list(RentalShop.stock.keys())
        quantity=[RentalShop.stock['Hatchback']['quantity'],
                  RentalShop.stock['Sedan']['quantity'],
                  RentalShop.stock['SUV']['quantity']]
        for i in range(len(RentalShop.stock.items())):    
            print("{:<12}  {:<20}".format(car_type[i],quantity[i]))
        
    def display_inventory_and_prices():
        
        print("{} | {} | {} | {}".format('Car type','Quantity','Daily rate for less than 7 days (£)','Daily rate for more than 7 days (£)'))
        car_type=list(RentalShop.stock.keys())
        quantity=[RentalShop.stock['Hatchback']['quantity'],
                  RentalShop.stock['Sedan']['quantity'],
                  RentalShop.stock['SUV']['quantity']]
        price_week=[RentalShop.stock['Hatchback']['price']['week'],
                    RentalShop.stock['Sedan']['price']['week'],
                    RentalShop.stock['SUV']['price']['week']]
        price_week_plus=[RentalShop.stock['Hatchback']['price']['week+'],
                    RentalShop.stock['Sedan']['price']['week+'],
                    RentalShop.stock['SUV']['price']['week+']]
    
        for i in range(len(RentalShop.stock.items())):    
            print("{:<12}  {:<20}  {:<30}  {}".format(car_type[i],quantity[i],price_week[i],price_week_plus[i]))
        
    
    def process_rent_request(self,car_type,days):
        if self.stock[car_type]['quantity']>0:
            self.stock[car_type]['quantity'] -=1
        else:return print("{} is currently not available. Please login again and select a different car.\n".format(car_type))
        print('\nYou have rented a(n) {} for {} days\n'.format(car_type,days))
        return print(RentalShop.display_inventory())
        
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
              '\nCharge: ',charge,
              '\n')
        return RentalShop.display_inventory()