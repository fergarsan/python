# -*- coding: utf-8 -*-

import requests

iss_url = 'https://api.wheretheiss.at/v1/satellites/25544'

my_header = {'accept':'application/json'}
results = requests.get(iss_url, headers=my_header)

jsoniss_results = results.json()
print(jsoniss_results)

print(results)