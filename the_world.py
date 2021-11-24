'''
The world class: dictates the stages/ areas
'''
import pygame
from constants import *

class World:
    '''dictates the world background'''
    def __init__(self, area):
        self.area = area #0 pertains to starting area, area 1 = stage 1
        self.appearence = pygame.image.load("Images/Start Area.png")
        
        #Detection Boundaries
        self.up_square = pygame.Rect(255, 0, 209, 30)
        self.down_square = pygame.Rect(255, 690, 209, 30)
        self.left_square = pygame.Rect(0, 255, 30, 209)
        self.right_square = pygame.Rect(690, 255, 30, 209)
        
        self.change_cooldown = 0
        self.go_to = ""
        
        #Stage Boss Defeated?
        self.stage1_enemy1_spawned = False
        self.stage1_enemy2_spawned = False
        self.stage1_enemy3_spawned = False
        self.stage1_enemy4_spawned = False
        self.stage1_boss_spawned = False
        self.stage1_done = False
        
    def world_change(self, player_hitbox, boss1_dead):
        '''returns a value that determines which area to go to'''
        if pygame.Rect.colliderect(self.up_square, player_hitbox) and self.area == 0:
            self.area = 2
            self.go_to = "bot"
        
        if pygame.Rect.colliderect(self.down_square, player_hitbox) and self.area == 2:
            self.area = 0
            self.go_to = "top"
        
        if pygame.Rect.colliderect(self.right_square, player_hitbox) and self.change_cooldown == 0:
            self.wrld_change_cooldown()
            if self.area == 0:
                self.area = 3
                self.go_to = "left"
            
            #Stage 1
            elif self.area == 1 and self.stage1_boss_spawned and boss1_dead:
                self.area = 0
                self.go_to = "left"
                
        if pygame.Rect.colliderect(self.left_square, player_hitbox):
            self.wrld_change_cooldown()
            if self.area == 0:
                self.area = 1
                self.go_to = "right"
            elif self.area == 3:
                self.area = 0
                self.go_to = "right"
        return self.go_to
    
    def world_image(self):
        '''sets background image'''
        if self.area == 0:
            self.appearence = pygame.image.load("Images/Start Area.png")
            
        elif self.area == 1:
            if self.stage1_done:
                self.appearence = pygame.image.load("Images/Stage1Done.png")
            else:
                self.appearence = pygame.image.load("Images/Stage1.png")
            
        elif self.area == 2:
            self.appearence = pygame.image.load("Images/Stage2.png")
            
        elif self.area == 3:
            self.appearence = pygame.image.load("Images/Stage3.png")
            
    def wrld_change_cooldown(self):
        '''Cooldown for world change'''
        if self.change_cooldown >= 30:
            self.change_cooldown = 0
        elif self.change_cooldown > 0:
            self.change_cooldown += 0.05 * FPS_CAP
            
    def world_enemy_spawn(self):
        '''Returns T/F for if enemies should spawn'''
        spawn = self.area == 1 and not self.stage1_done
        return spawn
