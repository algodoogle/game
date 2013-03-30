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
        self.menu =  pygame.image.load("main_menu_1_v3.png")
        self.buttonPlay = button((100,100), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonOnline = button((400,100), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonSantum = button((100,300), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonOptions = button((100,500), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonAddons = button((400,500), 350, 150, pygame.image.load('buttom_1.png'))
        self.buttonExit = button((100,700), 350, 150, pygame.image.load('buttom_1.png'))


        
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
        self.buttonExit.draw(screen)
        



    def getClick(self, XY):
        if self.buttonPlay.click(XY): return 'play'
        if self.buttonOnline.click(XY): return 'online'
        if self.buttonSantum.click(XY): return 'santum'
        if self.buttonOptions.click(XY): return 'options'
        if self.buttonAddons.click(XY): return 'addons'
        if self.buttonExit.click(XY): return 'exit'
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
