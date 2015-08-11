import pygame
from pygame.locals import *
from random import randint

def tupleValide(t):
    return t[0] >= 0 and t[0] <= 3 and t[1] >= 0 and t[1] <= 3

def getVoisins(black):
    print(black)
    res = []
    tmp = []
    tmp.append((black[0]-1, black[1]))
    tmp.append((black[0]+1, black[1]))
    tmp.append((black[0], black[1]-1))
    tmp.append((black[0], black[1]+1))
    for i in range(4):
        if tupleValide(tmp[i]):
            res.append(tmp[i])
    return res

def isOnTile(coo, mouse):
    return coo[0] * 146 <= mouse[0] and coo[0] * 146 + 145 >= mouse[0] and coo[1] * 146 <= mouse[1] and coo[1] * 146 + 145 >= mouse[1]

def update(sq, pos, fen):
    for i in range(len(sq)):
        fen.blit(sq[i], pos[i])

def exchangePos(black, sq, pos, coo, coo_tuple):
    print("OL: ",coo," OL")
    a = coo.index(coo_tuple)
    coo[a], black = black, coo[a]
    pos[a] = (coo[a][0] * 146, coo[a][1] * 146)

    
    


    
pygame.init()
fenetre = pygame.display.set_mode((584, 584))

squares = []
positions = []
coo = []
cpt = 0
pos_dispo = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]

for i in range(4):
    for j in range(4):
        if j != 3 or i != 3:
            squares.append(pygame.image.load("img/ol"+str(i)+str(j)+".jpg").convert())
            positions.append(squares[cpt].get_rect())
            choice = randint(0,len(pos_dispo)-1)
            positions[cpt] = positions[cpt].move(pos_dispo[choice][0] * 146, pos_dispo[choice][1] * 146)
            coo.append(pos_dispo[choice])
            del pos_dispo[choice]
            update(squares, positions, fenetre)
#            fenetre.blit(squares[cpt], positions[cpt])
            cpt += 1

black = pos_dispo[0]

                       
pygame.display.flip()

continuer = 1
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("black : ", black)
                    tile = getVoisins(black)
                    print("tile : ", tile)
                    print("mouse : ", event.pos)
                    for i in tile:
                        if isOnTile(i, event.pos):
                            exchangePos(black, squares, positions, coo, i)
                            fenetre.fill((0,0,0))
                            update(squares, positions, fenetre)
                            pygame.display.flip()
