import pygame
import time

pygame.mixer.init()


playlist = list()
playlist.append ( "musiques/musique1.mp3" )  # charger la musique 1
playlist.append ( "musiques/musique3.mp3" )  # charger la musique 2
playlist.append ( "musiques/musique2.mp3" )  # charger la musique 3

pygame.mixer.music.load ( playlist.pop() )  
pygame.mixer.music.queue ( playlist.pop() ) 
pygame.mixer.music.set_endevent ( pygame.USEREVENT )   
pygame.mixer.music.play()   