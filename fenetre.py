import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((520, 520))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))



perso = pygame.image.load("perso.jpg").convert()
perso.set_colorkey((255,255,255))
perso = pygame.transform.scale(perso, (75,75))
pos_perso = perso.get_rect()
fenetre.blit(perso, pos_perso)




#Rafraîchissement de l'écran
pygame.display.flip()

pygame.key.set_repeat(400,30)
SPEED = 5
#BOUCLE INFINIE
continuer = 1
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = 0
                if event.type == KEYDOWN:
                        if event.key == K_UP:
                                pos_perso = pos_perso.move(0,-SPEED)
                        elif event.key == K_DOWN:
                                pos_perso = pos_perso.move(0,SPEED)
                        elif event.key == K_LEFT:
                                pos_perso = pos_perso.move(-SPEED,0)
                        elif event.key == K_RIGHT:
                                pos_perso = pos_perso.move(SPEED,0)
        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, pos_perso)
        pygame.display.flip()

