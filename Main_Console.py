'''
Nicolas FELS
30/09/2024
But: Main du jeu du pendu version console
A faire: '''

from Library import fJeu

print("Bienvenu dans le jeu du pendu")
choix = False
while choix == False:
    rep = input("Voulez vous faire une partie ? (o ou n): ")
    if rep.lower not in [o, n]:
        print("Je n'ai pas compris votre demande.")
    else:
        choix = True
Victoire, Mot = fJeu()
if Victoire == True:
    print("Vous avez gagné !")
else:
    print("Vous avez perdu, le mot était: " + Mot)