# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:36:24 2021

@author: Shivam
"""

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(Counter(d1))
print(new_dict)