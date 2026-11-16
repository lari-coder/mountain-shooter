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
                'Player2': 4,
                'Enemy1': 3,
                'Enemy2': 2,
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
P_K_SHOOT = {'Player1': pygame.K_SPACE,
          'Player2': pygame.K_KP_ENTER}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

