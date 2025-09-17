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
tentativeMax = 4 
listeCouleurs = ["R", "G", "B", "Y", "P", "W"]
rangeCouleurs = 5

tentative = 0
listeRndCouleurs = []
listeChoixJoueur = []
listeVerif = []
winGame = 0
correct = 0
partiel = 0
play = 0
nbrTotPartie = 0
win = 0
lost = 0

a=0
for a in range(5):
    rndCouleurs = random.choice(listeCouleurs)
    listeRndCouleurs.append(rndCouleurs)
# print(listeRndCouleurs) // Utile au debug

print("---------------------------")
print("  Bienvenue au Mastermind  ")
print("---------------------------")
print("")
fichierScore = open("score.txt", "r").read()
print(f"Nombre de victoires précédente série: {fichierScore}")
print("")
print("")

def demandeJeu (play, nbrTotPartie, win, lost):
    while 1:
        try: 
            print(f"Nombre de partie réalisé - {nbrTotPartie}")
            avisJoueur = input("Voulez vous jouer ? (Y/N): ")
            if avisJoueur != "Y" and avisJoueur != "N":
                print(f"Choisir avec 'N' -> Non ou 'Y' -> Yes ")
                print("")

        except ValueError:
            print(f"Choisir avec 'N' -> Non ou 'Y' -> Yes ")
            print("")

        if avisJoueur == "Y":
            play = 1
            nbrTotPartie = nbrTotPartie + 1
            print("Préparer vous à jouer ...")
            break

        if avisJoueur == "N":
            play = 0
            print("")
            print("---------------------------")
            print(f"Pour un total de {nbrTotPartie} partie(s): victoire = {win}, defaite = {lost}")
            print("Dommage, à bientôt!")
            print("---------------------------")
            open("score.txt", "w").write(str(nbrTotPartie))
            print("Score enregistré !")
            nbrTotPartie = 0
            break
        
    return play, nbrTotPartie, win, lost

play, nbrTotPartie, win, lost = demandeJeu(play, nbrTotPartie, win, lost)
os.system('cls')




while (play == 1): # Jouer plusieurs fois
    while (winGame == 0 and tentative <= (tentativeMax + 1)): # conditions d'arrêts
         
        print("")
        print(f">> Choisir parmi cette liste de couleur: {listeCouleurs}")
        print("")

        b=0
        c = 0
        for b in range(rangeCouleurs):
            try: 
                choixJoueur = str(input(f"Couleur {b} : "))
                if choixJoueur not in listeCouleurs and choixJoueur != "":
                    print(f"Choisir parmi cette liste de couleur: {listeCouleurs}")
                    break
            except ValueError:
                print(f"Choisir parmi cette liste de couleur: {listeCouleurs}")
                

            listeChoixJoueur.append(choixJoueur)
            print(listeChoixJoueur)
            print("")

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
            win = win + 1
            print("")
            print("Vous avez gagné !")
            print("")
            break
        else:
            if tentative <= tentativeMax:
                print("Essayer de nouveau")
                print(f"Encore {tentativeMax - tentative} tentative(s)")
                print("")
                tentative = tentative + 1
            else:
                lost = lost + 1
                print("Vous avez perdu :(")
                print("")
                break

        correct = partiel = 0
        listeChoixJoueur = []

    tentative = 0
    avisJoueur = 0
    play, nbrTotPartie, win, lost = demandeJeu(play, nbrTotPartie, win, lost)





