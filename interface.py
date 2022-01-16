import pygame
pygame.init()

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.frame = pygame.display.set_mode((largeur, hauteur), vsync=0)
        self.loop()


    
    def loop(self):
        self.alive = True
        while self.alive:
            pygame.mouse.set_visible(False)
            fecran = pygame.image.load('images/table.jpg')                # Fond d'ecran à modifier
            curseur = pygame.image.load('images/Cotton_gloves.png')
            curseur = pygame.transform.scale(curseur, (50, 50))           # Permet de changer la taille du curseur
            curseur = pygame.transform.rotate(curseur, -90)              # Change la rotation
            self.frame.blit(fecran, (0, 0))                               # Commande qui permet de mettre le fond d'ecran sur l'image
            x, y = pygame.mouse.get_pos()                                 # J'obtient les positions x et y de ma souris
            self.frame.blit(curseur, (x -20, y -20))                       #Permet de cadrer l'image


            for e in pygame.event.get() :
                if e.type == pygame.QUIT:
                    self.alive = False
            pygame.display.flip()


test = Interface()
