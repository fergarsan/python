# -*- coding: utf-8 -*-

def space_suit_welcome(name, space_ship, color = "white", allergy=None):
    print(f'Welcome {name} to {space_ship}, your space suit color is {color}, Your allergy is {allergy}')
    
names = ["neil armstrong", "buzz aldrin", "asdfa", "yuri gagarin", "elon musk"]
    
space_ships = ["space ship 1", "space ship 2", "space ship 3", "space ship 4", "space_ship 5"]

welcome_elon_musk_sentence = space_suit_welcome("elon musk", "flying pan")
print(welcome_elon_musk_sentence)
