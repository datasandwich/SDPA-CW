#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:05:02 2020

@author: datasandwich
"""
from Rental_shop import RentalShop



class Customer:
    def __init__(self, name, car_type, days):
        self.name = name
        self.shop = RentalShop()
        self.car_type = car_type
        self.days = days
        
    def inquire():
        RentalShop.display_inventory_and_prices()
    
    def rent_car(self):
        self.shop.process_rent_request(self.car_type,self.days)
        
    def return_car(self):
        self.shop.process_return_request(self.car_type,self.days)