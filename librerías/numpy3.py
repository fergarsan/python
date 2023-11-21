# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 02:48:55 2023

@author: vayam
"""

import pandas as pd

series_1 = pd.Series([100,300,120,400,600])
series_1.index = ["Law", "Pharmacy", "Architecture", "Business","Engineering"]
print(series_1)
print(series_1 > 110)

series_2 = series_1[series_1>110]
print(series_2)
