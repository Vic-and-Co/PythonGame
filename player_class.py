"""
This is where we create controls for the player
"""
#Imports
import keyboard
import pygame
from constants import *

#Controls
class Player:
    '''playable character'''
    def __init__(self):
        self.player_x = 350 #    These are
        self.player_y = 350 # Start Positions
        self.player_hp = 3 #What health we player starts at
        self.player_hearts = pygame.image.load("Images/h3.png")
        self.appearence = pygame.image.load("Images/character.png")
        self.sword_hitzone = (self.player_x + SWORD_HB_OFFSET, \
        self.player_y + SWORD_HB_OFFSET, 80, 80)
        self.hitbox = pygame.Rect(self.player_x + HITBOX_OFFSET, \
        self.player_y + HITBOX_OFFSET, 13, 13)
        self.damage_cooldown = 0
        self.attack_cooldown = 0
        self.lunge_cooldown = 0
        self.focus = False
        
        self.taking_dmg = False
        self.player_rect = pygame.Rect(self.hitbox)
        
        #Attack bar
        self.allowed_bar_y = 180
        self.allowed_bar_going_down = True
        self.attack_allowed_bar = pygame.Rect(750, self.allowed_bar_y, 59, 30)
        self.attack_allowed_zone = pygame.Rect(750, 360, 59, 135)
        self.attack_allowed = False
        
        #Sword
        self.angle = 1
        self.sword = pygame.image.load("Images/sword.png")
        self.sword_x = 0
        self.sword_y = 0
        self.sword_rotation = pygame.transform.rotate(self.sword, self.angle)
        self.sword_rots_x = self.sword_x - int(self.sword_rotation.get_width() / 2)
        self.sword_rots_y = self.sword_y - int(self.sword_rotation.get_height() / 2)
        
    def player_movement(self):
        '''does player movement'''
        def move_right():
            self.lng_cooldown()
            if keyboard.is_pressed('right') or keyboard.is_pressed('d') and self.player_x < 690.5:
                if keyboard.is_pressed('shift'):
                    self.player_x += (PLAYER_SPEED * FPS_CAP) / 2
                    
                elif (keyboard.is_pressed('space') and self.lunge_cooldown == 0):
                    self.player_x += PLAYER_LUNGE * FPS_CAP
                    self.lunge_cooldown += 1
                    
                else:
                    self.player_x += (PLAYER_SPEED * FPS_CAP)
                
        def move_left():
            self.lng_cooldown()
            if keyboard.is_pressed('left') or keyboard.is_pressed('a') and self.player_x > -11:
                if keyboard.is_pressed('shift'):
                    self.player_x -= (PLAYER_SPEED * FPS_CAP) / 2
                
                elif keyboard.is_pressed('space') and self.lunge_cooldown == 0:
                    self.player_x -= PLAYER_LUNGE * FPS_CAP
                    self.lunge_cooldown += 1
                    
                else:
                    self.player_x -= PLAYER_SPEED * FPS_CAP

        def move_up():
            self.lng_cooldown()
            if keyboard.is_pressed('up') or keyboard.is_pressed('w') and self.player_y > -9:
                if keyboard.is_pressed('shift'):
                    self.player_y -= (PLAYER_SPEED * FPS_CAP) / 2
                
                elif (keyboard.is_pressed('space') and self.lunge_cooldown == 0):
                    self.player_y -= PLAYER_LUNGE * FPS_CAP
                    self.lunge_cooldown += 1
                    
                else:
                    self.player_y -= PLAYER_SPEED * FPS_CAP
            
        def move_down():
            self.lng_cooldown()
            if keyboard.is_pressed('down') or keyboard.is_pressed('s') and self.player_y < 690.5:
                if keyboard.is_pressed('shift'):
                    self.player_y += (PLAYER_SPEED * FPS_CAP) / 2
                
                elif (keyboard.is_pressed('space') and self.lunge_cooldown == 0):
                    self.player_y += PLAYER_LUNGE * FPS_CAP
                    self.lunge_cooldown += 1
                    
                else:
                    self.player_y += PLAYER_SPEED * FPS_CAP
        
                    
        move_right()
        move_left()
        move_up()
        move_down()
        
    def focus_mode_on(self):
        '''makes character slower and shows hitbox, hitzone'''
        if keyboard.is_pressed('shift'):
            self.appearence = pygame.image.load("Images/characterFocus.png")
            self.focus = True
        else:
            self.appearence = pygame.image.load("Images/character.png")
            self.focus = False
        return self.focus
        
    def dmg_cooldown(self):
        '''cooldown attack'''
        if self.damage_cooldown >= 60:
            self.damage_cooldown = 0
            self.taking_dmg = False
        elif self.damage_cooldown > 0:
            self.damage_cooldown += 0.05 * FPS_CAP
            
    def lng_cooldown(self):
        '''cooldown attack'''
        if self.lunge_cooldown >= 50:
            self.lunge_cooldown = 0
            self.lunge_cooldown = False
        elif self.lunge_cooldown > 0:
            self.lunge_cooldown += 0.05 * FPS_CAP
    
    def atk_cooldown(self):
        '''cooldown attack'''
        if self.attack_cooldown >= 30:
            self.attack_cooldown = 0
        elif self.attack_cooldown > 0:
            self.attack_cooldown += 0.05 * FPS_CAP
        
    def add_health(self):
        '''adds health'''
        if self.player_hp < 3:
            self.player_hp += 1
        
    def sub_health(self):
        '''subs health'''
        self.dmg_cooldown()
        if (self.player_hp > 0 and self.damage_cooldown == 0 and self.taking_dmg):
            self.player_hp -= 1
            self.damage_cooldown = 1
    
    def take_damage(self, enem_hitbox, enemy_alive):
        '''triggers damage taking'''
        if self.taking_dmg:
            self.sub_health()
        if pygame.Rect.colliderect(self.hitbox, enem_hitbox) and enemy_alive:
            self.taking_dmg = True
    
    def draw_health(self):
        '''draws hearts'''
        if self.player_hp == 3:
            self.player_hearts = pygame.image.load("Images/h3.png")
        
        elif self.player_hp == 2:
            self.player_hearts = pygame.image.load("Images/h2.png")
            
        elif self.player_hp == 1:
            self.player_hearts = pygame.image.load("Images/h1.png")
            
        elif self.player_hp == 0:
            self.player_hearts = pygame.image.load("Images/blank.png")
    
    def check_dead(self):
        '''is player dead?'''
        return self.player_hp < 1
            
    def allowed_bar_movement(self):
        '''The thing that moves up and down on the right'''
        if self.allowed_bar_y < 645 and self.allowed_bar_going_down:
            self.allowed_bar_y += (PLAYER_HITBAR_SPEED * FPS_CAP)
            self.attack_allowed_bar = pygame.Rect(750, self.allowed_bar_y, 60, 30)
            
            if self.allowed_bar_y > 644:
                self.allowed_bar_going_down = False
            
        elif self.allowed_bar_y > 180 and not self.allowed_bar_going_down:
            self.allowed_bar_y -= (PLAYER_HITBAR_SPEED * FPS_CAP)
            self.attack_allowed_bar = pygame.Rect(750, self.allowed_bar_y, 60, 30)
            
            if self.allowed_bar_y < 181:
                self.allowed_bar_going_down = True
    
    def player_attack(self):
        '''deal damage'''
        m1_press, m_mid_press, m2_press = pygame.mouse.get_pressed()
        self.atk_cooldown()
        if pygame.Rect.colliderect(self.attack_allowed_bar, self.attack_allowed_zone):
            if (m1_press and self.attack_cooldown <= 0):
                self.attack_cooldown = 1
                self.attack_allowed = True
            elif self.attack_cooldown >= 1:
                self.attack_allowed = False
        return self.attack_allowed
    
    def melee_sword_draw(self):
        '''draws the sword'''
        self.sword_x, self.sword_y = self.player_x + SWORD_OFFSET_X, self.player_y + SWORD_OFFSET_Y
        self.angle -= 20
        self.sword_rotation = pygame.transform.rotate(self.sword, self.angle)
        self.sword_rots_x = self.sword_x - int(self.sword_rotation.get_width() / 2)
        self.sword_rots_y = self.sword_y - int(self.sword_rotation.get_height() / 2)
            
    def character_hitbox_draw(self):
        '''updates hitbox location'''
        self.hitbox = pygame.Rect(self.player_x + HITBOX_OFFSET,\
        self.player_y + HITBOX_OFFSET, 13, 13)
        self.player_rect = pygame.Rect(self.hitbox)
        
        #Sword HitZone Draw
        self.appearence = pygame.image.load("Images/character.png")
        self.sword_hitzone = pygame.Rect(self.player_x + SWORD_HB_OFFSET, \
        self.player_y + SWORD_HB_OFFSET, 90, 90)
