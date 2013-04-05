"""
menu class
Theo Hay
29/3/2013
"""

import pygame, string, glob, os, pygame.locals
from funshion import *


class mainMenu:
    def __init__(self, screenRes):
        self.res = screenRes
        self.backIM = pygame.image.load("menu_tile_v1.png")
<<<<<<< HEAD
        self.menu =  pygame.image.load("mane_menu//main_menu_base_v3.png")
        #self.buttonPlay = button((100,100), 350, 150, pygame.image.load('buttom_1.png'))
        #self.buttonOnline = button((400,100), 350, 150, pygame.image.load('buttom_1.png'))
        #self.buttonSantum = button((100,300), 350, 150, pygame.image.load('buttom_1.png'))
        #self.buttonOptions = button((100,500), 350, 150, pygame.image.load('buttom_1.png'))
        #self.buttonAddons = button((400,500), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonExit = button((0,680), 350, 150, pygame.image.load('mane_menu//Button_9.png'), pygame.image.load('mane_menu//Button_10.png'))
=======
        self.menu =  pygame.image.load("main_menu_1_v3.png")
        self.buttonPlay = button((100,100), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonOnline = button((400,100), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonSantum = button((100,300), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonOptions = button((100,500), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonAddons = button((400,500), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonExit = button((100,700), 350, 150, pygame.image.load('buttom_1.png'))
>>>>>>> adb13081fcc21070d297d3db8410f3f72ae44ab4


        
        #tiling the background
        if not self.backIM.get_size() == self.res:
            backIM = self.backIM
            W = 0
            H = 0
            self.backIM = pygame.Surface(self.res)
            while H < self.res[0]:
                while W < self.res[1]:
                    self.backIM.blit(backIM, [H, W])
                    W += backIM.get_size()[1]
                W = 0
                H += backIM.get_size()[0]

        #macking the rest of the grafix worck :) 
        if not self.menu.get_size() == self.res:
<<<<<<< HEAD
            size = self.menu.get_size()
            dif1 = self.res[0]/size[0]
            dif2 = self.res[1]/size[1]
            print (dif1,dif2)
            if dif1 > dif2:
                print (round(size[0]*dif2), round(size[1]*dif2))
                self.menu = pygame.transform.smoothscale(self.menu, (round(size[0]*dif2), round(size[1]*dif2)))
                self.buttonExit.scal(dif2)
                self.buttonExit.XY = (0, round(1639*dif2))
            else:
                print(self.buttonExit.XY)
                print (round(size[0]*dif1), round(size[1]*dif1))
                self.buttonExit.scal(dif1)
                self.buttonExit.XY = (0, round(1639*dif1))
                self.menu = pygame.transform.smoothscale(self.menu, (round(size[0]*dif1), round(size[1]*dif1)))

                            
    def draw(self, screen, XY):
        #check the overs
        #self.buttonPlay.over(XY)
        #self.buttonOnline.over(XY)
        #self.buttonSantum.over(XY)
        #self.buttonOptions.over(XY)
        #self.buttonAddons.over(XY)
        self.buttonExit.over(XY)
        #bliting to the screen
        screen.blit(self.backIM, (0,0))
        screen.blit(self.menu, (0,0))
        #self.buttonPlay.draw(screen)
        #self.buttonOnline.draw(screen)
        #self.buttonSantum.draw(screen)
        #self.buttonOptions.draw(screen)
        #self.buttonAddons.draw(screen)
=======
            i = self.res[1]/9
            self.menu = pygame.transform.smoothscale(self.menu, (int(16*i), self.res[1]))

                        
    def draw(self, screen):
        screen.blit(self.backIM, (0,0))
        screen.blit(self.menu, (0,0))
        self.buttonPlay.draw(screen)
        self.buttonOnline.draw(screen)
        self.buttonSantum.draw(screen)
        self.buttonOptions.draw(screen)
        self.buttonAddons.draw(screen)
>>>>>>> adb13081fcc21070d297d3db8410f3f72ae44ab4
        self.buttonExit.draw(screen)
        



    def getClick(self, XY):
<<<<<<< HEAD
        #if self.buttonPlay.click(XY): return 'play'
        #if self.buttonOnline.click(XY): return 'online'
        #if self.buttonSantum.click(XY): return 'santum'
        #if self.buttonOptions.click(XY): return 'options'
        #if self.buttonAddons.click(XY): return 'addons'
        if self.buttonExit.click(XY): return 'play'
=======
        if self.buttonPlay.click(XY): return 'play'
        if self.buttonOnline.click(XY): return 'online'
        if self.buttonSantum.click(XY): return 'santum'
        if self.buttonOptions.click(XY): return 'options'
        if self.buttonAddons.click(XY): return 'addons'
        if self.buttonExit.click(XY): return 'exit'
>>>>>>> adb13081fcc21070d297d3db8410f3f72ae44ab4
        return None
        
    
                
                




"""
res=[1600,900]
screen = pygame.display.set_mode(res)

menu = mainMenu(res)
print( menu.getClick([101,101]) )
print( menu.getClick([101,501]) )
menu.draw(screen)
pygame.display.flip()

pygame.quit()
"""
