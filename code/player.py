#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.playerShot import PlayerShot
from code.const import ENTITY_SHOT_DELAY, ENTITY_SPEED, P_K_DOWN, P_K_LEFT, P_K_RIGHT, P_K_SHOT, P_K_UP, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[P_K_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[P_K_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[P_K_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[P_K_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shot(self):
        if self.shot_delay > 0:
            self.shot_delay -= 1
        if self.shot_delay == 0:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[P_K_SHOT[self.name]]:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        