#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from bisect import bisect_left
from random import choice
from tkinter.constants import SEL_FIRST

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.player import Player
from code.enemy import Enemy
from code.Const import WIN_HEIGHT, COLOR_WHITE, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, COLOR_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.EntityMediator import EntityMediator
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) # 'Level1Bg'
        self.entity_list.append(EntityFactory.get_entity('Player1'))


        #Add player 2
        if game_mode in [MENU_OPTION[1],MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        #Instanciar o inimigo a cada periodo de tempo
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        #tocar musica na fase
        pygame.mixer_music.play(SPAWN_TIME)
        # clock garante rodar na mesma taxa de atualização
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # Aditing shot in player and enemy
                if isinstance(ent,(Player,Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health:} | Score: {ent.score}' , COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health:} | Score: {ent.score} ', COLOR_CYAN, (10, 45))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                #Decrease time
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        return True




            # PRINT text, FPS, tempo e quantidade de entidades
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'intimidates: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            #Verify Collision
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
    pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

