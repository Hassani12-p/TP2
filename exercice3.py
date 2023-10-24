import random
nombre_secret = random.randint(1, 100)
essais_restants = 7

for essai in range(1, 8):
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if devine == nombre_secret:
        print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {essai} essais.")
        break
    elif devine < nombre_secret:
        print("Le nombre est trop petit. Essayez encore.")
    else:
        print("Le nombre est trop grand. Essayez encore.")
    essais_restants -= 1
    print(f"Il vous reste {essais_restants} essais.\n")


if essais_restants == 0:
    print(f"Désolé, vous n'avez pas trouvé le nombre. Le nombre était {nombre_secret}.")
