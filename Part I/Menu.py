#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:22:21 2020

@author: datasandwich
"""
from Customer import Customer

class Menu():
    customers={}
    def login(customers):
        customer_name=input("Please enter your name: ")
        try: isinstance(customers[customer_name],Customer)
        except: 
                KeyError()
                
                Menu.display_new_customer_menu(customer_name)
                
        Menu.display_returning_customer_menu(customer_name)
                
    def display_new_customer_menu(customer_name):
        print('Current customer: {}'.format(customer_name),
                          '\nInquire [1]'
                          '\nRent a car [2]'
                          '\nReturn a car [3]')
     
        try:user_input=int(input()) 
        except: 
            ValueError 
            print('Enter an integer\n')
            Menu.display_new_customer_menu(customer_name)
        if user_input < 1 or user_input >3:
            print('Enter a value between 1 and 3\n')
            Menu.display_new_customer_menu(customer_name)
      
         
     
        if user_input==1:
            Customer.inquire()
            Menu.display_new_customer_menu(customer_name)
        elif user_input==2:
            while True:
                car_type=input('car type?')
                if car_type == "Hatchback" or car_type == "Sedan" or car_type == "SUV":break
                
                else: print("Please specify either Hatchback, Sedan or SUV")
            while True:
                try:
                    days=int(input("days?")) 
                    break
                except: 
                    ValueError 
                    print('Enter an integer\n')
            while True:
                if days<1:
                    print("Please enter a valid number of days")
                else: break
            Menu.customers[customer_name]=Customer(customer_name,car_type,days)
         #login(customers)
            Menu.customers[customer_name].rent_car()
            print('{} logged out'.format(customer_name))
            Menu.login(Menu.customers)
    
     

    def display_returning_customer_menu(customer_name):
        print('Current customer: {}'.format(customer_name),
           '\nInquire [1]'
           #'\nRent a car [2]'
           '\nReturn a car [3]')
        user_input=int(input())
        if user_input==1:
            Menu.customers[customer_name].inquire()
            Menu.display_returning_customer_menu(customer_name)
    
        elif user_input==3:
            Menu.customers[customer_name].return_car()
            print('{} logged out'.format(customer_name))
            Menu.login(Menu.customers)
        else: 
            print('Enter an integer between 1 and 3')
            Menu.display_returning_customer_menu(customer_name) 