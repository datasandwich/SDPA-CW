#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:04:31 2020

@author: datasandwich (Jarek Ettl, of20499)
@description: Unit test script for car rental program
"""
from unittest.mock import patch,Mock
import unittest
from Rental_shop import RentalShop
from Menu import Menu




class RentalShopTestCase(unittest.TestCase):
    
    def test_process_rent_and_return_request(self):
        car_type="SUV"
        days="7"
        self.shop1=RentalShop()
        self.shop1.process_rent_request(car_type, days)
        self.assertEqual(self.shop1.stock['SUV']['quantity'],2)
        self.shop1.process_return_request(car_type, days)
        self.assertEqual(self.shop1.stock['SUV']['quantity'],3)
    
class MenuTestCase(unittest.TestCase):
    
    def test_response_1(self):
        self.Menu=Menu()
        actual=self.Menu.response('3','dave')
        expected='Please enter either 1 or 2!\n'
        self.assertIn(expected,actual)
    def test_response_2(self):
        user_input="-3"
        customer_name='Dave'
        self.menu=Menu()
        actual=self.menu.response(user_input,customer_name)
        expected='Please enter either 1 or 2!\n'
        self.assertIn(expected,actual)
    def test_response_3(self):
        user_input="word"
        customer_name='Dave'
        self.menu=Menu()
        actual=self.menu.response(user_input,customer_name)
        expected='Please enter an integer!'
        self.assertIn(expected,actual)
        
    @patch('Menu.input',return_value='3')    
    def test_response_4(self,input):
        user_input="2"
        customer_name='Dave'
        self.menu=Menu()
        actual=self.menu.response(user_input,customer_name)
        expected="Please specify either Hatchback, Sedan or SUV!\n"
        self.assertIn(expected,actual)
        
    @patch('Menu.input',return_value='word')    
    def test_response_5(self,input):
        user_input="2"
        customer_name='Dave'
        self.menu=Menu()
        actual=self.menu.response(user_input,customer_name)
        expected="Please specify either Hatchback, Sedan or SUV!\n"
        self.assertIn(expected,actual)
        
    @patch('Menu.input',return_value='SUV')   
    @patch('Menu.input',return_value='0')   
    def test_response_6(self,input_1,input_2):
        user_input="2"
        customer_name='Dave'
        self.menu=Menu()
        actual=self.menu.response(user_input,customer_name)
        expected="Please enter a valid number of days!\n"
        self.assertIn(expected,actual)
        
    @patch('Menu.input',return_value='SUV')   
    @patch('Menu.input',return_value='word')   
    def test_response_7(self,input_1,input_2):
        user_input="2"
        customer_name='Dave'
        self.Menu=Menu()
        actual=self.Menu.response(user_input,customer_name)
        expected='Please enter an integer!\n'
        self.assertIn(expected,actual)
        
    
        
        


    
if __name__ == '__main__':
    unittest.main()
    


