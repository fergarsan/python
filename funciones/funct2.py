# -*- coding: utf-8 -*-

def custom_welcome(name, space_ship):
    print(f'welcome {name} and your travel space ship is {space_ship}')
    
names = ['neil armstrong', 'buzz aldrin', 'sally ride', 'yuri gagarin', 'elon musk']
space_ship = 'travelverse spaceship'
for name in names:
    custom_welcome(name.title(), space_ship)
    