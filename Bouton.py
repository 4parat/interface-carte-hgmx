import pygame


class Bouton(pygame.sprite.Sprite):
    def __init__(self,x,y,image):                                     #Mon bouton à besoin d'une image et de deux pos .
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()                             #Creation de la hitbox
        self.rect.x = x
        self.rect.y = y

    def update(self,interface):
        interface.blit(self.image, self.rect)                         #Colle l'image au position de la hitbox




