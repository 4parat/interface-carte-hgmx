from plateau import *
from paquet import *
from interface import *
from carte import *

interface = Interface(1700, 900)
plateau = interface.plateau
plateau.creer_paquet(vide = True)
plateau.paquets[0].cartes.append(Carte("pique", 1))
plateau.paquets[0].cartes.append(Carte("coeur", 1))
plateau[0][1].teleporter(500, 500)
interface.loop()


