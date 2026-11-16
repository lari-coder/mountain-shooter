# C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

# E
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 4,
                'Player1Shot': 1,
                'Player2': 4,
                'Player2Shot': 3,
                'Enemy1': 1,
                'Enemy1Shot': 5,
                'Enemy2': 1,
                'Enemy2Shot': 2,
                }

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
P_K_UP = {'Player1': pygame.K_w,
          'Player2': pygame.K_UP}
P_K_DOWN = {'Player1': pygame.K_s,
          'Player2': pygame.K_DOWN}
P_K_LEFT = {'Player1': pygame.K_a,
          'Player2': pygame.K_LEFT}
P_K_RIGHT = {'Player1': pygame.K_d,
          'Player2': pygame.K_RIGHT}
P_K_SHOT = {'Player1': pygame.K_SPACE,
          'Player2': pygame.K_RCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

