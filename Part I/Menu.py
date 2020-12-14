#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:22:21 2020

@author: datasandwich (Jarek Ettl, of20499)
@description: 
    This program defines the Menu class. 
    The Menu class can:
        Login customers
        Display an interactive menu
        
"""
from Customer import Customer

class Menu():
    
    """Initialise class attributes"""
    
    customers={}
    
    def login():
        
        """Function summary
        
        The login function creates accounts for new customers and subsequently displays the menu.
        For the existing customers, it processes the return of their rental car.
        
        Returns:
            if the customer is new:
                str: Message informing that an account has been created for them
                str: The customers username
            else:
                str: Welcoming back the existing customer
                str: Message informing the customer that they have been logged out of the system
                
            
        """
        
        customer_name=input("Welcome to My Car Rental. Please enter your name to login: \n")
           
        try: isinstance(Menu.customers[customer_name],Customer)
        except: 
                KeyError()
                print('\nNew customer account created.',
                      '\nUsername: {}\n'.format(customer_name))
                Menu.display_customer_menu(customer_name)
        print("Welcome back {}.\n".format(customer_name),
              'You have successfully returned your car!. Please view your bill below:\n\n')        
        Menu.customers[customer_name].return_car()
        print('You have been logged out of your account.')
        Menu.login(Menu.customers)
        
                
    def display_customer_menu(customer_name):
        
        """Function summary
        
        The display_customer_menu function presents the customer with an interactive menu.
        
        Parameters:
            customer_name(str): The name of the customer currently logged into the system
            
        Returns:
            str: Message informing the customer that they have been logged out of the system
        """
        
        print(
              '\nPlease select an option from the menu below.',
              '\n[1] Inquire '
              '\n[2] Rent a car ')
        try: 
            user_input=int(input())
            if user_input<1 or user_input>2:
                print('Please enter either 1 or 2!\n')
                Menu.display_customer_menu(customer_name)
        except: 
            ValueError
            print('Please enter an integer!\n')
            Menu.display_customer_menu(customer_name) 
     
        if user_input==1:
            Customer.inquire()
            Menu.display_customer_menu(customer_name)
        elif user_input==2:
            while True:
                        car_type=input('Which car would you like to rent?\n')
                        if car_type == "Hatchback" or car_type == "Sedan" or car_type == "SUV":
                            break
                        else: print("Please specify either Hatchback, Sedan or SUV!\n")
            while True:
                try:
                    
                    days=int(input("How many days would you like to rent the car for?\n")) 
                    if days<1:
                        print("Please enter a valid number of days!\n")
                    
                    else:break
                except: 
                    ValueError 
                    print('Please enter an integer!\n')
           
            Menu.customers[customer_name]=Customer(customer_name,car_type,days)
            Menu.customers[customer_name].rent_car()
            print('\nYou have been logged out of your account.\n')
            Menu.login(Menu.customers)
    
