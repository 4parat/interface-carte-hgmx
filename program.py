from plateau import *
from paquet import *
from interface import *
from carte import *

fullscreen = pygame.display.Info()
x = fullscreen.current_w                             #renvoi les dimensions actuelle de votre ecran qu'importe la taille
y = fullscreen.current_h                             #Aller voir https://www.pygame.org/docs/ref/display.html#pygame.display.Info pour comprendre
interface = Interface(x, y)
plateau = interface.plateau
plateau.creer_paquet(vide = True)
plateau[0].add(Carte("coeur", 1))
plateau[0].add(Carte("pique", 1))
interface.loop()


