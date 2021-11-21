'''
The world class: dictates the stages/ areas
'''
import pygame
from Constants import *

class World:
    def __init__(self, area):
        self.area = area #0 pertains to starting area, other stages are their individual stage numbers
        self.changedArea = False
        self.appearence = pygame.image.load("Images/Start Area.png")
        
        #Detection Boundaries
        self.upSquare = pygame.Rect(255, 0, 209, 30)
        self.downSquare = pygame.Rect(255, 690, 209, 30)
        self.leftSquare = pygame.Rect(0, 255, 30, 209)
        self.rightSquare = pygame.Rect(690, 255, 30, 209)
        
        self.changeCoolDown = 0
        
        #Stage Boss Defeated?
        self.stage1Enemy1Spawned = False
        self.stage1Enemy2Spawned = False
        self.stage1Enemy3Spawned = False
        self.stage1Enemy4Spawned = False
        self.stage1BossSpawned = False
        self.stage1Done = False
        
    def worldChange(self, playerHitBox, playerX, playerY, boss1Dead):
        if pygame.Rect.colliderect(self.upSquare, playerHitBox) and self.area == 0:
            self.area = 2
            return "bot"
        
        if pygame.Rect.colliderect(self.downSquare, playerHitBox) and self.area == 2:
            self.area = 0
            return "top"
        
        if pygame.Rect.colliderect(self.rightSquare, playerHitBox) and self.changeCoolDown == 0:
            self.wrldChangeCoolDown()
            if self.area == 0:
                self.area = 3
                return "left"
            
            #Stage 1 
            elif self.area == 1 and self.stage1BossSpawned and boss1Dead:
                self.area = 0
                return "left"
                
        if pygame.Rect.colliderect(self.leftSquare, playerHitBox):
            self.wrldChangeCoolDown()
            if self.area == 0:
                self.area = 1
                return "right"
            elif self.area == 3:
                self.area = 0
                return "right"
            
    def isStageLock(self):
        if self.area == 1:
            if self.stage1Done():
                return False
            else:
                return True
        
    def worldImage(self):
        if self.area == 0:
            self.appearence = pygame.image.load("Images/Start Area.png")
            
        elif self.area == 1:
            if self.stage1Done:
                self.appearence = pygame.image.load("Images/Stage1Done.png")
            else:
                self.appearence = pygame.image.load("Images/Stage1.png")
            
        elif self.area == 2:
            self.appearence = pygame.image.load("Images/Stage2.png")
            
        elif self.area == 3:
            self.appearence = pygame.image.load("Images/Stage3.png")
            
    def wrldChangeCoolDown(self):
        if self.changeCoolDown >= 30:
            self.changeCoolDown = 0
        elif self.changeCoolDown > 0:
            self.changeCoolDown += 0.05 * FPS_CAP
            
    def worldEnemySpawn(self):
        if self.area == 1 and not self.stage1Done:
            return True
        else:
            return False