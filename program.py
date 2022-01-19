from plateau import *
from paquet import *
from interface import *
from carte import *


plat = Interface(1920, 1080)

carte1 = Carte("", 0)

plat.mon_groupe.add(carte1)
plat.loop()