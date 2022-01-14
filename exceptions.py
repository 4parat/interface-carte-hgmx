# On définira toutes les erreurs ici. Par exemple si on prend plus de cartes qui possible dans un paquet, il y aura une erreur qui sera
# affiché à l'écran du type "pasAssezDeCarte" 

class pasAssezDeCarte(Exception):
    def __init__(self):
        super().__init__("Erreur : pas assez de carte à tirer.")
        