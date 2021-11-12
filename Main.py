'''
Where the game is run
'''

#Imports
import pygame
import keyboard
from time import sleep
from Controls import Control

#Bruh
pygame.init()

#Variables
width = 720
height = 720
playerSpeed = 0.4

#Images
startArea = pygame.image.load("Images/Start Area.png")
character = pygame.image.load("Images/character.png")

controls = Control()

def main():
    gameRunning = True
    screen = pygame.display.set_mode((width, height))
    while gameRunning:
        #Controls
        controls.moveX()
        controls.moveY()
        
        if (keyboard.is_pressed('esc')):
            gameRunning = False
            exit()
        
        
        screen.blit(startArea, (0, 0))
        screen.blit(character, (controls.playerX, controls.playerY))
        
        
        #Refresh
        pygame.display.update()
    

if __name__ == "__main__":
    main()