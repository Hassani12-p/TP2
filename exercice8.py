def rechercher_occurrences(liste, nombre):
    occurrences = 0
    indices = []

    for index, element in enumerate(liste):
        if element == nombre:
            occurrences += 1
            indices.append(index)

    return occurrences, indices
liste = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

nombre_recherche = int(input("Entrez le nombre que vous souhaitez rechercher : "))

occurrences, indices = rechercher_occurrences(liste, nombre_recherche)

if occurrences > 0:
    print(f"Le nombre {nombre_recherche} a été trouvé {occurrences} fois aux indices : {indices}")
else:
    print(f"Le nombre {nombre_recherche} n'a pas été trouvé dans la liste.")
