'''
Nicolas FElS
30/09/2024
But: Creation des fonctions pour le jeu du pendu
A faire:
'''

from random import randint

def fChoix_mot():
    '''Fonction qui va choisir aléatoirement un mot dans une liste et le
    renvoi. 
    '''
    fich = open('mots.txt', 'r')
    liste_mots = fich.readlines()
    num = randint(0, len(liste_mots))
    return liste_mots[num]

def fAffichage(pMot, pLettres_trouvees):
    '''Renvoi le mot en affichant la premiere lettre et les lettres 
    trouvee et des _ pour les autres
    '''
    Affiche = pMot[0]
    for lettre in pMot[1:]:
        if lettre in pLettres_trouvees:
            Affiche += lettre
        else:
            Affiche += " _"
    return Affiche

def fProposition():
    '''Demande une lettre ou un mot, puis verifie si l'entree est correcte et
    la met en minuscule, sinon redemande jusqu'à avoir une proposition correcte.
    Renvoi la proposition.
    '''
    valide = False
    while valide == False:
        prop = input("Entree une lettre ou un mot: ")
        prop.lower()
        if prop.isalpha() == True:
            valide = True
    return prop

def fVerification_prop(pMot, pProp, pLettres_trouvees):
    '''Verifie si la proposition est dans le mot ou est le mot lui meme.
    Renvoi True si c'est le cas, False sinon
    '''
    if pProp in pMot or pProp == pMot:
        for lettre in pProp:
            if lettre not in pLettres_trouvees:
                pLettres_trouvees.append(lettre)
        return True
    return False

def fVictoire(pMot, pLettres_trouvees):
    '''Verifie si toutes les lettres ont ete trouvees et renvoi True si c'est
    le cas.
    '''
    Lettre_mot = [lettre for lettre in pMot]
    if len(Lettre_mot) == len(pLettres_trouvees):
        return True
    return False


def fJeu():
    '''Fonction principale qui gere le jeu du pendu. Renvoie True en as de victoire
    False sinon, ainsi que le mot
    '''
    Mot_cache = fChoix_mot()
    Lettres_trouvees = []
    fAffichage(Mot_cache, Lettres_trouvees)
    Vie = 8
    while Vie > 8:
        Proposition = fProposition()
        if fVerification_prop(Mot_cache, Proposition, Lettres_trouvees) == False:
            print(Proposition + " n'est pas une lettre du mot ou le mot !")
            Vie -= 1
        fAffichage(Mot_cache, Lettres_trouvees)
        if fVictoire(Mot_cache, Lettres_trouvees) == True:
            return True, Mot_cache
    return False, Mot_cache