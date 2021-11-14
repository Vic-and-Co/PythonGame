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
            
    def characterHitBoxUpdate(self):
        self.rectX = self.eX + int(self.appearence.get_width())
        self.rectY = self.eY + int(self.appearence.get_height())