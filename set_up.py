"""
sets up uthe the screen
Theo Hay
30/3/2013
"""
import pygame, pygame.locals

def setUp():
    time=pygame.time.Clock()
    screen = pygame.display.set_mode((640, 360),32)
    screen.blit(pygame.transform.smoothscale((pygame.image.load("splash screen.png")), (640,360)),(0,0))
    pygame.display.flip()


    modes = pygame.display.list_modes(32)
    if not modes:
        print ('32bit not supported')
        modes = pygame.display.list_modes(16)
        if not modes:
            print ('16bit not supported')
            print ('Set Resolution: 640, 480')
            modes = [(640, 480), ()]
    screenRes = modes[1]#                                                     temp for testing shoud be       screnRes = modes[0]
    #screenRes = (5000,1000)
    print('set Set Resolution: ' + str(screenRes[0]) + ' ' + str(screenRes[1]))

    print('start up: ' + str(pygame.time.get_ticks() / 1000) + 's')


    return time, screen, screenRes

