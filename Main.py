'''
Where the game is run
'''

#Imports
import pygame
import keyboard
from time import sleep, time

from PlayerClass import *
from EnemyFile import *
from  TheWorld import *

#Bruh
pygame.init()

#Variables
gamer = Player()
stage = World(0)

angle = 1

width = 1080
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("NIGHTMARE NIGHTMARE NIGHTMARE")
clock = pygame.time.Clock()

#Images
menu = pygame.image.load("Images/menu.png")
sideScreen = pygame.image.load("Images/sideScreen.png")
sword = pygame.image.load("Images/sword.png")


def main():
    #Keep at top
    gameRunning = True
    playerWantClose()
    
    while gameRunning:
        #keep at top of gameRunning
        playerWantClose()
        
        #Controls
        gamer.playerMovement()
        gamer.focusModeOn()
        #print(pygame.mouse.get_pos())
        
        worldChangeVar = stage.worldChange(gamer.hitbox, gamer.playerX, gamer.playerY)
        if worldChangeVar == "bot":
            gamer.playerY = 630
        elif worldChangeVar == "top":
            gamer.playerY = 60
        elif worldChangeVar == "left":
            gamer.playerX = 60
        elif worldChangeVar == "right":
            gamer.playerX = 620
        stage.worldImage()
            
        #print(stage.area)
        gamer.subHealth()
        
        #Meeeenu
        screen.blit(menu, (0, 0))
        
        
        #Refresh    
        worldChangeVar = stage.worldChange(gamer.hitbox, gamer.playerX, gamer.playerY)
        if worldChangeVar == "bot":
            gamer.playerY = 630
        elif worldChangeVar == "top":
            gamer.playerY = 60
        elif worldChangeVar == "left":
            gamer.playerX = 60
        elif worldChangeVar == "right":
            gamer.playerX = 620
        stage.worldImage()
        screen.blit(stage.appearence, (0, 0))
        
        #pygame.draw.rect(screen, (255, 0 ,0), gamer.swordHitZone, 2) #Draws sword hitzone, unneeded but useful for testing enemy damage range
        screen.blit(gamer.appearence, (gamer.playerX, gamer.playerY))
        gamer.characterHitBoxDraw()
        if gamer.attackCoolDown != 0:
            gamer.meleeSwordDraw()
            screen.blit(gamer.swordRotation, (gamer.swordRotsX, gamer.swordRotsY))
        
        
             #These need to be at the end of draw since they're at the top
        if (keyboard.is_pressed('tab') and (stage.area == 0)):
            screen.blit(menu, (0, 0))
            menuOpen = True
        else:
            menuOpen = False
        
        gamer.drawHealth()
        screen.blit(sideScreen, (0, 0))
        screen.blit(gamer.playerHearts, (0, 0))
        pygame.draw.rect(screen,(255, 255, 255), (gamer.attackAllowedBar))
        #pygame.draw.rect(screen,(255, 0, 0), (gamer.attackAllowedZone), 2)
        gamer.allowedBarMovement()
        gamer.playerAttack()
        
        
        clock.tick(60)
        pygame.event.wait(1)
        pygame.display.update()
        pygame.display.flip()
    
#Other Functions
def playerWantClose():
    if (keyboard.is_pressed('esc')):
        print("closing")
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()