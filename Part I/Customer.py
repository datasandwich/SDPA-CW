#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:02 2020

@author: datasandwich (Jarek Ettl, of20499)
@description: 
    This program defines the Customer class. 
    The Customer class allows customers to:
        Inquire about available stock and prices;
        Rent a car;
        Return a car they have previously rented.
"""

from Rental_shop import RentalShop

class Customer:
    
    def __init__(self, name, car_type, days):
        
        """Initialise instance attributes"""
        
        self.name = name
        self.shop = RentalShop()
        self.car_type = car_type
        self.days = days
        
    def inquire():
        
        """Calls the display_inventory_and_prices function from the RentalShop class"""
        
        RentalShop.display_inventory_and_prices()
    
    def rent_car(self):
        
        """Calls the process_rent_request function from the RentalShop class"""
        
        self.shop.process_rent_request(self.car_type,self.days)
        
    def return_car(self):
        
        """Calls the process_return_request function from the RentalShop class"""
        
        self.shop.process_return_request(self.car_type,self.days)