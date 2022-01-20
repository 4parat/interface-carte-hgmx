from paquet import *
from exceptions import *


class Plateau:
    def __init__(self):
        self.paquets = []

    def __getitem__(self, i):
        return self.paquets[i]
    
    def creer_paquet(self, vide = False, joker = False):                                 # crée un paquet sur le plateau
        self.paquets.append(Paquet(vide, joker))
    
    def supprimer_paquet(self, paquet):                     # supprime un paquet du plateau
        for i in range(len(self.paquets)):
            if self.paquets[i] is paquet:
                self.paquets.pop(i)
                del paquet
                return
        raise paquetPasSurLePlateauError(self)

    def ajouter_paquet(self, paquet):                       # ajoute un paquet déja existant sur le plateau
        self.paquets.append(paquet)
    


