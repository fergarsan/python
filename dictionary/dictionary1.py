#!/usr/bin/env python
 
astronaut = {"name" : "Shiba Inu", "Suit size" : "medium", "allergies" : "chocolate"}
ne = astronaut ["name"]
ja = astronaut.keys()
print (ne)
print(ja)
l = list(astronaut.values())[1:]
print(l)
astronaut["allegies"] = "cotton"
print(astronaut)
del astronaut["allegies"]
print(astronaut)