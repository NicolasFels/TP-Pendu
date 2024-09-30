'''
Nicolas FElS
30/09/2024
But: Creation des fonctions pour le jeu du pendu
A faire:
'''

from random import randint

def fChoix_mot(pListe):
    '''Fonction qui va choisir aléatoirement un mot dans une liste et le
    renvoi. 
    '''
    fich = open('mots.txt', 'r')
    liste_mots = fich.readlines()
    num = randint(0, len(liste_mots))
    return liste_mots[num]

def Affichage()