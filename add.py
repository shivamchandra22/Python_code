# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:08:36 2021

@author: Shivam
"""

def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1
print(add_nums(2, 10))