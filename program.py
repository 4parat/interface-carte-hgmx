from plateau import *
from paquet import *
from interface import *
from carte import *
from musique import *

fullscreen = pygame.display.Info()
x = fullscreen.current_w                             #renvoi les dimensions actuelle de votre ecran qu'importe la taille
y = fullscreen.current_h                             #Aller voir https://www.pygame.org/docs/ref/display.html#pygame.display.Info pour comprendre
interface = Interface(x, y)
plateau = interface.plateau
plateau.creer_paquet()
plateau[0].melanger()
plateau[0].retourner()
interface.loop()


