#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Font, Rect, Surface
import pygame.image

from code.const import C_ORANGE, C_WHITE, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=C_WHITE, text_center_ps=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=C_WHITE,text_center_ps=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_WHITE,
                               text_center_ps=((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit() # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_ps: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True, color=text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_ps)
        self.window.blit(source=text_surf, dest=text_rect)




