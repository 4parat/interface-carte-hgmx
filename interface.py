import pygame
pygame.init()
from souris import *

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.fecran = pygame.image.load("images/table.jpg")
        self.fecran = pygame.transform.scale(self.fecran, (largeur, hauteur))
        self.frame = pygame.display.set_mode((largeur, hauteur))
        self.mon_groupe = pygame.sprite.Group()
        self.souris = Souris()

    
    def loop(self):
        self.alive = True

        while self.alive:
            self.frame.blit(self.fecran,(0,0))


            pression = pygame.mouse.get_pressed(3)
            if pression[0] == True :
                self.souris.click_G()
            elif pression[1] == True :                                      #A faire : Gerer le click droit
                pass
            else:
                self.souris.reinitialiser()




            for e in pygame.event.get() :                                   # Boucle qui teste les évènements
                if e.type == pygame.QUIT:
                    self.alive = False
            
            self.mon_groupe.draw(self.frame)
            self.souris.update(self.frame)                                  #Affiche la Souris depuis souris.py
            pygame.display.flip()

interface = Interface()