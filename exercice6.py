
liste = [1, 2, 3, 4, 2, 5, 2, 6]
nombre_a_supprimer = int(input("Entrez le nombre que vous souhaitez supprimer : "))

while nombre_a_supprimer in liste:
    liste.remove(nombre_a_supprimer)
print("Liste après suppression des occurrences :", liste)
