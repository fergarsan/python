#!/usr/bin/env python

list_variable = [1, "string", 123.45, 5, 4, 3, 3, 2, 2, 1]
set_variable = set(list_variable)

list_variable2 = list(set(list_variable))
tuple_variable = tuple(list_variable)

print(list_variable2)
print(set_variable)
print(tuple_variable)