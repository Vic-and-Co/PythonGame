"""
This is where we create controls for the player
"""
#Imports
import keyboard
from Constants import *

#Controls
class Control:
    def __init__(self):
        self.playerX = 350 #    These are
        self.playerY = 350 # Start Positions
        
    def moveX(self):
        global playerX
        if (keyboard.is_pressed('right') or keyboard.is_pressed('d')):
            self.playerX += PLAYER_SPEED
        elif (keyboard.is_pressed('left') or keyboard.is_pressed('a')):
            self.playerX -= PLAYER_SPEED

    def moveY(self):
        global playerY
        if (keyboard.is_pressed('up') or keyboard.is_pressed('w')):
            self.playerY -= PLAYER_SPEED
        elif (keyboard.is_pressed('down') or keyboard.is_pressed('s')):
            self.playerY += PLAYER_SPEED
