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
                
                Menu.display_customer_menu(customer_name)
        print("Welcome back {}".format(customer_name))        
        Menu.customers[customer_name].return_car()
        print('{} logged out'.format(customer_name))
        Menu.login(Menu.customers)
        #Menu.display_returning_customer_menu(customer_name)
                
    def display_customer_menu(customer_name):
        print('\nNew customer: {}'.format(customer_name),
                          '\nInquire [1]'
                          '\nRent a car [2]'
                          )
        
            
        
        try: 
            user_input=int(input())
            if user_input<1 or user_input>2:
                print('Please enter either 1 or 2\n')
                Menu.display_customer_menu(customer_name)
        except: 
            ValueError
            print('Please enter an integer')
            Menu.display_customer_menu(customer_name) 
     
        if user_input==1:
            Customer.inquire()
            Menu.display_customer_menu(customer_name)
        elif user_input==2:
            while True:
                        car_type=input('car type?')
                        if car_type == "Hatchback" or car_type == "Sedan" or car_type == "SUV":
                            break
                        else: print("Please specify either Hatchback, Sedan or SUV")
            while True:
                try:
                    
                    days=int(input("days?")) 
                    if days<1:
                        print("Please enter a valid number of days")
                    
                    else:break
                except: 
                    ValueError 
                    print('Enter an integer\n')
           
            Menu.customers[customer_name]=Customer(customer_name,car_type,days)
         #login(customers)
            Menu.customers[customer_name].rent_car()
            
            print('\n{} logged out'.format(customer_name))
            Menu.login(Menu.customers)
    
     
'''
    def display_returning_customer_menu(customer_name):
        print('\nReturning customer: {}'.format(customer_name),
           #'\nInquire [1]'
           #'\nRent a car [2]'
           '\nReturn a car [1]')
        try: 
            user_input=int(input())
            if user_input+1:
                print('Please enter 1')
                Menu.display_returning_customer_menu(customer_name)
        except: 
            ValueError
            print('Please enter an integer')
            Menu.display_returning_customer_menu(customer_name)
       
        if user_input==1:
            Menu.customers[customer_name].inquire()
            Menu.display_returning_customer_menu(customer_name)
     
        if user_input==1:
            Menu.customers[customer_name].return_car()
            print('{} logged out'.format(customer_name))
            Menu.login(Menu.customers)
        else: 
            print('{} logged out'.format(customer_name))
            Menu.login(Menu.customers)
            '''