'''
The world class: dictates the stages/ areas
'''
import pygame

class World:
    def __init__(self, area):
        self.area = area #0 pertains to starting area, other stages are their individual stage numbers
        
        #Detection Boundaries
        self.upSquare = pygame.Rect(255, 0, 209, 30)
        
    def worldChange(self, playerHitBox, playerX, playerY):
        if pygame.Rect.colliderect(self.upSquare, playerHitBox) and self.area == 0:
            self.area = 2
            playerX = 350
            playerY = 350