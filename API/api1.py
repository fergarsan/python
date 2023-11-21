# -*- coding: utf-8 -*-

import requests

joke_url = 'https://icanhazdadjoke.com/'

my_header = {'accept':'application/json'}
results = requests.get(joke_url, headers=my_header)

json_results = results.json()
print(json_results)
print(json_results["joke"])
print(results)
