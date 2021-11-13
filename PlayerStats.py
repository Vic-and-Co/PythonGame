'''
Health and Super energy
'''

#Imports
import keyboard
import pygame
from Constants import *

#Var



#Stats
class PlayStatistics:
    def __init__(self):
        self.playerHp = 3 #What health we player starts at
        self.playerHearts = pygame.image.load("Images/h3.png")
    
    def addHealth(self):
        if (self.playerHp < 3):
            self.playerHp += 1
        
    def subHealth(self):
        if (self.playerHp > 0):
            self.playerHp -= 1
    
    def drawHealth(self):
        if (self.playerHp == 3):
            self.playerHearts = pygame.image.load("Images/h3.png")
        
        elif (self.playerHp == 2):
            self.playerHearts = pygame.image.load("Images/h2.png")
            
        elif (self.playerHp == 1):
            self.playerHearts = pygame.image.load("Images/h1.png")
            
        elif (self.playerHp == 0):
            self.playerHearts = pygame.image.load("Images/blank.png")