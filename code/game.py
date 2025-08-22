#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
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

                if menu_return == MENU_OPTION[0]:
                    pass
                elif menu_return == MENU_OPTION[4]:
                    pygame.quit()
                    quit()
                else:
                    pass




