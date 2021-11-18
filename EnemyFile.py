'''
Create classes for enemies here
'''
#Imports
from Constants import *
from PlayerClass import *

gamer = Player()

class MeleeType:
    def __init__(self, eX, eY):
        self.eX = eX
        self.eY = eY
        self.speed = MELEE_E_SPEED
        self.appearence = pygame.image.load("Images/MeleeEnemy.jpg")
        self.health = 3
        
    def goTowardsPlayerX(self, playerX):
        if (self.eX > playerX):
            self.eX  -= (MELEE_E_SPEED * FPS_CAP)
        elif (self.eX < playerX):
            self.eX  += (MELEE_E_SPEED * FPS_CAP)
            
    def goTowardsPlayerY(self, playerY):
        if (self.eY > playerY):
            self.eY  -= (MELEE_E_SPEED * FPS_CAP)
        elif (self.eY < playerY):
            self.eY  += (MELEE_E_SPEED * FPS_CAP)
            
    def isPlayerAttack(self, swordHitZone, playerAttack):
        if (pygame.Rect.colliderect(self.hitbox, swordHitZone) and self.hitbox.collidepoint(pygame.mouse.get_pos()) and swordHitZone.collidepoint(pygame.mouse.get_pos())):
            if (playerAttack):
                exit()
    
    def addHealth(self):
        if (self.health < 3):
            self.health += 1
    
    def subHealth(self):
        if (self.health > 0):
            self.health -= 1
    
    def checkHealth(self):
        if self.health == 3:
            self.appearence = pygame.image.load("Images/MeleeEnemy.jpg")
        elif self.health == 2:
            self.appearence = pygame.image.load("Images/MeleeEnemy2.jpg")
        elif self.health == 1:
            self.appearence = pygame.image.load("Images/MeleeEnemy3.jpg")

    def characterHitBoxUpdate(self):
        self.rectX = 72
        self.rectY = 8
        self.hitbox = pygame.Rect(self.eX, self.eY, self.rectX, self.rectY)