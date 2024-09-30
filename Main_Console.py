'''
Nicolas FELS
30/09/2024
But: Main du jeu du pendu version console
A faire: Proposer de rejouer et sauvegarder les scores'''

from Library import fJeu

print("Bienvenu dans le jeu du pendu")
choix = False
while choix == False:
    rep = input("Voulez vous faire une partie ? (o ou n): ")
    rep.lower()
    if rep != "o" and rep != "n":
        print("Je n'ai pas compris votre demande.")
    else:
        choix = True
if rep == "o":
    Victoire, Mot = fJeu()
    if Victoire == True:
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu, le mot était: ", Mot)
else:
    print("Au revoir")