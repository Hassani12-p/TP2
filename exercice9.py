def convertir_euro_en_mad(euro):
    return euro * 10.86

def convertir_mad_en_euro(mad):
    return mad * 0.092

def main():
    while True:
        print("Choisissez la direction de conversion:")
        print("1. Euro en MAD")
        print("2. MAD en Euro")

        choix = input("Entrez 1 ou 2 (ou un nombre négatif pour quitter): ")

        if choix.startswith('-'):
            break

        try:
            choix = int(choix)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choix == 1:
            euro = float(input("Entrez la valeur en Euro: "))
            mad = convertir_euro_en_mad(euro)
            print(f"{euro} Euro = {mad} MAD")
        elif choix == 2:
            mad = float(input("Entrez la valeur en MAD: "))
            euro = convertir_mad_en_euro(mad)
            print(f"{mad} MAD = {euro} Euro")
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")


