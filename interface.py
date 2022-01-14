from pygame import *

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        self.frame = display.set_mode((largeur, hauteur), vsync=0)
        self.loop()
    
    def loop(self):
        self.alive = True
        while self.alive:
            for e in event.get() :
                if e.type == QUIT:
                    self.alive = False
            display.flip()