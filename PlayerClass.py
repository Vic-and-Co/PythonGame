"""
This is where we create controls for the player
"""
#Imports
from re import A
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
        self.swordHitZone = (self.playerX + SWORD_HB_OFFSET, self.playerY + SWORD_HB_OFFSET, 80, 80)
        self.hitbox = pygame.Rect(self.playerX + HITBOX_OFFSET, self.playerY + HITBOX_OFFSET, 13, 13)
        self.damageCoolDown = 0
        self.attackCoolDown = 0
        
        self.takingDmg = False
        self.doDmg = False
        
        #Attack bar
        self.allowedBarY = 180
        self.allowedBarGoingDown = True
        self.attackAllowedBar = pygame.Rect(750, self.allowedBarY, 59, 30) #No clue what to call this, its the thing that moves up and down, dictating if you can attack
        self.attackAllowedZone = pygame.Rect(750, 360, 59, 135)
        self.attackAllowed = False
        
        #Super
        self.angle = 1
        self.sword = pygame.image.load("Images/sword.png")
        self.swordX = 0
        self.swordY = 0
        
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
            self.appearence = pygame.image.load("Images/characterFocus.png")
        else:
            self.appearence = pygame.image.load("Images/character.png")
        
        
    def dmgCoolDown(self):
        if self.damageCoolDown >= 30:
            self.damageCoolDown = 0
            self.takingDmg = False
        elif self.damageCoolDown > 0:
            self.damageCoolDown += 0.05 * FPS_CAP
    
    def atkCoolDown(self):
        if self.attackCoolDown >= 30:
            self.attackCoolDown = 0
        elif self.attackCoolDown > 0:
            self.attackCoolDown += 0.05 * FPS_CAP
        
    def addHealth(self):
        if (self.playerHp < 3):
            self.playerHp += 1
        
    def subHealth(self):
        self.dmgCoolDown()
        if (self.playerHp > 0 and self.damageCoolDown == 0 and self.takingDmg):
            self.playerHp -= 1
            self.damageCoolDown = 1
    
    def takeDamage(self, enemHitBox, enemyAlive):
        if self.takingDmg == True:
            self.subHealth()
        if pygame.Rect.colliderect(self.hitbox, enemHitBox) and enemyAlive:
            self.takingDmg = True
            #self.subHealth()
    
    def drawHealth(self):
        if (self.playerHp == 3):
            self.playerHearts = pygame.image.load("Images/h3.png")
        
        elif (self.playerHp == 2):
            self.playerHearts = pygame.image.load("Images/h2.png")
            
        elif (self.playerHp == 1):
            self.playerHearts = pygame.image.load("Images/h1.png")
            
        elif (self.playerHp == 0):
            self.playerHearts = pygame.image.load("Images/blank.png")
    
    def checkDead(self):
        if self.playerHp < 1:
            return True
            
    def allowedBarMovement(self):
        if ((self.allowedBarY < 645) and self.allowedBarGoingDown):
            self.allowedBarY += (PLAYER_HITBAR_SPEED * FPS_CAP)
            self.attackAllowedBar = pygame.Rect(750, self.allowedBarY, 60, 30)
            
            if self.allowedBarY > 644:
                self.allowedBarGoingDown = False
            
        elif ((self.allowedBarY > 180) and not self.allowedBarGoingDown):
            self.allowedBarY -= (PLAYER_HITBAR_SPEED * FPS_CAP)
            self.attackAllowedBar = pygame.Rect(750, self.allowedBarY, 60, 30)
            
            if self.allowedBarY < 181:
                self.allowedBarGoingDown = True
    
    def playerAttack(self):
        m1Press, mMidPress, m2Press = pygame.mouse.get_pressed()
        self.atkCoolDown()
        if pygame.Rect.colliderect(self.attackAllowedBar, self.attackAllowedZone):
            if (m1Press and self.attackCoolDown <= 0):
                print("bruh")
                self.attackCoolDown = 1
                self.attackAllowed = True
                return True
            elif self.attackCoolDown >= 1:
                self.attackAllowed = False
        # else:
        #     self.attackAllowed = False
        #     return False
    
    def meleeSwordDraw(self):
        self.swordX, self.swordY = self.playerX + SWORD_OFFSET_X, self.playerY + SWORD_OFFSET_Y
        self.angle -= 20
        self.swordRotation = pygame.transform.rotate(self.sword, self.angle)
        #screen.blit(swordRotation, (swordX - int(swordRotation.get_width() / 2), swordY - int(swordRotation.get_height() / 2)))
        self.swordRotsX = self.swordX - int(self.swordRotation.get_width() / 2)
        self.swordRotsY = self.swordY - int(self.swordRotation.get_height() / 2)
            
    def characterHitBoxDraw(self):
        self.hitbox = pygame.Rect(self.playerX + HITBOX_OFFSET, self.playerY + HITBOX_OFFSET, 13, 13)
        self.playerRect = pygame.Rect(self.hitbox)
        
        #Sword HitZone Draw
        self.appearence = pygame.image.load("Images/character.png")
        self.swordHitZone = pygame.Rect(self.playerX + SWORD_HB_OFFSET, self.playerY + SWORD_HB_OFFSET, 90, 90)