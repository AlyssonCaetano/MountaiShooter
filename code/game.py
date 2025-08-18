#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        #Definir tamanho da janela do windows
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        #Adicionar/carregar musica
        pygame.mixer_music.load('./asset/Menu.mp3')
        #Tocar a musica
        pygame.mixer_music.play(-1)

        while True:
            #chamar tela de menu
            menu = Menu(self.window)
            menu.run()
            pass


            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit() # Close window
            #         quit() # end pygame