# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:20:15 2021

@author: Abdullah
"""

# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("hepatitis.csv", na_values = missing_values)

# Take a look at the first few rows
 #housing_map = {'yes': 1, 'no': 0}
 #df['NUM_BEDROOMS'] = df['NUM_BEDROOMS'].map(housing_map)



 #median = df['ST_NAME'].median()
 # df['ST_NAME'].fillna(median, inplace=True)

print( df.head())
