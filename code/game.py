#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        #Definir tamanho da janela do windows
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
            while True:
                #chamar tela de menu
                menu = Menu(self.window)
                menu_return = menu.run()


                if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                    player_score = [0,0] #score player 1 and player 2
                    #Chama level 1
                    level = Level(self.window, 'Level1', menu_return, player_score)
                    level_return = level.run(player_score)
                    #Chama level  2
                    if level_return:
                        level = Level(self.window, 'Level2', menu_return, player_score)
                        level_return = level.run(player_score)

                elif menu_return == MENU_OPTION[4]:
                    pygame.quit()
                    quit()
                else:
                    pass




