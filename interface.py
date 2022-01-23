import pygame
pygame.init()
from souris import *
from plateau import *
from Bouton import *

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.fecran = pygame.image.load("images/plateau.jpeg")
        self.fecran = pygame.transform.scale(self.fecran, (largeur, hauteur))
        self.frame = pygame.display.set_mode((largeur, hauteur),pygame.FULLSCREEN)        # Rajouter pygame.FULLSCREEN pour mettre en plein ecran
        self.groupe = pygame.sprite.LayeredUpdates()
        self.souris = Souris()
        self.bouton_quitter = pygame.image.load("images/Boutton_quitter.png")
        self.bouton_quitter = Bouton(largeur - 60,0,self.bouton_quitter)
        self.hauteur = hauteur
        self.largeur = largeur
        self.plateau = Plateau()

    def loop(self):
        self.alive = True
        

        while self.alive:
            self.frame.blit(self.fecran,(0,0))

            self.vitesseCurseurX, self.vitesseCurseurY = pygame.mouse.get_rel()     # permet simplement de débugger cette fonction de l'enfer pour updatePlateau()
                                                                                    # Ça serait peut etre mieux de trouver un moyen de le faire dans curseur.py



            for event in pygame.event.get() :                            ############ BOUCLE DES ÉVÈNEMENTS
                
                if event.type == pygame.QUIT:                   # Gestion de la fermeture du programme
                    self.alive = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.bouton_quitter.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
                       self.alive = False
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lorsque clic gauche enfoncé
                    self.souris.click_G()                                           # Load le sprite du clic gauche
                    for paquets in self.plateau.paquets:                            # Ajoute la carte touché par le clic en main
                        for carte in paquets:
                            if carte.rect.collidepoint(pygame.mouse.get_pos()):
                                self.plateau.carte_en_main = carte
                                self.groupe.move_to_front(carte)

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:    # Lorsque clic gauche désenfoncé
                    self.souris.reinitialiser()                                     # Reset le sprite de la souris
                    self.plateau.carte_en_main = None
                

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if self.plateau.carte_en_main != None:
                        self.plateau.carte_en_main.retourner()
                    else:
                        for paquets in self.plateau.paquets:
                            for carte in paquets:
                                if carte.rect.collidepoint(pygame.mouse.get_pos()):
                                    carte.retourner()

            
            self.updatePlateau()                                            # update le plateau (affiche les cartes, gère la carte en main, ect...)
            self.souris.update(self.frame)                                  # Affiche la Souris depuis souris.py
            pygame.display.flip()                                           # refresh l'image à partir du nouvel état de self.groupe


    def updatePlateau(self):
        if self.plateau.carte_en_main != None:
            
            self.plateau.carte_en_main.deplacer(self.vitesseCurseurX, self.vitesseCurseurY)

        for paquet in self.plateau.paquets:
            for carte in paquet.cartes:
                if carte not in self.groupe:
                    self.groupe.add(carte)


        self.groupe.draw(self.frame)
        self.bouton_quitter.update(self.frame)