#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        #Opção escolhida
        menu_option = 0
        # Adicionar/ carregar musica
        pygame.mixer_music.load('./asset/Menu.mp3')
        # Tocar a musica
        pygame.mixer_music.play(-1)
        while True:
            #Criar background e depois texto
            self.window.blit(source=self.surf, dest=self.rect)
            #TExto na tela, tamanho de fonte, cor e posição(x,y).
            self.menu_text(50,"Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Sooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25*i))
            pygame.display.flip()

            # Check for all events
            # Event for close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit() # end pygame

                # Event for select option in menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and menu_option >= 0:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option+=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP and menu_option >= 0:
                        if menu_option > 0 :
                            menu_option -=1
                        else:
                            menu_option = 4
                    # Acept option with ENTER
                    if event.key == pygame.K_RETURN:
                        return  MENU_OPTION[menu_option]



    # metodo estipulado para classe MENU, desenhar texto como imagem na tela
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
