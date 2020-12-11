#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:02 2020

@author: datasandwich
"""
from Rental_shop import RentalShop

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
