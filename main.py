# Mastermind #

# Librairies 
import random
import os

os.system('cls')

# Red = R
# Green = G
# Blue = B
# Yellow = Y
# Purple = P 
# White = W


# Démmarage de la partie

tentative = 0
listeCouleurs = ["R", "G", "B", "Y", "P", "W"]
listeRndCouleurs = []
listeChoixJoueur = []
winGame = 0
correct = 0
partiel = 0
resultTour = 0
a=0
for a in range(5):
    rndCouleurs = random.choice(listeCouleurs)
    listeRndCouleurs.append(rndCouleurs)
    print(listeRndCouleurs)

print("Bienvenue au Mastermind:")

while (winGame == 0 and tentative <=12):
    
    tentative = tentative + 1

    b=0
    c = 0
    for b in range(5):
        try: 
            choixJoueur = str(input(f"Couleur {b} : "))
            if choixJoueur not in listeCouleurs:
                print(f"Choisir parmi cette liste de couleur: {listeCouleurs}")
                break
        except ValueError:
            print(f"Choisir parmi cette liste de couleur: {listeCouleurs}")

        listeChoixJoueur.append(choixJoueur)
        print(listeChoixJoueur)

        if listeChoixJoueur [b] == listeRndCouleurs [b]:
            correct = correct + 1
        
        for c in range(5):
            if listeChoixJoueur [b] == listeRndCouleurs [c]:
                partiel = partiel + 1
                print(f"b: {b} | c: {c}")
    
    partiel = partiel - correct   
    print(f"Correct: {correct} | Partiel: {partiel}")
    correct = partiel = 0




