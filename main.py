'''
Where the game is run
'''

#Imports
import sys
import random
from time import sleep, time
from threading import Timer
import pygame
import keyboard

from player_class import *
from enemy_file import *
from the_world import *


#Bruh
pygame.init()

#Variables
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
clock = pygame.time.Clock()

#Images
menu = pygame.image.load("Images/menu.png")
side_screen = pygame.image.load("Images/sideScreen.png")
sword = pygame.image.load("Images/sword.png")
red_screen = pygame.image.load("Images/dead.png")

#Player Instance
gamer = Player()

#Enemy Classes
m_enemy1 = MeleeType(100, 100, 0, 1)
m_enemy2 = MeleeType(100, 100, 0, 2)
m_enemy3 = MeleeType(100, 100, 0, 3)
m_enemy4 = MeleeType(100, 100, 0, 4)
m_boss = MeleeType(100, 100, 0, 5)


the_world = World(0)


def main():
    '''Main Method'''
    #Keep at top
    game_running = True
    player_close()
    pygame.display.set_caption(random_name())
    while game_running:
        #keep at top of game_running
        player_close()
        
        #Meeeenu
        screen.blit(menu, (0, 0))
    
        #These need to be at the end of draw since they're at the top
        if (keyboard.is_pressed('tab') and (the_world.area == 0)):
            screen.blit(menu, (0, 0))

        
        screen.blit(side_screen, (0, 0))
        screen.blit(gamer.player_hearts, (0, 0))
        
        pygame.draw.rect(screen,(255, 255, 255), (gamer.attack_allowed_bar))

        #World
        world_change_var = the_world.world_change(gamer.hitbox, m_boss.boss1_dead)
        if world_change_var == "bot":
            gamer.player_y = 630
            the_world.go_to = ""
        elif world_change_var == "top":
            gamer.player_y = 60
            the_world.go_to = ""
        elif world_change_var == "left":
            gamer.player_x = 60
            the_world.go_to = ""
        elif world_change_var == "right":
            gamer.player_x = 620
            the_world.go_to = ""
        the_world.world_image()
        screen.blit(the_world.appearence, (0, 0))

        #Player
        player_functions()
        
        #Enemy Spawning Stage 1
        m_enemy_spawn()
    
        #Death Check
        if gamer.check_dead():
            screen.blit(red_screen, (0, 0))
            game_running = False
            
        #Player Class Stuff that takes enemy arg
        clock.tick(60)
        pygame.event.wait(1)
        pygame.display.update()
        pygame.display.flip()
    
    while not game_running:
        player_close()

#Functions
def player_functions():
    '''does player functions'''
    gamer.player_movement()
    gamer.focus_mode_on()
    gamer.draw_health()
    gamer.allowed_bar_movement()
    gamer.player_attack()
    screen.blit(gamer.appearence, (gamer.player_x, gamer.player_y))
    gamer.character_hitbox_draw()
        
    if gamer.attack_cooldown != 0:
        gamer.melee_sword_draw()
        screen.blit(gamer.sword_rotation, (gamer.sword_rots_x, gamer.sword_rots_y))
    if gamer.focus_mode_on():
        pygame.draw.rect(screen, (255, 0 ,0),
        gamer.sword_hitzone, 2) #Draws Hit Zone if Shift
        
    if the_world.area == 0:
        gamer.player_hp = 3     

def m_enemy_spawn():
    '''does melee enemy spawning'''
    if the_world.world_enemy_spawn():
        if not the_world.stage1_enemy1_spawned: #Spawn Melee Enemy 1
            m_enemy1.health = 3
            m_enemy1.e_x = 100
            m_enemy1.e_y = 100
            
            if gamer.player_x <= 615:
                the_world.stage1_enemy1_spawned = True
        
        if m_enemy1.health == 0: #Spawn Melee Enemy 2
            m_enemy1.health -= 1
            
            the_world.stage1_enemy2_spawned = True
            m_enemy2.health = 3
            m_enemy2.e_x = 620
            m_enemy2.e_y = 100
        
        if the_world.stage1_enemy2_spawned and m_enemy2.health == 0: #Spawn Melee Enemy 3
            m_enemy2.health -= 1
            
            the_world.stage1_enemy3_spawned = True
            m_enemy3.health = 3
            m_enemy3.e_x = 100
            m_enemy3.e_y = 620
        
        if the_world.stage1_enemy3_spawned and m_enemy3.health == 0: #Spawn Melee Enemy 4
            m_enemy3.health -= 1
            
            the_world.stage1_enemy4_spawned = True
            m_enemy4.health = 3
            m_enemy4.e_x = 620
            m_enemy4.e_y = 620
        
        if the_world.stage1_enemy4_spawned and m_enemy4.health == 0: #Spawn Melee Boss
            m_enemy4.health -= 1
            
            the_world.stage1_boss_spawned = True
            m_boss.health = 3
            m_boss.e_x = 350
            m_boss.e_y = 350
        
        if the_world.stage1_boss_spawned and m_boss.health <= 0: #Relays if boss1 dead
            the_world.stage1_done = True
            
        m_enemy_functions()

def m_enemy_functions():
    '''does melee enemy functions'''
    m_enemy1.character_hitbox_update()
    m_enemy1.check_health()
    m_enemy1.movement(gamer.player_x, gamer.player_y)
    m_enemy1.is_player_attack(gamer.sword_hitzone, gamer.attack_allowed)
    
    m_enemy2.character_hitbox_update()
    m_enemy2.check_health()
    m_enemy2.movement(gamer.player_x, gamer.player_y)
    m_enemy2.is_player_attack(gamer.sword_hitzone, gamer.attack_allowed)

    m_enemy3.character_hitbox_update()
    m_enemy3.check_health()
    m_enemy3.movement(gamer.player_x, gamer.player_y)
    m_enemy3.is_player_attack(gamer.sword_hitzone, gamer.attack_allowed)
    
    m_enemy4.character_hitbox_update()
    m_enemy4.check_health()
    m_enemy4.movement(gamer.player_x, gamer.player_y)
    m_enemy4.is_player_attack(gamer.sword_hitzone, gamer.attack_allowed)
    
    m_boss.character_hitbox_update()
    m_boss.check_health()
    m_boss.movement(gamer.player_x, gamer.player_y)
    m_boss.is_player_attack(gamer.sword_hitzone, gamer.attack_allowed)
    
    gamer.take_damage(m_enemy1.hitbox, m_enemy1.is_alive())
    gamer.take_damage(m_enemy2.hitbox, m_enemy2.is_alive())
    gamer.take_damage(m_enemy3.hitbox, m_enemy3.is_alive())
    gamer.take_damage(m_enemy4.hitbox, m_enemy4.is_alive())
    gamer.take_damage(m_boss.hitbox, m_boss.is_alive())
        
    screen.blit(m_enemy1.appearence, (m_enemy1.e_x, m_enemy1.e_y))
    screen.blit(m_enemy2.appearence, (m_enemy2.e_x, m_enemy2.e_y))
    screen.blit(m_enemy3.appearence, (m_enemy3.e_x, m_enemy3.e_y))
    screen.blit(m_enemy4.appearence, (m_enemy4.e_x, m_enemy4.e_y))
    screen.blit(m_boss.appearence, (m_boss.e_x, m_boss.e_y))
#Other Functions
def player_close():
    '''Check if player close'''
    if keyboard.is_pressed('esc'):
        print("closing")
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def random_name():
    '''Makes window title a random name'''
    title_num = random.randint(1,6)
    if title_num == 1:
        title = "NIGHTMARE NIGHTMARE NIGHTMARE"
    if title_num == 2:
        title = "Epic rpg bossfight simulator"
    if title_num == 3:
        title = "Sponsered by my tears"
    if title_num == 4:
        title = "The Older Writings"
    if title_num == 5:
        title = "Made in Chinor"
    if title_num == 6:
        title = "Strohm Bot 2000.exe VER.3 (In Progress)"
    return title
    