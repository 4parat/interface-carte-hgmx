from exceptions import *
from carte import *
from random import *
import pygame


class Paquet(pygame.sprite.LayeredUpdates):
    def __init__(self, vide = False, joker = False):
        super().__init__(self)
        self.retourné = False

        if not vide:                # Permet d'initialiser un paquet avec toute les cartes               
            for i in ["pique", "coeur", "treifle", "carreau"]: 
                for j in range(13):
                    self.add(Carte(i, j+1))
        if joker:
            for i in range(2):
                self.add(Carte(None, 0))      # J'avoue ne pas avoir trouver de sprite pour les jokers

    def __repr__(self):             # permet d'afficher l'ensemble des cartes du paquet dans la console en faisant print(paquet)
        repr = ""
        for i in self:
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
        return self.get_sprite(i)

    def taille(self):
        return self.sprites().__len__()

    def inverser(self):                         # Permet de changer l'ORDRE des cartes (la première devient la dernière et vice versa sans changer en gardant le fait)
        self.sprites = self.sprites()[::-1]         # que les cartes soient retourné ou non

    def retourner(self):                        # Permet de retourner le paquet comme dans la réalité : la première devient la dernière et toute les cartes sont
        self.retourné = not self.retourné       # retournés.
        for i in self:
            i.retourner()
        self.inverser()

    def melanger(self):             # Permet de mélanger les cartes
        shuffle(self)
    
    # def donner(self, paquet, nb):   # Permet de transférer nb cartes du paquet "self" vers un paquet "paquet"
    #     for i in range(nb):
    #         paquet.cartes.append(self[-1])
    #         self.cartes.pop(-1)

    # def prendre(self, paquet, nb):  # Permet de faire l'inverse de la fonction précédente
    #     if nb > paquet.cartes.__len__():
    #         raise pasAssezDeCarte()
    #     for i in range(nb):
    #         self.cartes.append(paquet[-1])
    #         paquet.cartes.pop(-1)
        
    