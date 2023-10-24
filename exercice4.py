# Liste initiale
L = [1, -30, 0, -2, 500, 4, 2, 100]

nombres_negatifs = []
nombres_positifs = []

for nombre in L:
    if nombre < 0:
        nombres_negatifs.append(nombre)
    else:
        nombres_positifs.append(nombre)

M = nombres_negatifs + nombres_positifs

print("Liste M avec les nombres négatifs au début et les positifs à la fin :", M)
