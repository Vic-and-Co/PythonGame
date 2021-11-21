'''
Where the game is run
'''

#Imports
import pygame
import keyboard
from time import sleep, time
import random
from threading import Timer

from PlayerClass import *
from EnemyFile import *
from  TheWorld import *


#Bruh
pygame.init()

#Variables

angle = 1

width = 1080
height = 720

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Images
menu = pygame.image.load("Images/menu.png")
sideScreen = pygame.image.load("Images/sideScreen.png")
sword = pygame.image.load("Images/sword.png")
redScreen = pygame.image.load("Images/dead.png")

#Class Instances
meleeEnemyList = []
gamer = Player()
nongamer = MeleeType(100, 100, 2)
nongamer.health = 0

theWorld = World(0)


def main():
    #Keep at top
    gameRunning = True
    playerWantClose()
    
    pygame.display.set_caption(randomName())
    
    
    while gameRunning:
        #keep at top of gameRunning
        playerWantClose()
        
        #Meeeenu
        screen.blit(menu, (0, 0))
    
        #These need to be at the end of draw since they're at the top
        if (keyboard.is_pressed('tab') and (theWorld.area == 0)):
            screen.blit(menu, (0, 0))
            menuOpen = True
        else:
            menuOpen = False
        
        
        screen.blit(sideScreen, (0, 0))
        screen.blit(gamer.playerHearts, (0, 0))
        
        pygame.draw.rect(screen,(255, 255, 255), (gamer.attackAllowedBar))
        #pygame.draw.rect(screen,(255, 0, 0), (gamer.attackAllowedZone), 2)

        #World
        worldChangeVar = theWorld.worldChange(gamer.hitbox, gamer.playerX, gamer.playerY)
        if worldChangeVar == "bot":
            gamer.playerY = 630
        elif worldChangeVar == "top":
            gamer.playerY = 60
        elif worldChangeVar == "left":
            gamer.playerX = 60
        elif worldChangeVar == "right":
            gamer.playerX = 620
        theWorld.worldImage()
        screen.blit(theWorld.appearence, (0, 0))

        #Player
        #print(gamer.damageCoolDown)
        gamer.playerMovement()
        gamer.focusModeOn()
        gamer.drawHealth()
        gamer.allowedBarMovement()
        gamer.playerAttack()
        screen.blit(gamer.appearence, (gamer.playerX, gamer.playerY))
        gamer.characterHitBoxDraw()
        
        if gamer.attackCoolDown != 0:
            gamer.meleeSwordDraw()
            screen.blit(gamer.swordRotation, (gamer.swordRotsX, gamer.swordRotsY))
        pygame.draw.rect(screen, (255, 0 ,0), gamer.swordHitZone, 2) #Draws sword hitzone, unneeded but useful for testing enemy damage range
        
        if theWorld.area == 0:
            gamer.playerHp = 3
        
        #Enemy Spawning Stage 1
        if (theWorld.worldEnemySpawn()):
            if not theWorld.stage1EnemiesSpawned:
                nongamer.health = 3
                nongamer.eX = 100
                nongamer.eY = 100
                if gamer.playerX <= 615:
                    theWorld.stage1EnemiesSpawned = True
            nongamer.characterHitBoxUpdate()
            nongamer.movement(gamer.playerX, gamer.playerY)
            nongamer.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
            gamer.takeDamage(nongamer.hitbox, nongamer.isAlive())
            screen.blit(nongamer.appearence, (nongamer.eX, nongamer.eY))
    
        #Death Check
        if gamer.checkDead():
            screen.blit(redScreen, (0, 0))
            gameRunning = False
            
        #Player Class Stuff that takes enemy arg
        clock.tick(60)
        pygame.event.wait(1)
        pygame.display.update()
        pygame.display.flip()
    
    while not gameRunning:
        playerWantClose()
                                                                                                                                                                                              
#Other Functions
def playerWantClose():
    if (keyboard.is_pressed('esc')):
        print("closing")
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
def randomName():
    titleNum = random.randint(1,11)
    if titleNum == 1:
        return "NIGHTMARE NIGHTMARE NIGHTMARE"
    elif titleNum == 2:
        return "Epic rpg bossfight simulator"
    elif titleNum == 3:
        return "run, now"
    elif titleNum == 4:
        return "Sponsered by my tears"
    elif titleNum == 5:
        return "The Older Writings"
    elif titleNum == 6:
        return "Game Child"
    elif titleNum == 7:
        return "Made in Chinor"
    elif titleNum == 8:
        return "Chewing Chum"
    elif titleNum == 9:
        return "Xx_EPIC_GAMER_2440_xX"
    elif titleNum == 10:
        return "Strohm Bot 2000.exe VER.3 (In Progress)"
    elif titleNum == 11:
        return "Top 10 Greatest"