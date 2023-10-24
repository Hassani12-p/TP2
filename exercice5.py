def inserer_valeur_triee(L, val):
    index = 0
    while index < len(L) and L[index] < val:
        index += 1

    L.insert(index, val)

liste_triee = [1, 3, 5, 7, 9]
valeur_a_inserer = 10

inserer_valeur_triee(liste_triee, valeur_a_inserer)

print("Liste triée après insertion :", liste_triee)
