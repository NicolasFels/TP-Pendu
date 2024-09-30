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
    num = randint(0, len(liste_mots)-1)
    return liste_mots[num]

def fAffichage(pMot):
    '''Renvoi le mot en affichant la premiere lettre et les lettres 
    trouvee et des _ pour les autres
    '''
    global Lettres_trouvees
    Affiche = pMot[0]
    for lettre in pMot[1:-1]:
        if lettre in Lettres_trouvees:
            Affiche += lettre
        else:
            Affiche += " _"
    return Affiche

def fProposition():
    '''Demande une lettre ou un mot, puis verifie si l'entree est correcte et
    la met en minuscule, sinon redemande jusqu'à avoir une proposition correcte.
    Renvoi la proposition.
    '''
    global Liste_prop
    valide = False
    while valide == False:
        prop = input("Entree une lettre ou un mot: ")
        if len(prop) == 1:
            prop.lower()
            if prop.isalpha() == True:
                if prop not in Liste_prop:
                    Liste_prop.append(prop)
                    valide = True
                else:
                    print("Deja proposer ou non une lettre")
    return prop

def fVerification_prop(pMot, pProp):
    '''Verifie si la proposition est dans le mot ou est le mot lui meme.
    Renvoi True si c'est le cas, False sinon
    '''
    global Lettre_trouvees
    if pProp in pMot:
        if pProp not in Lettres_trouvees:
            Lettres_trouvees.append(pProp)
        return True
    return False

def fVictoire(pMot):
    '''Verifie si le joueur a gagner
    '''
    if "_" not in fAffichage(pMot):
        return True
    return False

def fJeu():
    '''Fonction principale qui gere le jeu du pendu. Renvoie True en as de victoire
    False sinon, ainsi que le mot
    '''
    global Lettres_trouvees, Liste_prop
    Mot_cache = fChoix_mot()
    Lettres_trouvees = []
    Liste_prop = []
    print(fAffichage(Mot_cache))
    Vie = 8
    while Vie > 0:
        print("Ce que vous avez deja proposez: ", Liste_prop)
        print("Ce que vous avez trouvee : ", Lettres_trouvees)
        Proposition = fProposition()
        if fVerification_prop(Mot_cache, Proposition) == False:
            print(Proposition + " n'est pas une lettre du mot ou le mot !")
            Vie -= 1
            print("Il vous reste ", Vie, " vies")
        print(fAffichage(Mot_cache))
        if fVictoire(Mot_cache) == True:
            return True, Mot_cache
    return False, Mot_cache