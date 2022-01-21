import pygame
pygame.init()
from souris import *
from plateau import *

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.fecran = pygame.image.load("images/table.jpg")
        self.fecran = pygame.transform.scale(self.fecran, (largeur, hauteur))
        self.frame = pygame.display.set_mode((largeur, hauteur))        # Rajouter pygame.FULLSCREEN pour mettre en plein ecran
        self.groupe = pygame.sprite.LayeredUpdates()
        self.souris = Souris()

        self.plateau = Plateau()

    def loop(self):
        self.alive = True
        

        while self.alive:
            self.frame.blit(self.fecran,(0,0))

            self.vitesseCurseurX, self.vitesseCurseurY = pygame.mouse.get_rel()     # permet simplement de débugger cette fonction de l'enfer pour updatePlateau()
                                                                                    # Ça serait peut etre mieux de trouver un moyen de le faire dans curseur.py



            pression = pygame.mouse.get_pressed(3)
            if pression[0] == True :
                self.souris.click_G()
            elif pression[1] == True :                                      #A faire : Gerer le click droit
                #self.souris.Click_D()
                pass
            elif pression[2] == True :
                self.souris.click_M()
            else:
                self.souris.reinitialiser()




            for event in pygame.event.get() :                                   # Boucle qui teste les évènements
                
                if event.type == pygame.QUIT:
                    self.alive = False


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                            for paq in self.plateau.paquets:
                                for carte in paq:
                                    if carte.rect.collidepoint(pygame.mouse.get_pos()): #### Continuer
                                        self.plateau.carte_en_main = carte
                                        self.groupe.move_to_front(carte)
                    
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.plateau.carte_en_main = None


                if event.type == pygame.KEYDOWN:                            # permet de finir quitter le jeu lorsque l'on press échappe
                    if event.key == pygame.K_ESCAPE:
                        self.alive = False
            
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
