from paquet import *
from exceptions import *


class Plateau:
    def __init__(self):
        self.paquets = []
    
    def creer_paquet(self):                                 # crée un paquet sur le plateau
        self.paquets.append(Paquet())
    
    def supprimer_paquet(self, paquet):                     # supprime un paquet du plateau
        for i in range(len(self.paquets)):
            if self.paquets[i] is paquet:
                self.paquets.pop(i)
                del paquet
                return
        raise paquetPasSurLePlateauError(self)

    def ajouter_paquet(self, paquet):                       # ajoute un paquet déja existant sur le plateau
        self.paquets.append(paquet)
    


