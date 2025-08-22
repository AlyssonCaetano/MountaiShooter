#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.entity import Entity


class Player(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)

    def move(self, ):
        #enquanto a tecla estiver pressionada
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.react.centery -= 1
        pass
