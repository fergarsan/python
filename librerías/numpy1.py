# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 02:48:55 2023

@author: vayam
"""

import numpy as np

x = np.arange(start=1, stop=11, step=1, dtype = np.int8)
n = [0,-1,2,3,4,5,-9,7,8,1]
n = np.array(n)

p = x + n
print(p)