#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:03:19 2020

@author: datasandwich
"""

from Customer import Customer


customers={}
def login(customers):
    customer_name=input("Please enter your name: ")
    try: isinstance(customers[customer_name],Customer)
    except: 
            KeyError()
            car_type=input('car type?')
            days=input('days?')
            customers[customer_name]=Customer(customer_name,car_type,days) 
    
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
         
         #login(customers)
         customers[customer_name].rent_car()
         print('{} logged out'.format(customer_name))
         login(customers)
     elif user_input==3:
         customers[customer_name].return_car()
         print('{} logged out'.format(customer_name))
         login(customers)
     else: 
         print('Enter 1, 2 or 3')
         display_menu(customer_name)
            

login(customers)

'''
Errors
Customers can rent more than one vehicle
Requests to hire a car for an invalid time-period, such as a negative number of days.
Rent a car with unlisted type/empty type.

'''


