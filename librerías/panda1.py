# -*- coding: utf-8 -*-
#discuss header
"""
Created on Sat Nov 18 02:48:55 2023

@author: vayam
"""

import pandas as pd

class Person():
   
        self.name = name
        self.age = age
        self.color = color

    def year_of_birth(self):
        return 2022-self.age

    def projected_age(self, years=5):
        return self.age+years
    
new_person = Person("Elon Musk", 38, "blue")
print(new_person.name)
print(new_person.color)
print(new_person.year_of_birth)
    
new_person.projected_age()
    