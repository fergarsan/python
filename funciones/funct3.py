# -*- coding: utf-8 -*-

def custom_welcome_to_space(name,space_ship):
    print(f'welcome, {name} and your space ship is {space_ship}.')
    
space_ships = ['spaceships 1', 'spaceships 2', 'spaceships 3', 'spaceships 4', 'spaceships 5']
names = ['neil armstrong', 'buzz aldrin', 'sally ride', 'yuri gagarin', 'elon musk']

for name in names:
    custom_welcome_to_space(name, space_ships)
