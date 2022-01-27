import pygame
from souris import *
from plateau import *
from Bouton import *

pygame.init()

class Interface:            # À compléter plus tard
    def __init__(self, largeur = 800, hauteur = 450):
        pygame.display.set_caption("Card Game")
        self.fecran = pygame.image.load("images/plateau.jpeg")
        self.fecran = pygame.transform.scale(self.fecran, (largeur, hauteur))
        self.frame = pygame.display.set_mode((largeur, hauteur))        # Rajouter pygame.FULLSCREEN pour mettre en plein ecran
        self.souris = Souris()

        self.bouton_quitter = pygame.image.load("images/Boutton_quitter.png")
        self.bouton_quitter = pygame.transform.scale(self.bouton_quitter, (60, 60))
        self.bouton_quitter = Bouton(largeur - 60,0,self.bouton_quitter)

        self.bouton_stopmusique = pygame.image.load("images/stopMusique.png")
        self.bouton_stopmusique = pygame.transform.scale(self.bouton_stopmusique, (60, 60))
        self.bouton_stopmusique = Bouton(largeur - 120,0,self.bouton_stopmusique)

        self.bouton_musiqueOn = pygame.image.load("images/musiqueOn.png")
        self.bouton_musiqueOn = pygame.transform.scale(self.bouton_musiqueOn, (60, 60))
        self.bouton_musiqueOn = Bouton(largeur - 120,0,self.bouton_musiqueOn)


        self.bouton_changementMusique = pygame.image.load("images/changementMusique.png")
        self.bouton_changementMusique = pygame.transform.scale(self.bouton_changementMusique, (60, 60))
        self.bouton_changementMusique = Bouton(largeur - 180,0,self.bouton_changementMusique)


        self.hauteur = hauteur
        self.largeur = largeur
        self.plateau = Plateau()

    def loop(self):
        self.test_musique = True
        self.alive = True
        

        while self.alive:
            self.frame.blit(self.fecran,(0,0))

            self.vitesseCurseurX, self.vitesseCurseurY = pygame.mouse.get_rel()     # permet simplement de débugger cette fonction de l'enfer pour updatePlateau()
                                                                                    # Ça serait peut etre mieux de trouver un moyen de le faire dans curseur.py



            for event in pygame.event.get() :                            ############ BOUCLE DES ÉVÈNEMENTS
                

                if event.type == pygame.USEREVENT:                                 
                    if len ( playlist ) > 0:                               # evenement de la musique
                        pygame.mixer.music.queue ( playlist.pop() )                 

                
                if event.type == pygame.QUIT:                   # Gestion de la fermeture du programme
                    self.alive = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.bouton_quitter.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
                       self.alive = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.bouton_stopmusique.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
                    self.test_musique = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.bouton_musiqueOn.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
                    self.test_musique = False
                
                #if event.type == pygame.KEYDOWN and event.key == KEYESCAPE:
                #    if menu:
                #        menu = False
                

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lorsque clic gauche enfoncé
                    self.souris.click_G()                                           # Load le sprite du clic gauche
                    for paquet in self.plateau.paquets:                             # Ajoute la carte touché par le clic en main
                        if paquet[-1].rect.collidepoint(pygame.mouse.get_pos()):     
                            self.plateau.carte_en_main.add(paquet[-1])
                            paquet.remove(paquet[-1])
                            print("Transfert paquet vers main")
                        if paquet.sprites() == []:
                            print("Suppression du paquet")
                            self.plateau.paquets.remove(paquet)
                    
                                

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:    # Lorsque clic gauche désenfoncé
                    self.souris.reinitialiser()                                     # Reset le sprite de la souris
                    
                    carte_dans_paquet = False
                    for paquet in self.plateau.paquets:
                        if self.plateau.carte_en_main[0].rect.colliderect(paquet[-1]):  #!! Erreur sur paquet[-1]
                            self.plateau.carte_en_main[0].rect.centerx = paquet[-1].rect.centerx
                            self.plateau.carte_en_main[0].rect.centery = paquet[-1].rect.centery
                            paquet.add(self.plateau.carte_en_main[0])

                            print("Transfert main vers paquet")
                            carte_dans_paquet = True
                            break
                    
                    if not carte_dans_paquet:
                        paq = Paquet(vide = True)
                        self.plateau.paquets.append(paq)
                        paq.add(self.plateau.carte_en_main[0])
                        print("Création du paquet")
                    self.plateau.carte_en_main.empty()                               # Enlève la carte de la main
                

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Lorsque clic droit enfoncé
                    if self.plateau.carte_en_main.sprites != []:                          # si main non vide
                        self.plateau.carte_en_main.retourner()                          # retourne la carte dans la main
                    else:
                        for paquets in self.plateau.paquets:                        # sinon test si carte en dessous de la souris
                                                                                    # puis la retourne
                            for carte in paquets:
                                if carte.rect.collidepoint(pygame.mouse.get_pos()):
                                    carte.retourner()

            
            self.updatePlateau()                                            # update le plateau (affiche les cartes, gère la carte en main, ect...)


            self.bouton_quitter.update(self.frame)

            if self.test_musique == True:

                self.bouton_musiqueOn.update(self.frame)
            if self.test_musique == False:
                self.bouton_stopmusique.update(self.frame)

            self.souris.update(self.frame)                                  # Affiche la Souris depuis souris.py



            pygame.display.flip()                                           # refresh l'image à partir du nouvel état de self.groupe


            
    def updatePlateau(self):
        for paquet in self.plateau.paquets:
            paquet.draw(self.frame)

        if len(self.plateau.carte_en_main.sprites()) != 0:
            self.plateau.carte_en_main[0].deplacer(self.vitesseCurseurX, self.vitesseCurseurY)
            self.plateau.carte_en_main.draw(self.frame)



        