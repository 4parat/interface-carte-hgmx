from carte import *
from random import *

class Paquet:
    def __init__(self, vide = False):
        self.cartes = []            # Liste stockant les cartes
        self.nbCartes = 0           # Nombre de cartes dans le paquet (pour éviter de faire len(paquet.cartes) a chaque fois)
        self.retourné = True

        if not vide:                # Permet d'initialiser un paquet avec toute les cartes               
            for i in ["pique", "coeur", "treifle", "carreau"]: 
                for j in range(13):
                    self.cartes.append(Carte(i, j+1))
            for i in range(2):
                self.cartes.append(Carte(None, 0))
            self.nbCartes = 54

    def __repr__(self):             # permet d'afficher l'ensemble des cartes du paquet dans la console en faisant print(paquet)
        repr = ""
        for i in self.cartes:
            if i.valeur == 0 :
                repr += "Joker"
            elif i.valeur == 1:
                repr += "As de " + i.enseigne
            elif i.valeur == 11:
                repr += "Valet de " + i.enseigne
            elif i.valeur == 12:
                repr += "Dame de " + i.enseigne
            elif i.valeur == 13:
                repr += "Roi de " + i.enseigne
            else:
                repr += str(i.valeur) + " de " + i.enseigne
            
            repr += "\n"
        return repr
    
    def __getitem__(self, i):       # Permet d'accéder à une carte en ieme position en faisant paquet[i]
        return self.cartes[i]

    def retourner(self):
        self.retourné = not self.retournée

    def melanger(self):             # Permet de mélanger les cartes
        shuffle(self.cartes)
    
    def donner(self, paquet, nb):   # Permet de transférer nb cartes du paquet "self" vers un paquet "paquet"
        k = -1 if self.retourné else 0
        l = -1 if paquet.retourné else 0
        for i in range(nb):
            paquet.cartes.insert(l, self[k])
            paquet.nbCartes += 1
            self.cartes.pop(k)
            self.nbCartes -= 1

    def prendre(self, paquet, nb):  # Permet de faire l'inverse de la fonction précédente
        k = -1 if self.retourné else 0
        l = -1 if paquet.retourné else 0
        for i in range(nb):
            self.cartes.insert(l, paquet[k])
            self.nbCartes +=1
            paquet.cartes.pop(k)
            paquet.nbCartes -= 1