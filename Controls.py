"""
This is where we create controls for the player
"""
#Imports
import keyboard
import pygame
from Constants import *

#Var
clock = pygame.time.Clock()
fpsCap = clock.tick(60)
focusMode = False

#Controls
class Control:
    def __init__(self):
        self.playerX = 350 #    These are
        self.playerY = 350 # Start Positions
        
    def playerMovement(self):
        def moveRight(self):
            if ((keyboard.is_pressed('right') or keyboard.is_pressed('d')) and self.playerX < 690.5):
                if (keyboard.is_pressed('shift')):
                    self.playerX += (PLAYER_SPEED * fpsCap) / 2
                    
                else:
                    self.playerX += (PLAYER_SPEED * fpsCap)
                
        def moveLeft(self):
            if ((keyboard.is_pressed('left') or keyboard.is_pressed('a')) and self.playerX > -11):
                if (keyboard.is_pressed('shift')):
                    self.playerX -= (PLAYER_SPEED * fpsCap) / 2
                    
                else:
                    self.playerX -= PLAYER_SPEED * fpsCap      

        def moveUp(self):
            if ((keyboard.is_pressed('up') or keyboard.is_pressed('w')) and self.playerY > -9):
                if (keyboard.is_pressed('shift')):
                    self.playerY -= (PLAYER_SPEED * fpsCap) / 2
                    
                else:
                    self.playerY -= PLAYER_SPEED * fpsCap
            
        def moveDown(self):       
            if ((keyboard.is_pressed('down') or keyboard.is_pressed('s')) and self.playerY < 690.5):
                if (keyboard.is_pressed('shift')):
                    self.playerY += (PLAYER_SPEED * fpsCap) / 2
                    
                else:
                    self.playerY += PLAYER_SPEED * fpsCap
                    
        moveRight(self)
        moveLeft(self)
        moveUp(self)
        moveDown(self)