from plateau import *
from paquet import *
from interface import *
from carte import *

interface = Interface(1700, 900)

carte1 = Carte("", 0)
interface.mon_groupe.add(carte1)
interface.loop()