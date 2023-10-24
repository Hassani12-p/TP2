
taille = int(input("Veuillez saisir la taille du triangle : "))

print("Triangle avec des étoiles :")
for i in range(1, taille + 1):
    print('* ' * i)


print("\nTriangle avec des nombres :")
for i in range(1, taille + 1):
    for j in range(i):
        print(i, end=" ")
    print()

