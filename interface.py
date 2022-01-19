import pygame
pygame.init()

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.frame = pygame.display.set_mode((largeur, hauteur))
        self.mon_groupe = pygame.sprite.Group()


    
    def loop(self):
        self.alive = True

        while self.alive:
            pygame.mouse.set_visible(False)
            fecran = pygame.image.load('images/table.jpg')                  # Fond d'ecran à modifier
            curseur = pygame.image.load('images/Cotton_gloves.png')
            self.frame.blit(fecran, (0, 0))                                 # Commande qui permet de mettre le fond d'ecran sur l'Interface
            curseur = pygame.transform.scale(curseur, (50, 50))             # Permet de changer la taille du curseur
            x, y = pygame.mouse.get_pos()                                   # J'obtient les positions x et y de ma souris


            pression = pygame.mouse.get_pressed(3)
            if pression[0] == True :
                curseur = pygame.image.load('images/Cotton_gloves_update.png')
                curseur = pygame.transform.scale(curseur, (27, 27))
                x = x + 12
                y = y + 12                                                  #Permet d'ajuster la position du nouveau gantelet
            elif pression[1] == True :                                      #A faire : Gerer le click droit
                pass

            curseur = pygame.transform.rotate(curseur, -90)                 # Change la rotation
            self.frame.blit(curseur, (x - 20, y - 20))                      # Permet de cadrer l'image



            for e in pygame.event.get() :                                   # Boucle qui teste les évènements
                if e.type == pygame.QUIT:
                    self.alive = False
            
            self.mon_groupe.draw(self.frame)
            pygame.display.flip()

interface = Interface()