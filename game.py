"""
Theo Hay
"""


#imports :)
import pygame, string, glob, os, random, pygame.locals

#importing my classes and funchons
from funshion import *
from set_up import setUp
from menuClass import *


"""
loading the mane menu and set up
"""
#loading the screen and other set up stuff
time, screen, screnRes = setUp()
menu = mainMenu(screnRes)

#loading the sprights
tiles = loadSprites()

#enishalisign the cor verdales

end = False
inGame = False
scroling = False
framecount = 0
soconds = 0
gameName = 'test'
#screen = pygame.display.set_mode(screnRes,FULLSCREEN)
screen = pygame.display.set_mode(screnRes)
click = False


"""
mane loop this shoud onle end when the plaer closis the game 
"""
menu = mainMenu(screnRes)
gameName = 'test'
while not end:
    #this the where the menu shoud be there is a lot of tems stuf heir for now

    #geting the in puts
    for i in pygame.event.get():
        if i.type is QUIT:
            end = True
            inGame = False
        if i.type is MOUSEMOTION:
            mousePos = i.pos
        if i.type is MOUSEBUTTONDOWN and i.button == 1:
            click = True
        if i.type is MOUSEBUTTONUP and i.button == 1: click = False



    menu.draw(screen)

    if click:
        i = menu.getClick(mousePos)
        click = False
        if i == 'play': inGame = True
        if i == 'exit':  end = True


    pygame.display.flip()
    framecount += 1
    if 1000*soconds < pygame.time.get_ticks():
            fps = framecount
            framecount = 0
            print('fps: ' + str(fps) + ';     run time: ' + msStr(pygame.time.get_ticks()) + ';')
            soconds += 1
    
    if inGame:
        avrRenderTime = 0
        renderCount = 0

        
        mousePos=[0,0]
        level = world(gameName)
        level.load()
        dispMenu = False
        tileSca = scalTile(tiles,level.scale)
        render = True
        buttom1 = button((100,100), 350, 150, pygame.image.load('buttom_1.png'))
    while inGame:

        




        for i in pygame.event.get():
            #print(i)            
            if i.type is QUIT:
                end = True
                inGame = False
            if i.type is KEYDOWN and i.key == 27:
                if dispMenu == True: dispMenu = False
                else: dispMenu = True
                render = True

            if i.type is MOUSEBUTTONDOWN and i.button == 3: scroling = True
            if i.type is MOUSEBUTTONUP and i.button == 3: scroling = False
            if scroling == True and i.type is MOUSEMOTION:
                level.screenOffSet[0] = level.screenOffSet[0] - i.rel[0]
                level.screenOffSet[1] = level.screenOffSet[1] - i.rel[1]
                render = True     
                while level.screenOffSet[0] > level.scale:
                    level.screenOffSet[0] = level.screenOffSet[0] - level.scale
                    level.screenPos[0] += 1
                while level.screenOffSet[1] > level.scale:
                    level.screenOffSet[1] = level.screenOffSet[1] - level.scale
                    level.screenPos[1] += 1             
                while level.screenOffSet[0] < 0:
                    level.screenOffSet[0] = level.screenOffSet[0] + level.scale
                    level.screenPos[0] -= 1
                while level.screenOffSet[1] < 0:
                    level.screenOffSet[1] = level.screenOffSet[1] + level.scale
                    level.screenPos[1] -= 1                
            if i.type is MOUSEBUTTONDOWN and i.button == 1:
                click = True
                render = True
            if i.type is MOUSEBUTTONUP and i.button == 1: click = False  
            if i.type is MOUSEBUTTONDOWN and i.button == 4:
                render = True
                scaleCha = int(level.scale)
                level.scale = level.scale + int(level.scale / 10 + 1)
                if level.scale > 256: level.scale = 256
                tileSca = scalTile(tiles,level.scale)
                level.screenOffSet[0] = level.screenOffSet[0] + int((level.scale - scaleCha) * (mousePos[0] / scaleCha))
                level.screenOffSet[1] = level.screenOffSet[1] + int((level.scale - scaleCha) * (mousePos[1] / scaleCha))                
            if i.type is MOUSEBUTTONDOWN and i.button == 5:
                render = True
                scaleCha = int(level.scale)
                level.scale = level.scale - int(level.scale / 10 + 1)
                if level.scale < 8: level.scale = 8
                tileSca = scalTile(tiles,level.scale)
                level.screenOffSet[0] = level.screenOffSet[0] - int((scaleCha - level.scale) * (mousePos[0] / scaleCha))
                level.screenOffSet[1] = level.screenOffSet[1] - int((scaleCha - level.scale) * (mousePos[1] / scaleCha))
            if i.type is MOUSEMOTION:
                mousePos = i.pos
                render = True


  

        
        if render:
            renTime = pygame.time.get_ticks() 
            if click:
                if dispMenu == True:
                    if buttom1.click(mousePos):
                        end = True
                        inGame = False

                            

                level.toggel(mousePos)
                click = False 

            render = False
            level.checkOK(screnRes)
            RENNUM = 0
            H = 0
            while H < screnRes [1] / level.scale + 2:
                W = 0
                while W < screnRes[0] / level.scale + 1:
                    RENNUM += 1
                    tile = tileSca[ level.backTiles[(level.screenPos[1]) + H] [(level.screenPos[0]) + W]]
                    screen.blit( tile,(W * level.scale - level.screenOffSet[0], H * level.scale - level.screenOffSet[1]))
                    W+=1
                H+=1


                
            if dispMenu == True:
                buttom1.draw(screen)


            pygame.display.flip()
            avrRenderTime +=  pygame.time.get_ticks() - renTime  
            renderCount += 1
            


        #print (framecount,0)
        #print (checkTile(hitBox,[framecount,0]))
        
        framecount += 1
        if 1000*soconds < pygame.time.get_ticks():
            if renderCount > 0 :
                print(avrRenderTime/renderCount)
                print (1000/(avrRenderTime/renderCount))
            avrRenderTime = 0
            renderCount = 0

            
            fps = framecount
            framecount = 0
            print('fps: ' + str(fps) + ';    displad tiles: ' + str(RENNUM) + ';     run time: ' + msStr(pygame.time.get_ticks()) + ';')
            soconds += 1

        if not inGame:
            saveGame(gameName, level.backTiles)
pygame.quit ()
