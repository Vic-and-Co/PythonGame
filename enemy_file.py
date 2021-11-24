'''
Create classes for enemies here
'''
#Imports
from threading import Timer
import random
from constants import *
from player_class import *

gamer = Player()

class MeleeType:
    '''Class for the melee enemy'''
    def __init__(self, e_x, e_y, health, subtype):
        self.e_x = e_x
        self.e_y = e_y
        self.speed = MELEE_E_SPEED
        self.appearence = pygame.image.load("Images/MeleeEnemy.png")
        self.health = health
        self.hitbox = pygame.Rect(self.e_x, self.e_y, 39, 39)
        
        self.damage_cooldown = 0
        self.lunge_cooldown = 0
        self.move_cooldown = 0
        self.boss_move_cooldown = 0
        self.subtype = subtype #1 top, 2 right, 3 bottom, 4 left
        self.boss1_dead = False
        self.move_dir = 0
        
    def movement(self, player_x, player_y):
        '''melee enemy movement'''
        self.mv_cooldown(100)
        self.boss_mv_cooldown(50)
        timer = Timer(0.3, self.lunge)
        boss_timer = Timer(0.3, self.lunge)
        if self.subtype == 1 and self.move_cooldown == 0:
            self.e_x = player_x + MELEE1_X_OFFSET
            self.e_y = player_y + MELEE1_Y_OFFSET
            self.move_cooldown = 1
            timer.start()
        
        elif self.subtype == 2 and self.move_cooldown == 0:
            self.e_x = player_x + MELEE2_X_OFFSET
            self.e_y = player_y + MELEE2_Y_OFFSET
            self.move_cooldown = 1
            timer.start()
        
        elif self.subtype == 3 and self.move_cooldown == 0:
            self.e_x = player_x + MELEE3_X_OFFSET
            self.e_y = player_y + MELEE3_Y_OFFSET
            self.move_cooldown = 1
            timer.start()
        
        elif self.subtype == 4 and self.move_cooldown == 0:
            self.e_x = player_x + MELEE4_X_OFFSET
            self.e_y = player_y + MELEE4_Y_OFFSET
            self.move_cooldown = 1
            timer.start()
            
        elif self.subtype == 5 and self.boss_move_cooldown == 0:
            self.move_dir = random.randint(1, 4)
            if self.move_dir == 1:
                self.e_x = player_x + MELEE1_X_OFFSET
                self.e_y = player_y + MELEE1_Y_OFFSET
                self.boss_move_cooldown = 1
                boss_timer.start()
                
            elif self.move_dir == 2:
                self.e_x = player_x + MELEE2_X_OFFSET
                self.e_y = player_y + MELEE2_Y_OFFSET
                self.boss_move_cooldown = 1
                boss_timer.start()
            
            elif self.move_dir == 3:
                self.e_x = player_x + MELEE3_X_OFFSET
                self.e_y = player_y + MELEE3_Y_OFFSET
                self.boss_move_cooldown = 1
                boss_timer.start()
            
            elif self.move_dir == 4:
                self.e_x = player_x + MELEE4_X_OFFSET
                self.e_y = player_y + MELEE4_Y_OFFSET
                self.boss_move_cooldown = 1
                boss_timer.start()
    
    def lunge(self):
        '''Enemy lunging at you after movement'''
        if self.subtype == 1:
            self.e_y += 40
        elif self.subtype == 2:
            self.e_x += 40
        elif self.subtype == 3:
            self.e_y -= 40
        elif self.subtype == 4:
            self.e_x -= 40
        elif self.subtype == 5:
            if self.move_dir == 1:
                self.e_y += 40
            elif self.move_dir == 2:
                self.e_x += 40
            elif self.move_dir == 3:
                self.e_y -= 40
            elif self.move_dir == 4:
                self.e_x -= 40
    
    def is_player_attack(self, sword_hitzone, player_attack):
        '''player attacked; subtract health'''
        self.check_health()
        if (pygame.Rect.colliderect(self.hitbox, sword_hitzone) and \
            self.hitbox.collidepoint(pygame.mouse.get_pos()) and \
                sword_hitzone.collidepoint(pygame.mouse.get_pos())):
            #print('mouse-chan is touching me ^w^')
            if player_attack:
                self.sub_health()
    
    def dmg_cooldown(self):
        '''cooldown damage'''
        if self.damage_cooldown >= 10:
            self.damage_cooldown = 0
        elif self.damage_cooldown > 0:
            self.damage_cooldown += 0.05 * FPS_CAP
    
    def lng_cooldown(self):
        '''cooldown lunge'''
        if self.lunge_cooldown >= 30:
            self.lunge_cooldown = 0
        elif self.lunge_cooldown > 0:
            self.lunge_cooldown += 0.05 * FPS_CAP
            
    def mv_cooldown(self, cooldown):
        '''cooldown movement'''
        if self.move_cooldown >= cooldown:
            self.move_cooldown = 0
        elif self.move_cooldown > 0:
            self.move_cooldown += 0.05 * FPS_CAP
    
    def boss_mv_cooldown(self, cooldown):
        '''cooldown boss movement'''
        if self.boss_move_cooldown >= cooldown:
            self.boss_move_cooldown = 0
        elif self.boss_move_cooldown > 0:
            self.boss_move_cooldown += 0.05 * FPS_CAP
    
    def add_health(self):
        '''adds health'''
        if self.health < 3:
            self.health += 1
    
    def sub_health(self):
        '''subtracts health'''
        self.dmg_cooldown()
        self.check_health()
        self.health -= 1
    
    def is_alive(self):
        '''checks if enemy is alive'''
        return self.health > 0
            
    def check_health(self):
        '''checks health'''
        if self.health == 3:
            self.appearence = pygame.image.load("Images/MeleeEnemy.png")
        elif self.health == 2:
            self.appearence = pygame.image.load("Images/MeleeEnemy2.png")
        elif self.health == 1:
            self.appearence = pygame.image.load("Images/MeleeEnemy3.png")
        elif self.health <= 0:
            self.appearence = pygame.image.load("Images/blank.png")
            if self.subtype == 5:
                self.boss1_dead = True

    def character_hitbox_update(self):
        '''updates hitbox location'''
        self.hitbox = pygame.Rect(self.e_x, self.e_y, 39, 39)
