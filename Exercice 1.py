import csv

import json

"""
data = [
    [2,3],
    [3,2],
    [1.0,-5.3],
    [0.7, 13]
]

with open('data.json', 'w') as json_file:
    json.dump(data, json_file,)
"""



with open("data.json", 'r') as jf:
    donnee = json.load(jf)

with open('data.csv', mode='w') as cf:

    donneW = csv.writer(cf, delimiter=',')

    donneW.writerow(['reel', 'imaginaire'])




