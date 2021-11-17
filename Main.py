'''
Where the game is run
'''

#Imports
import pygame
import keyboard
import mouse
from time import sleep, time

from PlayerClass import *
from EnemyFile import *
from  TheWorld import *

#Bruh
pygame.init()

#Variables
gamer = Player()
dummy = MeleeType(700, 200)
stage = World(0)

angle = 1

width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
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
            
        print(stage.area)
        
        #Meeeenu
        screen.blit(menu, (0, 0))
        
        #Dumb Eggies' Movement
        dummy.goTowardsPlayerX(gamer.playerX)
        dummy.goTowardsPlayerY(gamer.playerY)
        
        #Refresh    
        screen.blit(stage.appearence, (0, 0))
        pygame.draw.rect(screen, (255, 0 ,0), gamer.swordHitZone, 2) #Will change location, draws red character hitbox
        screen.blit(gamer.appearence, (gamer.playerX, gamer.playerY))
        screen.blit(dummy.appearence, (dummy.eX, dummy.eY))
        gamer.characterHitBoxDraw()
        dummy.characterHitBoxUpdate()
        
        pygame.draw.rect(screen,(255, 0, 0), (dummy.eX, dummy.eY, dummy.rectX, dummy.rectY), 2)
        
        pygame.draw.rect(screen, (255, 0, 0), stage.upSquare, 2)
        pygame.draw.rect(screen, (255, 0, 0), stage.downSquare, 2)
        pygame.draw.rect(screen, (255, 0, 0), stage.leftSquare, 2)
        pygame.draw.rect(screen, (255, 0, 0), stage.rightSquare, 2)
        
        dummy.isPlayerAttack(gamer.swordHitZone, gamer.attackAllowed)
        
        meleeSwordDraw()
        
        
        # if pygame.Rect.colliderect(dummy.hitbox, gamer.swordHitZone):
        #     print(True)
        #     exit()
        
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
        gamer.allowedToAttack()
        
        
        clock.tick(60)
        pygame.event.wait(1)
        pygame.display.update()
        pygame.display.flip()
    
#Other Functions
def playerWantClose():
    if (keyboard.is_pressed('esc')):
        print("closing")
        exit()

def meleeSwordDraw():
    global angle
    swordX, swordY = gamer.playerX + SWORD_OFFSET_X, gamer.playerY + SWORD_OFFSET_Y
    angle += 20
    # swordHB = (gamer.playerX + SWORD_OFFSET, gamer.playerY + SWORD_OFFSET, 2, 30)
    # swordRect = pygame.Rect(swordHB)
    # pygame.draw.rect(screen, (255, 0, 0), swordRect)
    #screen.blit(sword, (gamer.playerX + SWORD_OFFSET_X, gamer.playerY + SWORD_OFFSET_Y, 2, 30))
    swordRotation = pygame.transform.rotate(sword, angle)
    screen.blit(swordRotation, (swordX - int(swordRotation.get_width() / 2), swordY - int(swordRotation.get_height() / 2)))
    