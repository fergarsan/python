# -*- coding: utf-8 -*-

def space_suit_welcome(name, space_ship, color = "white", allergy=None):
    print(f'Welcome {name} to {space_ship}, your space suit color is {color}, Your allergy is {allergy}')
    
names = ["neil armstrong", "buzz aldrin", "asdfa", "yuri gagarin", "elon musk"]
    
space_ships = ["space ship 1", "space ship 2", "space ship 3", "space ship 4", "space_ship 5"]
for idx, name in enumerate(names):
    spaceship = space_ships[idx]
    if name == "elon musk":
        space_suit_welcome(name, spaceship, color = "orange")
    elif spaceship == "space ship 4":
        space_suit_welcome(name, spaceship, color = "blue")
    else:
        space_suit_welcome(name, spaceship)
