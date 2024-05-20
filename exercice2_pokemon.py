import csv

# Ouverture du fichier CSV en mode lecture
with open("pokemon.csv", newline='') as pokemon_csv:
    # Création d'un objet lecteur CSV
    pokemon = csv.reader(pokemon_csv)
    stats = []
    nom = []
    #Remove the name from every line of the csv doc and return a list
    for ligne in pokemon:
        nom.append(ligne.pop(0))
        stats.append(list(map(int, ligne)))

#Dictionnaire
pkmn = {
    nom[0] : stats[0],
    nom[1] : stats[1],
    nom[2] : stats[2]
}
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")






