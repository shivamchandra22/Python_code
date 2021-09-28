# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import Counter
  
def find_dup_char(input):
  
    # now create dictionary using counter method
    # which will have strings as key and their 
    # frequencies as value
    WC = Counter(input)
    j = -1
    new_dict = {}

    # Finding no. of  occurrence of a character
    # and get the index of it.
    for key, value in WC.items():
        j = j + 1
        if( value > 1 ):
            new_dict[key] = value
    print(new_dict)
# Driver program
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)