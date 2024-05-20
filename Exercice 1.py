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


print("Fichier data.json")
with open("data.json", 'r') as jf:
    donneeL = json.load(jf)

    for ligne in donneeL:
        print(ligne)


with open('data.csv', mode='w', newline='') as cf:
    donneW = csv.writer(cf, delimiter=',')

    donneW.writerow(['reel', 'imaginaire'])
    for row in donneeL:
        donneW.writerow(row)


print(f"\n############################\n")
print("Fichier data.csv")

with open('data.csv', mode='r') as cL:
    donneecsv= csv.reader(cL, delimiter=',')

    for row in donneecsv:
        print(row)
