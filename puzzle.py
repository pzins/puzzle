import pygame
from pygame.locals import *
from random import randint

class Tile:
    """ carreau du puzzle """
    def __init__(self, num, coord, img):
        self.coo = coord
        self.image = img
        self.numero = num
        self.real_coo = (self.coo[0]*146, self.coo[1]*146)
        
    
    
    

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

def update(tiles, fen):
    for i in tiles:
        fen.blit(i.image, i.real_coo)

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

tiles = []

for i in range(4):
    for j in range(4):
        if j != 3 or i != 3:
            choice = randint(0,len(pos_dispo)-1)
            print(pos_dispo[choice])
            t = Tile(cpt, pos_dispo[choice],pygame.image.load("img/ol"+str(i)+str(j)+".jpg").convert())
            tiles.append(t)
#            squares.append(pygame.image.load("img/ol"+str(i)+str(j)+".jpg").convert())
 #           positions.append(squares[cpt].get_rect())
  #          choice = randint(0,len(pos_dispo)-1)
   #         positions[cpt] = positions[cpt].move(pos_dispo[choice][0] * 146, pos_dispo[choice][1] * 146)
    #        coo.append(pos_dispo[choice])
            del pos_dispo[choice]
#            update(squares, positions, fenetre)
#            fenetre.blit(t.image, t.real_coo)
            cpt += 1
update(tiles, fenetre)
black = pos_dispo[0]

                       
pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                tile = getVoisins(black)
                for i in tile:
                    if isOnTile(i, event.pos):
                        pygame.display.flip()
                        print('ol')
                        """
                        exchangePos(black, squares, positions, coo, i)
                        fenetre.fill((0,0,0))
                        update(squares, positions, fenetre)
                        """

