"""
This is where we create controls for the player
"""
#Imports
import keyboard
import pygame
from Constants import *

#Var
focusMode = False

#Controls
class Player:
    def __init__(self):
        self.playerX = 350 #    These are
        self.playerY = 350 # Start Positions
        self.playerHp = 3 #What health we player starts at
        self.playerHearts = pygame.image.load("Images/h3.png")
        self.appearence = pygame.image.load("Images/character.png")
        
    def playerMovement(self):
        def moveRight(self):
            if ((keyboard.is_pressed('right') or keyboard.is_pressed('d')) and self.playerX < 690.5):
                if (keyboard.is_pressed('shift')):
                    self.playerX += (PLAYER_SPEED * FPS_CAP) / 2
                    
                else:
                    self.playerX += (PLAYER_SPEED * FPS_CAP)
                
        def moveLeft(self):
            if ((keyboard.is_pressed('left') or keyboard.is_pressed('a')) and self.playerX > -11):
                if (keyboard.is_pressed('shift')):
                    self.playerX -= (PLAYER_SPEED * FPS_CAP) / 2
                    
                else:
                    self.playerX -= PLAYER_SPEED * FPS_CAP      

        def moveUp(self):
            if ((keyboard.is_pressed('up') or keyboard.is_pressed('w')) and self.playerY > -9):
                if (keyboard.is_pressed('shift')):
                    self.playerY -= (PLAYER_SPEED * FPS_CAP) / 2
                    
                else:
                    self.playerY -= PLAYER_SPEED * FPS_CAP
            
        def moveDown(self):       
            if ((keyboard.is_pressed('down') or keyboard.is_pressed('s')) and self.playerY < 690.5):
                if (keyboard.is_pressed('shift')):
                    self.playerY += (PLAYER_SPEED * FPS_CAP) / 2
                    
                else:
                    self.playerY += PLAYER_SPEED * FPS_CAP
                    
        moveRight(self)
        moveLeft(self)
        moveUp(self)
        moveDown(self)
        
    def focusModeOn(self):
        if (keyboard.is_pressed('shift')):
            self.character = pygame.image.load("Images/characterFocus.png")
        else:
            self.character = pygame.image.load("Images/character.png")
        
        
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
            
            
    def characterHitBoxDraw(self):
        self.hitbox = (self.playerX + HITBOX_OFFSET, self.playerY + HITBOX_OFFSET, 13, 13)
        self.playerRect = pygame.Rect(self.hitbox)