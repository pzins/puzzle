import pygame
import sys
from pygame.locals import *
from random import randint

class Tile:
    """ carreau du puzzle """
    def __init__(self,name, num, coord, img):
        self.name = name
        self.coo = coord
        self.image = img
        self.image.set_alpha(100)
        self.numero = num
        self.update_coo()
        
    def update_coo(self):
        """update les vraies coo"""
        self.real_coo = (self.coo[0]*146, self.coo[1]*146)
        if int(self.name[1]) == self.coo[0] and int(self.name[0]) == self.coo[1]:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(100)
    
    
def tupleValide(t):
    """test si un tuple a des coo coherentes avec la grille"""
    return t[0] >= 0 and t[0] <= 3 and t[1] >= 0 and t[1] <= 3

def getVoisins(black):
    """return list des carreaux voisins"""
    black = black[0]
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
    """test si le clic est bien sur le carreaux de coordonnees coo """
    return coo[0] * 146 <= mouse[0] and coo[0] * 146 + 145 >= mouse[0] and coo[1] * 146 <= mouse[1] and coo[1] * 146 + 145 >= mouse[1]

def update(tiles, fen):
    """update l'affichage"""
    for i in tiles:
        fen.blit(i.image, i.real_coo)

def exchangePos(black, tiles, voisin):
    """echange un carreau voisin avec le carreau noir"""
    for i in tiles:
        if i.coo == voisin:
            i.coo, black[0] = black[0], i.coo
            i.update_coo()
            return 0   

pygame.init()
fenetre = pygame.display.set_mode((584, 584)) #fenetre du jeu
pos_dispo = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)] #coo des positions dispo grille
tiles = [] #list contenant les carreaux
cpt = 0 #compteur

#initialisation
for i in range(4):
    for j in range(4):
        if j != 3 or i != 3:
            choice = randint(0,len(pos_dispo)-1)
            t = Tile(str(i)+str(j),cpt, pos_dispo[choice],pygame.image.load("img/ol"+str(i)+str(j)+".jpg").convert())
            tiles.append(t)
            del pos_dispo[choice]
            cpt += 1

update(tiles, fenetre)
black = pos_dispo #position de la case vide, on utilise une liste pour passage par reference

pygame.display.flip() #update the content of the entire display


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            voisins = getVoisins(black)
            for i in voisins:
                if isOnTile(i, event.pos):
                    exchangePos(black, tiles, i)
                    fenetre.fill((0,0,0))
                    update(tiles, fenetre)
                    pygame.display.flip()
