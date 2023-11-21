# -*- coding: utf-8 -*-

list_newest = ["a","b","c","d","e"]
numeric_list = [22,33,44,55,66]

for i_1, i_2 in zip (numeric_list, list_newest):
    print(f"Mixed Pair -> {i_1}:{i_2}")

