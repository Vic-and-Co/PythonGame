'''
Self explanitory
'''
import pygame
CLOCK = pygame.time.Clock()
FPS_CAP = CLOCK.tick(60)

SCR_WID = 1080
SCR_HEI = 720

PLAYER_SPEED = 0.3
PLAYER_LUNGE = 2
HITBOX_OFFSET = 13
PLAYER_HITBAR_SPEED = 1

SWORD_OFFSET_X = 19.5
SWORD_OFFSET_Y = 19
SWORD_HB_OFFSET = -25

MELEE_E_SPEED = 0.15

MELEE1_X_OFFSET = 0
MELEE1_Y_OFFSET = -50

MELEE2_X_OFFSET = -50
MELEE2_Y_OFFSET = 0

MELEE3_X_OFFSET = 0
MELEE3_Y_OFFSET = 50

MELEE4_X_OFFSET = 50
MELEE4_Y_OFFSET = 0