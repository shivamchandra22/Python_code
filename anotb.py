# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:19:42 2021

@author: Shivam
"""

import pandas as pd
df1 = pd.Series([2, 4, 8, 10, 12])
df2 = pd.Series([8, 12, 10, 15, 16])
df1=df1[~df1.isin(df2)]
print(df1)