# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:23:50 2019

@author: james
"""

import pandas as pd
df = pd.read_csv('Yelp_Reviews.csv')
df.head(2)

ex=df.date[1]