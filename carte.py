class Carte:
    def __init__(self, enseigne, valeur):
        self.enseigne = enseigne        # la couleur de la carte
        self.valeur = valeur            # la valeur de la carte (as = 1, valet = 11, dame=  12, roi = 13, et joker = 0)
        self.x = 0                      # position en x
        self.y = 0                      # position en y
        self.retourné = False           # Vrai si la carte est face caché
    
    def estFigure(self):                # retourne vrai si la carte est un valet, une dame, ou un roi
        return self.valeur > 10
    
    def retourner(self):                # permet de retourner la carte (swap de True à False ou de False à True)
        self.retourné = not self.retourné