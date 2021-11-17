'''
Create classes for enemies here
'''
#Imports
from Constants import *
from PlayerClass import *
from Data import *

gamer = Player()

class MeleeType:
    def __init__(self, eX, eY):
        self.eX = eX
        self.eY = eY
        self.speed = MELEE_E_SPEED
        self.appearence = pygame.image.load("Images/rals.jpg")
        
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
            
    def isPlayerAttack(self, swordHitZone, attackAllowed):
        if (pygame.Rect.colliderect(self.hitbox, swordHitZone) and self.hitbox.collidepoint(pygame.mouse.get_pos()) and swordHitZone.collidepoint(pygame.mouse.get_pos())):
            m1Press, mMidPress, m2Press = pygame.mouse.get_pressed()
            if (m1Press and attackAllowed):
                #print("attacked!")
                exit()
            

    def characterHitBoxUpdate(self):
        self.rectX = 72
        self.rectY = 8
        self.hitbox = pygame.Rect(self.eX, self.eY, self.rectX, self.rectY)
        
    