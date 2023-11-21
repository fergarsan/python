# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:14:22 2023

@author: vayam
"""

class Person():

    # the method that runs as soon as you create a class

    def __init__(self, name, age, color): #self, we are passing this instance of this class to this __init__() function

        # create some attributes for person class

        self.name = name

        self.age = age

        self.color = color

        

    # date of birth method

    def year_of_birth(self):

        return 2022-self.age

    

    # projected age

    def projected_age(self, years=5):

        return self.age+years

class Astronaut(Person):
    
    #define initialization method
    # it is essential to pass through parent class attribute
    def __init__(self, name, age, color, mission_length_in_months): 
        super().__init__(name, age, color) #inheritance of the parent class - use super.()
        self.mission_length_in_months = mission_length_in_months
        
    #method for caculating age on return
    def age_on_return(self):
        return self.projected_age(years=self.mission_length_in_months/12)
    
new_astronaut = Astronaut('shiba inu', 5, 'orange', 24)
print(new_astronaut.name)
print(new_astronaut.mission_length_in_months)
print(new_astronaut.year_of_birth())
print(new_astronaut.age_on_return())