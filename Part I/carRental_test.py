#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:04:31 2020

@author: datasandwich (Jarek Ettl, of20499)
@description: Unit test script for car rental program
"""
from unittest.mock import patch
import unittest
from Rental_shop import RentalShop
from Menu_for_testing import Menu

"""
A copy of Menu.py has been used for unit testing as the perpetual looping 
of the menu made it difficult to assess the relevant responses of the Menu class.

The test class below demonstrates this:

       
from Menu import Menu as menu_loop

class LoopingMenuTestCase(unittest.TestCase):
  
    @patch('builtins.input', side_effect=['3','Hatchback','7'])    
    def test_response_2(self,input):
        self.assertIn('1 or 2', menu_loop.display_customer_menu('Dave'))
        
    
Menu_for_testing returns the string message associateed with acceptable or unacctable 
inputs, without calling the display_customer_menu function, thus avoiding looping.
"""

class RentalShopTestCase(unittest.TestCase):
    """ Tests the renting and return functionalities """
   
    def test_process_rent_and_return_request(self):
        
        self.shop1=RentalShop()
        self.shop1.process_rent_request('SUV', 7)
        self.assertEqual(self.shop1.stock['SUV']['quantity'],2)
        self.shop1.process_return_request('SUV', 7)
        self.assertEqual(self.shop1.stock['SUV']['quantity'],3)
    
class MenuTestCase(unittest.TestCase):
    """ Tests the response of the Menu class to different inputs"""
    
    @patch('builtins.input', side_effect=['3','Hatchback','7'])    
    def test_response_2(self,input):
        self.assertIn('1 or 2', Menu.display_customer_menu('Dave'))
    @patch('builtins.input', side_effect=['-3','Hatchback','7'])    
    def test_response_3(self,input):
        self.assertIn('1 or 2', Menu.display_customer_menu('Dave'))
    @patch('builtins.input', side_effect=['word','Hatchback','7'])    
    def test_response_4(self,input):
        self.assertIn('integer', Menu.display_customer_menu('Dave')) 
    @patch('builtins.input', side_effect=['1','Hatchback','7'])    
    def test_response_5(self,input):
        self.assertEqual('Customer.inquire()', Menu.display_customer_menu('Dave')) 
    @patch('builtins.input', side_effect=['2','3','7'])    
    def test_response_6(self,input):
        self.assertIn('specify', Menu.display_customer_menu('Dave')) 
    @patch('builtins.input', side_effect=['2','Hatchsnack','7'])    
    def test_response_7(self,input):
        self.assertIn('specify', Menu.display_customer_menu('Dave')) 
    @patch('builtins.input', side_effect=['2','Hatchback','0'])    
    def test_response_8(self,input):
        self.assertIn('valid', Menu.display_customer_menu('Dave'))
    @patch('builtins.input', side_effect=['2','Hatchback','7.5'])    
    def test_response_9(self,input):
        self.assertIn('integer', Menu.display_customer_menu('Dave'))
    @patch('builtins.input', side_effect=['2','Hatchback','7'])    
    def test_response_1(self,input):
        self.assertIn('logged out', Menu.display_customer_menu('Dave'))


if __name__ == '__main__':
    unittest.main()    