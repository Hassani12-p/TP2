
chiffre = int(input("Veuillez saisir un chiffre : "))

somme = 0

for i in range(1, 5):
    terme = int(str(chiffre) * i)
    somme += terme

print(f"La somme est : {'+'.join(map(str, [int(str(chiffre) * i) for i in range(1, 5)]))} = {somme}")
