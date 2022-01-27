import pygame
import time

pygame.mixer.init()
pygame.display.init()

screen = pygame.display.set_mode ( ( 420 , 240 ) )

playlist = list()
playlist.append ( "musiques/musique1.mp3" )
playlist.append ( "musiques/musique2.mp3" )
playlist.append ( "musiques/musique3.mp3" )

pygame.mixer.music.load ( playlist.pop() )  # va lire la première musique de la playlist
pygame.mixer.music.queue ( playlist.pop() ) # la deuxième musique de la playlist
pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
pygame.mixer.music.play()           # lire la musique automatiquement 
