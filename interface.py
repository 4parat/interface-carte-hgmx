import pygame
pygame.init()
from souris import *

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.fecran = pygame.image.load("images/table.jpg")
        self.fecran = pygame.transform.scale(self.fecran, (largeur, hauteur))
        self.frame = pygame.display.set_mode((largeur, hauteur))        # Rajouter pygame.FULLSCREEN pour mettre en plein ecran
        self.mon_groupe = pygame.sprite.Group()
        self.souris = Souris()

        self.plateau = Plateau()
        paquet = Paquet(vide = True)
        carte1 = Carte("pique", 1)
        
        self.plateau.ajouter_paquet(paquet)
        self.plateau[0].cartes.append(carte1)
    
    def loop(self):
        self.alive = True

        while self.alive:
            self.frame.blit(self.fecran,(0,0))


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
                    for paq in self.plateau.paquets:
                        for carte in paq:
                            if pygame.Rect.colliderect(pygame.mouse.pos): #### Continuer
                                carte.retourner()

            self.mon_groupe.draw(self.frame)
            self.souris.update(self.frame)                                  # Affiche la Souris depuis souris.py
            pygame.display.flip()
