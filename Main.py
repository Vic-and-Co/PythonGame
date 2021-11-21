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

#Enemy Classes
mEnemy1 = MeleeType(100, 100, 0, 1)
mEnemy2 = MeleeType(100, 100, 0, 2)
mEnemy3 = MeleeType(100, 100, 0, 3)
mEnemy4 = MeleeType(100, 100, 0, 4)
mBoss = MeleeType(100, 100, 0, 5)


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
        worldChangeVar = theWorld.worldChange(gamer.hitbox, gamer.playerX, gamer.playerY, mBoss.boss1Dead)
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
        if gamer.focusModeOn(): pygame.draw.rect(screen, (255, 0 ,0), gamer.swordHitZone, 2) #Draws Hit Zone if Shift
        
        if theWorld.area == 0:
            gamer.playerHp = 3
        
        #Enemy Spawning Stage 1
        if (theWorld.worldEnemySpawn()):
            if not theWorld.stage1Enemy1Spawned: #Spawn Melee Enemy 1
                mEnemy1.health = 3
                mEnemy1.eX = 100
                mEnemy1.eY = 100
                
                if gamer.playerX <= 615:
                    theWorld.stage1Enemy1Spawned = True
            
            if mEnemy1.health == 0: #Spawn Melee Enemy 2
                mEnemy1.health -= 1
                
                theWorld.stage1Enemy2Spawned = True
                mEnemy2.health = 3
                mEnemy2.eX = 620
                mEnemy2.eY = 100
            
            if theWorld.stage1Enemy2Spawned and mEnemy2.health == 0: #Spawn Melee Enemy 3
                mEnemy2.health -= 1
                
                theWorld.stage1Enemy3Spawned = True
                mEnemy3.health = 3
                mEnemy3.eX = 100
                mEnemy3.eY = 620
            
            if theWorld.stage1Enemy3Spawned and mEnemy3.health == 0: #Spawn Melee Enemy 4
                mEnemy3.health -= 1
                
                theWorld.stage1Enemy4Spawned = True
                mEnemy4.health = 3
                mEnemy4.eX = 620
                mEnemy4.eY = 620
            
            if theWorld.stage1Enemy4Spawned and mEnemy4.health == 0: #Spawn Melee Boss
                mEnemy4.health -= 1
                
                theWorld.stage1BossSpawned = True
                mBoss.health = 3
                mBoss.eX = 350
                mBoss.eY = 350
            
            if theWorld.stage1BossSpawned and mBoss.health <= 0: #Relays if boss1 dead
                theWorld.stage1Done = True
                        
            mEnemy1.characterHitBoxUpdate()
            mEnemy1.checkHealth()
            mEnemy1.movement(gamer.playerX, gamer.playerY)
            mEnemy1.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
            
            mEnemy2.characterHitBoxUpdate()
            mEnemy2.checkHealth()
            mEnemy2.movement(gamer.playerX, gamer.playerY)
            mEnemy2.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
        
            mEnemy3.characterHitBoxUpdate()
            mEnemy3.checkHealth()
            mEnemy3.movement(gamer.playerX, gamer.playerY)
            mEnemy3.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
            
            mEnemy4.characterHitBoxUpdate()
            mEnemy4.checkHealth()
            mEnemy4.movement(gamer.playerX, gamer.playerY)
            mEnemy4.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
            
            mBoss.characterHitBoxUpdate()
            mBoss.checkHealth()
            mBoss.movement(gamer.playerX, gamer.playerY)
            mBoss.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
            
            
            gamer.takeDamage(mEnemy1.hitbox, mEnemy1.isAlive())
            gamer.takeDamage(mEnemy2.hitbox, mEnemy2.isAlive())
            gamer.takeDamage(mEnemy3.hitbox, mEnemy3.isAlive())
            gamer.takeDamage(mEnemy4.hitbox, mEnemy4.isAlive())
            gamer.takeDamage(mBoss.hitbox, mBoss.isAlive())
                
            screen.blit(mEnemy1.appearence, (mEnemy1.eX, mEnemy1.eY))
            screen.blit(mEnemy2.appearence, (mEnemy2.eX, mEnemy2.eY))
            screen.blit(mEnemy3.appearence, (mEnemy3.eX, mEnemy3.eY))
            screen.blit(mEnemy4.appearence, (mEnemy4.eX, mEnemy4.eY))
            screen.blit(mBoss.appearence, (mBoss.eX, mBoss.eY))
    
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