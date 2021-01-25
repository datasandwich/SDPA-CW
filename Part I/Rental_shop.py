#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:15 2020

@author: datasandwich (Jarek Ettl, of20499)
@description: 
    This program defines the RentalShop class. 
    The RentalShop class can:
        Display available inventory and prices when a customer inquires;
        Process rent requests from customers after verifying stock availability;
        Issue a bill when the customer returns their car.
"""

class RentalShop:
    
    """Initialise class attributes"""
    
    stock = {'Hatchback':{'quantity':4,'price':{'week':30,'week+':25}},
             'Sedan':{'quantity':3,'price':{'week':50,'week+':40}},
             'SUV':{'quantity':3,'price':{'week':100,'week+':90}}} 
        
    def display_inventory():
        
        """Function summary
    
        Returns:
            Table consisting of car types and their current respective quantities
            
        """
        print("Stock list: \n\n")
        print("{} | {}".format('Car type','Quantity'))
        car_type=list(RentalShop.stock.keys())
        
        quantity=[RentalShop.stock['Hatchback']['quantity'],
                  RentalShop.stock['Sedan']['quantity'],
                  RentalShop.stock['SUV']['quantity']]
        
        for i in range(len(RentalShop.stock.items())):    
            print("{:<12}  {:<20}".format(car_type[i],quantity[i]))
        
    def display_inventory_and_prices():
        
        """Function summary
        
        Returns:
            Table consisting of car types,
            their current respective quantities,
            and prices depending on rental period.
            
        """
        
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
        
        """Function summary
        
        
        Parameters:
            car_type (str): Type of car specified by the customer
            days (int): Rental period specified by the customer, in days
            
        Returns:
            if specified car is not available:
                str: Informing customer to choose a different car type
            else:
                str: Informes the customer which car type they have rented, 
                     and for how many days
                str: Current inventory
            
        """
        
        if self.stock[car_type]['quantity']>0:
            self.stock[car_type]['quantity'] -=1
        else:return print("{} is currently not available. Please login again and select a different car.\n".format(car_type))
        
        return print('\nYou have rented a(n) {} for {} days\n'.format(car_type,days)), RentalShop.display_inventory()
        
    def process_return_request(self,car_type,days):
        
        """Function summary
        
        Parameters:
            car_type (str): Type of car specified by the customer
            days (int): Rental period specified by the customer, in days
            
        Returns:
            str: Customer bill
            str: Current inventory
        """
        
        days=int(days)
        self.stock[car_type]['quantity'] +=1
        if days<7:
            rate = self.stock[car_type]['price']['week']
        else:rate = self.stock[car_type]['price']['week+']
        charge = rate * days
        
        return print('Bill:',
              '\nType: ',car_type,
              '\nPeriod: ',days,
              '\nRate: ',rate,
              '\nCharge: ',charge,
              '\n'), RentalShop.display_inventory()