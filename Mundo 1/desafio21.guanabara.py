#Desafio 21 - Curso em Vídeo
#Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
