class Carte:
    def __init__(self, enseigne, valeur):
        self.enseigne = enseigne        # la couleur de la carte
        self.valeur = valeur            # la valeur de la carte (as = 1, valet = 11, dame = 12, roi = 13, et joker = 0)
        self.x = 0                      # position en x
        self.y = 0                      # position en y
        self.sprite = ""                # définira ou se trouvera l'image de la carte
        self.retourné = False