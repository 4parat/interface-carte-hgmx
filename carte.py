import pygame

class Carte(pygame.sprite.Sprite):
    def __init__(self, enseigne, valeur):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.enseigne = enseigne        # la couleur de la carte
        self.valeur = valeur            # la valeur de la carte (as = 1, valet = 11, dame=  12, roi = 13, et joker = 0)
        self.retourné = False           # Vrai si la carte est face caché
    
        

        ens = ""
        val = ""

        if self.valeur == 0:
            self.image = pygame.image.load("images/cartes 2 (avec Jokers)/ace_of_hearts.png")
        else:
            if self.enseigne == "pique":
                ens = "spades"
            elif self.enseigne == "coeur":
                ens = "hearts"
            elif self.enseigne == "treifle":
                ens = "clubs"
            elif self.enseigne == "carreau":
                ens = "diamonds"

            if self.valeur == 1:
                val = "ace"
            elif self.valeur <= 10:
                val = str(self.valeur)
            elif self.valeur == 11:
                val = "jack"
            elif self.valeur == 12:
                val = "queen"
            elif self.valeur == 13:
                val = "king"
            #print("images/cartes 2 (avec Jokers)/"+val+'_of_'+ens+".png")
            self.image = pygame.image.load("images/cartes 2 (avec Jokers)/"+val+'_of_'+ens+".png")

        self.rect = self.image.get_rect()

        #pygame.draw.rect(self.image, pygame.Rect(0,0, 20, 10))

    def estFigure(self):                # retourne vrai si la carte est un valet, une dame, ou un roi
        return self.valeur > 10
    
    def retourner(self):                # permet de retourner la carte (swap de True à False ou de False à True)
        if self.retourné:
            if self.valeur == 0:
                self.image = pygame.image.load("images/cartes 2 (avec Jokers)/black_joker.png")
            else:
                if self.enseigne == "pique":
                    ens = "spades"
                elif self.enseigne == "coeur":
                    ens = "hearts"
                elif self.enseigne == "treifle":
                    ens = "clubs"
                elif self.enseigne == "carreau":
                    ens = "diamonds"

                if self.valeur == 1:
                    val = "ace"
                elif self.valeur <= 10:
                    val = str(self.valeur)
                elif self.valeur == 11:
                    val = "jack"
                elif self.valeur == 12:
                    val = "queen"
                elif self.valeur == 13:
                    val = "king"
                #print("images/cartes 2 (avec Jokers)/"+val+'_of_'+ens+".png")
                self.image = pygame.image.load("images/cartes 2 (avec Jokers)/"+val+'_of_'+ens+".png")
        else:
            self.image = pygame.image.load("images/cartes 2 (avec Jokers)/dos-bleu.png")

        self.retourné = not self.retourné


    