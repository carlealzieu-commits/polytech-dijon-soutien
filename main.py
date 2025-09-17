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

# Variables pouvant variés
tentativeMax = 12
listeCouleurs = ["R", "G", "B", "Y", "P", "W"]
rangeCouleurs = 5

tentative = 0
listeRndCouleurs = []
listeChoixJoueur = []
listeVerif = []
winGame = 0
correct = 0
partiel = 0

a=0
for a in range(5):
    rndCouleurs = random.choice(listeCouleurs)
    listeRndCouleurs.append(rndCouleurs)
print(listeRndCouleurs)

print("Bienvenue au Mastermind:")

while (winGame == 0 and tentative <= nbrTentatives):
    
    tentative = tentative + 1

    b=0
    c = 0
    for b in range(rangeCouleurs):
        try: 
            choixJoueur = str(input(f"Couleur {b} : "))
            if choixJoueur not in listeCouleurs:
                print(f"Choisir parmi cette liste de couleur: {listeCouleurs}")
                break
        except ValueError:
            print(f"Choisir parmi cette liste de couleur: {listeCouleurs}")

        listeChoixJoueur.append(choixJoueur)
        print(listeChoixJoueur)

        # Trouver le nbr de partiel et correct 
        if listeChoixJoueur [b] == listeRndCouleurs [b]:
            correct = correct + 1
            listeVerif.append(b)
        else:
            for c in range(rangeCouleurs):
                if b != c and c not in listeVerif:
                    if listeChoixJoueur [b] == listeRndCouleurs [c]:
                        partiel = partiel + 1
                        listeVerif.append(c)
                        break

    
    
    print(f"Correct: {correct} | Partiel: {partiel }")

    if correct == rangeCouleurs:
        print("Vous avez gagné !")
        break
    else:
        print("Essayer de nouveau")
        print(f"Encore {tentative} tentative(s)")
    correct = partiel = 0




