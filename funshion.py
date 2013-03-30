
import pygame, string
import random
from pygame.locals import *
import glob
import os

"""
objects
"""
class world:
    def __init__(self, name):
        self.name = name

    def toggel(self, mousePos):
        x = int(((mousePos[0]+self.screenOffSet[0])/self.scale)+self.screenPos[0])
        y = int(((mousePos[1]+self.screenOffSet[1])/self.scale)+self.screenPos[1])
        if self.backTiles [y][x] == 0:
            self.backTiles [y][x]=1
        else:
            self.backTiles [y][x]=0


    def load (self):

        if  len(glob.glob("save//" + self.name + ".save")) == 0:
            print('macking new save')
            newGame(self.name)
        
        self.backTiles = loadBackTiles(self.name)
        vers = loadVars(self.name)
 
        #how meny tile acros the screen is
        self.screenPos = [vers[0],vers[1]]
        #what the of set is
        self.screenOffSet =[vers[2],vers[3]]
        self.scale = vers[4]

        print('loaded game')

    def checkOK(self,screnRes):
            while self.screenOffSet[0] > self.scale:
                self.screenOffSet[0] = self.screenOffSet[0] - self.scale
                self.screenPos[0] += 1
            while self.screenOffSet[1] > self.scale:
                self.screenOffSet[1] = self.screenOffSet[1] - self.scale
                self.screenPos[1] += 1
            while self.screenOffSet[0] < 0:
                self.screenOffSet[0] = self.screenOffSet[0] + self.scale
                self.screenPos[0] -= 1
            while self.screenOffSet[1] < 0:
                self.screenOffSet[1] = self.screenOffSet[1] + self.scale
                self.screenPos[1] -= 1

            if self.screenPos[0] < 0:
                self.screenPos[0] = 0
                self.screenOffSet[0] = 0
            if self.screenPos[1] < 0:
                self.screenPos[1] = 0
                self.screenOffSet[1] = 0
            if self.screenPos[0] > int(len(self.backTiles[0]) - (screnRes[0] / self.scale + 1)):
                self.screenPos[0] = int(len(self.backTiles[0]) - (screnRes[0] / self.scale + 1))
                self.screenOffSet[0] = self.scale - 1
            if self.screenPos[1] > len(self.backTiles) - (screnRes[1] / self.scale + 3):
                self.screenPos[1] = int(len(self.backTiles) - (screnRes[1] / self.scale + 3)) 
                self.screenOffSet[1] = self.scale - 1
        
class button:
    def __init__(self, XY, sysX, sysY, icon):
        self.XY = XY
        self.sysX = sysX
        self.sysY = sysY
        self.icon = icon


    def click(self, XY):
        if XY[0] > self.XY[0] and XY[0] < self.XY[0] + self.sysX:
            if XY[1] > self.XY[1] and XY[1] < self.XY[1] + self.sysY:
                return True
        return False
                 
            
    def ID(self):
        return str(self)


    def draw(self, screen):
        screen.blit(self.icon, self.XY)














def loadSprites():
    gotAll = False
    i = 0
    tiles = []
    while not gotAll:
        path = str( "sprites\\" + str(i) + ".png")
        try:
            tiles.append(pygame.image.load(path))
            i += 1
        except:
            gotAll = True
            print ('loaded '+str(len(tiles))+' tiles' )
    return tiles

def int2hx(i):
    if len(i) > 1:
        if i > 9:
            if i == 10: return 'A'
            if i == 11: return 'B'         
            if i == 12: return 'C'
            if i == 13: return 'D'
            if i == 14: return 'E'
            if i == 15: return 'F'
        return str(i)
    else:
        print('hi')

def hx2int(hx):
    if len(hx) > 1:
        x = 16**(len(hx) - 1)        
        i = hx2int(hx[1:])        
        if hx[0] in '1234567890':
            return int(hx[0]) * x + i
        if hx[0] == 'A':
            return 10 * x + i
        if hx[0] == 'B':
            return 11 * x + i
        if hx[0] == 'C':
            return 12 * x + i
        if hx[0] == 'D':
            return 13 * x + i
        if hx[0] == 'E':
            return 14 * x + i
        if hx[0] == 'F':
            return 15 * x + i

    else:
        if hx[0] in '1234567890':
            return int(hx[0])
        if hx[0] == 'A':
            return 10
        if hx[0] == 'B':
            return 11
        if hx[0] == 'C':
            return 12
        if hx[0] == 'D':
            return 13
        if hx[0] == 'E':
            return 14
        if hx[0] == 'F':
            return 15

        
def saveLevel(name,map1):
    if not os.path.exists('save//'+name+'.save'): os.makedirs('save//'+name+'.save')
    if os.path.exists("save//"+name+".save//tyMap.txt"):
        os.remove("save//"+name+".save//tyMap.txt")
        print('file dleted')
    try:
        fileName = "save//"+name+".save//tyMap.txt"
        file12 = open(fileName,'w')
    except IOError as e:
            print(fileName+" not there")
    for line in map1:
        out=''
        for i in line:
            x=hex(i)[2:]
            while len(x)<3:
                x='0'+x
            out=out+x
        file12.write(out+'\n')

"""
saveing the game
"""
def saveGame(name,backTiles):
    if not os.path.exists('save//'+name+'.save'): os.makedirs('save//'+name+'.save')
    if os.path.exists("save//"+name+".save//bace.bac//backTiles.txt"):
        os.remove("save//"+name+".save//bace.bac//backTiles.txt")
        print('file dleted')
    try:
        fileName = "save//"+name+".save//bace.bac//backTiles.txt"
        file12 = open(fileName,'w')
    except IOError as e:
            print(fileName+" not there")
    for line in backTiles:
        out=''
        for i in line:
            x=hex(i)[2:]
            while len(x)<3:
                x='0'+x
            out=out+x
        file12.write(out+'\n')

"""
new game macker
"""
     
def newGame(name):
    if  not os.path.exists("save//" + name + ".save"):
        os.makedirs('save//' + name + '.save')
        os.makedirs('save//' + name + '.save//bace.bac')
        print('yep')
        #loading the back tiles
        try:
            fileName = "save//" + name + ".save//bace.bac//backTiles.txt"
            loadFile = 'templats//0.save//bace.bac//backTiles.txt'
            f = open(fileName, 'a')
            read = open(loadFile, 'r')
            for line in read:
                f.write(line)
            f.close()
            read.close()
            print ('loadid the new back tiles')
        except IOError as e:
            print(fileName+" not there")

        #loading the vers
        try:
            fileName = "save//" + name + ".save//vers.txt"
            loadFile = 'templats//0.save//vers.txt'
            f = open(fileName, 'a')
            read = open(loadFile, 'r')
            for line in read:
                f.write(line)
            f.close()
            read.close()
            print ('loadid the new vers tiles')
        except IOError as e:
            print(fileName+" not there")
        
        
    return None



"""
loading the level
"""
"""

def loadGame(name):
    if  glob.glob("save//" + name + ".save") == None: return None
    backTiles = loadBackTiles(name)
    vers = loadVars(name)
    print('loaded game')
    return (backTiles , vers)
"""

def loadBackTiles(name):
    backTiles = []
    try:
        fileName = "save//" + name + ".save//bace.bac//backTiles.txt"
        File = open(fileName, 'r')
    except IOError as e:
            print(fileName + " not there :(")
    for line in File:
        i = 0
        x = []
        while i < len(line) - 3:
            if i % 3 == 0:
                x.append(hx2int(line[i] + line[i + 1] + line[i + 2]))
            i += 1
        backTiles.append(x)
    File.close()
    print('loaded back Tiles')
    return backTiles

def loadVars(name):
    vers=[]
    try:
        fileName = "save//"+name+".save//vers.txt"
        File = open(fileName, 'r')
    except IOError as e:
            print(fileName + " not there :(")
            return None
    for line in File:
        vers.append(int(line))
        #print int(line)
    print('loaded the verables')
    return vers

"""
scaling the tiles
"""

        
def scalTile(tiles, scale):
    tileSca = []
    for tile in tiles:
        tileSca.append(pygame.transform.smoothscale(tile, (int((tile.get_width() / 256) * scale), int((tile.get_height() / 256) * scale))))
    return tileSca


"""
a funshon to con vert milisecond to a D H M S MS string
Theo Hay
2013.3.27
"""


def msStr(intMs):
    if intMs < 1000: return str(intMs)+'ms'
    seconds = intMs // 1000
    ms = intMs % 1000
    if seconds > 59:
        minits = seconds // 60
        seconds = seconds % 60
        if minits < 60:
            return str(minits) + 'm     '+ str(seconds) + 's   ' + str(ms)+'ms'
        howers = minits // 60
        minits = minits % 60
        if howers < 24:
            return str(howers) + 'h    ' + str(minits) + 'm     ' + str(seconds) + 's   ' + str(ms)+'ms'
        days = howers // 24
        howers = howers % 24
        return str(days)+'d    '+str(howers) + 'h    ' + str(minits) + 'm     ' + str(seconds) + 's   ' + str(ms)+'ms'       
        
        

    return str(seconds) + 's   ' + str(ms)+'ms'



   
"""
       AI!
"""


def getHitBox(tiles):
    hitBox=[]

    for line in tiles:
        x=[]
        for tile in line:
            if tile == 0: x.append(False)
            if tile == 1: x.append(True)
        hitBox.append(x)
    return hitBox




def checkTile(hitBox,XY):
    if XY[0]>len(hitBox)-1: return None
    if XY[1]>len(hitBox[0])-1: return None
    if XY[0]<0: return None
    if XY[1]<0: return None

    derec=[]
    if XY[0] == 0 :
        if XY[1] == 0:
            if hitBox[XY[0]+1][XY[1]] == False :derec.append([1,0])
            if hitBox[XY[0]+1][XY[1]+1] == False :derec.append([1,1])
            if hitBox[XY[0]][XY[1]+1] == False :derec.append([0,1])
            return(derec)
        if XY[1] == len(hitBox[0])-1:
            if hitBox[XY[0]+1][XY[1]] == False :derec.append([1,0])
            if hitBox[XY[0]+1][XY[1]-1] == False :derec.append([1,-1])
            if hitBox[XY[0]][XY[1]-1] == False :derec.append([0,-1])            
            return(derec)

        if hitBox[XY[0]+1][XY[1]] == False :derec.append([1,0])
        if hitBox[XY[0]+1][XY[1]+1] == False :derec.append([1,1])
        if hitBox[XY[0]+1][XY[1]-1] == False :derec.append([1,-1])
        if hitBox[XY[0]][XY[1]+1] == False :derec.append([0,1])
        if hitBox[XY[0]][XY[1]-1] == False :derec.append([0,-1])
        return(derec)

    if XY[0] == len(hitBox)-1:
        if XY[1] == 0:
            if hitBox[XY[0]-1][XY[1]] == False :derec.append([-1,0])
            if hitBox[XY[0]-1][XY[1]+1] == False :derec.append([-1,1])
            if hitBox[XY[0]][XY[1]+1] == False :derec.append([0,1])
            return(derec)

        if XY[1] == len(hitBox[0])-1:
            if hitBox[XY[0]-1][XY[1]] == False :derec.append([-1,0])
            if hitBox[XY[0]-1][XY[1]-1] == False :derec.append([-1,-1])
            if hitBox[XY[0]][XY[1]-1] == False :derec.append([0,-1])
            return(derec)


        if hitBox[XY[0]-1][XY[1]] == False :derec.append([-1,0])
        if hitBox[XY[0]-1][XY[1]+1] == False :derec.append([-1,1])
        if hitBox[XY[0]-1][XY[1]-1] == False :derec.append([-1,-1])
        if hitBox[XY[0]][XY[1]+1] == False :derec.append([0,1])
        if hitBox[XY[0]][XY[1]-1] == False :derec.append([0,-1])
        return(derec)



    if hitBox[XY[0]+1][XY[1]] == False :derec.append([1,0])
    if hitBox[XY[0]+1][XY[1]+1] == False :derec.append([1,1])
    if hitBox[XY[0]+1][XY[1]-1] == False :derec.append([1,-1])
    if hitBox[XY[0]-1][XY[1]] == False :derec.append([-1,0])
    if hitBox[XY[0]-1][XY[1]+1] == False :derec.append([-1,1])
    if hitBox[XY[0]-1][XY[1]-1] == False :derec.append([-1,-1])
    if hitBox[XY[0]][XY[1]+1] == False :derec.append([0,1])
    if hitBox[XY[0]][XY[1]-1] == False :derec.append([0,-1])
    return(derec)




