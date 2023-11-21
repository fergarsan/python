# -*- coding: utf-8 -*-


new_set = {1,2,3,4,5,6}
try:
    new_set[0]= 4
except Exception as e:
    print(f"Error message {e}")
    print("Something went wrong with your request")