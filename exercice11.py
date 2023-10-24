def transformation_miroir(liste):
    return liste[::-1]

L = [8, 24, 48, 2, 16]
resultat = transformation_miroir(L)

print("Liste originale:", L)
print("Résultat de la transformation miroir:", resultat)
