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

#Bruh
pygame.init()

#Variables
gamer = Player()
dummy = MeleeType(700, 200)

angle = 1

width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
area = 0 #0 refers to start area, other numbers correspond to their respective stages

clock = pygame.time.Clock()

#Images
startArea = pygame.image.load("Images/Start Area.png")
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
        
        #Meeeenu
        screen.blit(menu, (0, 0))
        
        #Dumb Eggies' Movement
        dummy.goTowardsPlayerX(gamer.playerX)
        dummy.goTowardsPlayerY(gamer.playerY)
        
        #Refresh    
        screen.blit(startArea, (0, 0))
        pygame.draw.circle(screen, (255, 0 ,0), (gamer.playerX + SWORD_OFFSET_X, gamer.playerY + SWORD_OFFSET_Y), 40) #Will change location
        screen.blit(gamer.appearence, (gamer.playerX, gamer.playerY))
        screen.blit(dummy.appearence, (dummy.eX, dummy.eY))
        gamer.characterHitBoxDraw()
        dummy.characterHitBoxUpdate()
        
        meleeSwordHBDraw()
        
             #These need to be at the end of draw since they're at the top
        if (keyboard.is_pressed('tab') and (area == 0)):
            screen.blit(menu, (0, 0))
            menuOpen = True
        else:
            menuOpen = False
        
        gamer.drawHealth()
        screen.blit(sideScreen, (0, 0))
        screen.blit(gamer.playerHearts, (0, 0))
        
        
        clock.tick(60)
        pygame.event.wait(1)
        pygame.display.update()
    
#Other Functions
def playerWantClose():
    if (keyboard.is_pressed('esc')):
        print("closing")
        exit()

def meleeSwordHBDraw():
    global angle
    swordX, swordY = gamer.playerX + SWORD_OFFSET_X, gamer.playerY + SWORD_OFFSET_Y
    angle += 20
    # swordHB = (gamer.playerX + SWORD_OFFSET, gamer.playerY + SWORD_OFFSET, 2, 30)
    # swordRect = pygame.Rect(swordHB)
    # pygame.draw.rect(screen, (255, 0, 0), swordRect)
    #screen.blit(sword, (gamer.playerX + SWORD_OFFSET_X, gamer.playerY + SWORD_OFFSET_Y, 2, 30))
    swordRotation = pygame.transform.rotate(sword, angle)
    screen.blit(swordRotation, (swordX - int(swordRotation.get_width() / 2), swordY - int(swordRotation.get_height() / 2)))

if __name__ == "__main__":
    main()