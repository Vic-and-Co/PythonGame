'''
Create classes for enemies here
'''
#Imports
from Constants import *
from PlayerClass import *
from Data import *
from threading import Timer
import random

gamer = Player()

class MeleeType:
    def __init__(self, eX, eY, subtype):
        self.eX = eX
        self.eY = eY
        self.speed = MELEE_E_SPEED
        self.appearence = pygame.image.load("Images/MeleeEnemy.png")
        self.health = 3
        
        self.damageCoolDown = 0
        self.lungeCoolDown = 0
        self.moveCoolDown = 0
        self.bossMoveCoolDown = 0
        self.subtype = subtype #1 top, 2 right, 3 bottom, 4 left
        
    def movement(self, playerX, playerY):
        self.mvCoolDown(100)
        self.boMvCoolDown(20)
        timer = Timer(0.3, self.lunge)
        bossTimer = Timer(0.3, self.lunge)
        if self.subtype == 1 and self.moveCoolDown == 0:
            self.eX = playerX + MELEE1_X_OFFSET
            self.eY = playerY + MELEE1_Y_OFFSET
            self.moveCoolDown = 1
            timer.start()
        
        elif self.subtype == 2 and self.moveCoolDown == 0:
            self.eX = playerX + MELEE2_X_OFFSET
            self.eY = playerY + MELEE2_Y_OFFSET
            self.moveCoolDown = 1
            timer.start()
        
        elif self.subtype == 3 and self.moveCoolDown == 0:
            self.eX = playerX + MELEE3_X_OFFSET
            self.eY = playerY + MELEE3_Y_OFFSET
            self.moveCoolDown = 1
            timer.start()
        
        elif self.subtype == 4 and self.moveCoolDown == 0:
            self.eX = playerX + MELEE4_X_OFFSET
            self.eY = playerY + MELEE4_Y_OFFSET
            self.moveCoolDown = 1
            timer.start()
            
        elif self.subtype == 5 and self.bossMoveCoolDown == 0:
            self.moveDir = random.randint(1, 4)
            if self.moveDir == 1:
                self.eX = playerX + MELEE1_X_OFFSET
                self.eY = playerY + MELEE1_Y_OFFSET
                self.bossMoveCoolDown = 1
                bossTimer.start()
                
            elif self.moveDir == 2:
                self.eX = playerX + MELEE2_X_OFFSET
                self.eY = playerY + MELEE2_Y_OFFSET
                self.bossMoveCoolDown = 1
                bossTimer.start()
            
            elif self.moveDir == 3:
                self.eX = playerX + MELEE3_X_OFFSET
                self.eY = playerY + MELEE3_Y_OFFSET
                self.bossMoveCoolDown = 1
                bossTimer.start()
            
            elif self.moveDir == 4:
                self.eX = playerX + MELEE4_X_OFFSET
                self.eY = playerY + MELEE4_Y_OFFSET
                self.bossMoveCoolDown = 1
                bossTimer.start()
    
    def lunge(self):
        if self.subtype == 1:
           self.eY += 40
        elif self.subtype == 2:
           self.eX += 40
        elif self.subtype == 3:
           self.eY -= 40
        elif self.subtype == 4:
           self.eX -= 40
        elif self.subtype == 5:
            if self.moveDir == 1:
                self.eY += 40
            elif self.moveDir == 2:
                self.eX += 40
            elif self.moveDir == 3:
                 self.eY -= 40
            elif self.moveDir == 4:
                self.eX -= 40
    
    def isPlayerAttack(self, swordHitZone, playerAttack):
        self.checkHealth()
        if (pygame.Rect.colliderect(self.hitbox, swordHitZone) and self.hitbox.collidepoint(pygame.mouse.get_pos()) and swordHitZone.collidepoint(pygame.mouse.get_pos())):
            #print('mouse-chan is touching me ^w^')
            if (playerAttack):
                print("pain")
                self.subHealth()
    
    def dmgCoolDown(self):
        if self.damageCoolDown >= 10:
            self.damageCoolDown = 0
        elif self.damageCoolDown > 0:
            self.damageCoolDown += 0.05 * FPS_CAP
    
    def lngCoolDown(self):
        if self.lungeCoolDown >= 30:
            self.lungeCoolDown = 0
        elif self.lungeCoolDown > 0:
            self.lungeCoolDown += 0.05 * FPS_CAP
            
    def mvCoolDown(self, cooldown):
        if self.moveCoolDown >= cooldown:
            self.moveCoolDown = 0
        elif self.moveCoolDown > 0:
            self.moveCoolDown += 0.05 * FPS_CAP
    
    def boMvCoolDown(self, cooldown):
        if self.bossMoveCoolDown >= cooldown:
            self.bossMoveCoolDown = 0
        elif self.bossMoveCoolDown > 0:
            self.bossMoveCoolDown += 0.05 * FPS_CAP
    
    def addHealth(self):
        if (self.health < 3):
            self.health += 1
    
    def subHealth(self):
        self.dmgCoolDown()
        self.checkHealth()
        self.health -= 1
    
    def isAlive(self):
        return self.health > 0
            
    def checkHealth(self):
        if self.health == 3:
            self.appearence = pygame.image.load("Images/MeleeEnemy.png")
        elif self.health == 2:
            self.appearence = pygame.image.load("Images/MeleeEnemy2.png")
        elif self.health == 1:
            self.appearence = pygame.image.load("Images/MeleeEnemy3.png")
        elif self.health == 0:
            self.appearence = pygame.image.load("Images/blank.png")
            if self.subtype == 5:
                stage1Done = True

    def characterHitBoxUpdate(self):
        self.rectX = 39
        self.rectY = 39
        self.hitbox = pygame.Rect(self.eX, self.eY, self.rectX, self.rectY)