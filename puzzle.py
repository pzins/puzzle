import pygame
from pygame.locals import *
from random import randint

pygame.init()


fenetre = pygame.display.set_mode((584, 584))


squares = []
positions = []
cpt = 0
pos_dispo = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]


for i in range(4):
    for j in range(4):
        if j != 3 or i != 3:
            squares.append(pygame.image.load("img/ol"+str(i)+str(j)+".jpg").convert())
            positions.append(squares[i].get_rect())
            choice = randint(0,len(pos_dispo)-1)
            positions[cpt] = positions[cpt].move(pos_dispo[choice][0] * 146, pos_dispo[choice][1] * 146)
            del pos_dispo[choice]
            fenetre.blit(squares[cpt], positions[cpt])
            cpt += 1

print(cpt)

                       


pygame.display.flip()

continuer = 1
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = 0
                if event.type == MOUSEMOTION and event.buttons[0] == 1:
                    print(event.pos[0], event.pos[1])
                    
