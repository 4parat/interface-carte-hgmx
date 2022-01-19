import pygame
pygame.init()
from interface import*
class Souris(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.curseur = pygame.image.load("images/Cotton_gloves.png")
        self.curseur = pygame.transform.scale(self.curseur, (50, 50))
        self.curseur = pygame.transform.rotate(self.curseur, -90)
        self.rect = self.curseur.get_rect()
        self.group_curseur = pygame.sprite.Group(curseur)

    def mouvement(self):
        pygame.mouse.set_visible(False)

        x, y = pygame.mouse.get_pos()
















