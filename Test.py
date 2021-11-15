'''
Testing file; no need to wrry abt
'''

import pygame

screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
pygame.init()
pygame.display.init()
while True:
    pygame.mouse.set_pos(0, 0)
    print(pygame.mouse.get_pos())
    
    pygame.display.update()