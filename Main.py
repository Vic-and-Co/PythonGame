'''
Where the game is run
'''

#Imports
import pygame
import keyboard
from time import sleep, time

from Controls import *
from PlayerStats import *

#Bruh
pygame.init()

#Variables
controls = Control()
playerStats = PlayStatistics()

width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
area = 0 #0 refers to start area, other numbers correspond to their respective stages

clock = pygame.time.Clock()

#Images
startArea = pygame.image.load("Images/Start Area.png")
character = pygame.image.load("Images/character.png")
menu = pygame.image.load("Images/menu.png")
sideScreen = pygame.image.load("Images/sideScreen.png")

amog = pygame.image.load("Images/character.png")

characterHitBox = pygame.image.load("Images/charHitBox.png")

def main():
    gameRunning = True
    
    
    pygame.mouse.set_pos(0, 0)
    while gameRunning:
        #Keep at top
        if (keyboard.is_pressed('esc')):
            print("closing")
            gameRunning = False
            exit()
            
            
        #Controls
        controls.playerMovement()
        
        if (keyboard.is_pressed('shift')):
            character = pygame.image.load("Images/characterFocus.png")
        else:
            character = pygame.image.load("Images/character.png")
        
        if (keyboard.is_pressed('a')):
            pass
        screen.blit(menu, (0, 0))
        
        
        # if (keyboard.is_pressed('f')):
        #     playerStats.subHealth()
            

        

        #Refresh
        print(playerStats.playerHp)
        
        screen.blit(startArea, (0, 0))
        screen.blit(character, (controls.playerX, controls.playerY))
        screen.blit(amog, (30, 30))
        #screen.blit(characterHitBox, (controls.playerX + HITBOX_OFFSET, controls.playerY + HITBOX_OFFSET))
        characterHitBoxDraw()
        
             #These need to be at the end of draw since they're at the top
        if (keyboard.is_pressed('tab') and (area == 0)):
            screen.blit(menu, (0, 0))
        
        playerStats.drawHealth()
        screen.blit(sideScreen, (0, 0))
        screen.blit(playerStats.playerHearts, (0, 0))
        
        
        clock.tick(60)
        pygame.display.update()
    
#Other Functions
def characterHitBoxDraw():
    hitbox = (controls.playerX + HITBOX_OFFSET, controls.playerY + HITBOX_OFFSET, 13, 13)
    testRect = pygame.Rect(30, 30, 13, 13)
    playerRect = pygame.Rect(hitbox)
    
    
    if (pygame.Rect.colliderect(playerRect, testRect)): #ends game when test rect and player hitbox touches
        exit()

if __name__ == "__main__":
    main()