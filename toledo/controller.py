import pygame
import sys

class Controller:

    def __init__(self, loop, fps):
        self._loop = loop
        self._fps = fps

        self._clock = pygame.time.Clock()


    def start(self):
        self._main_loop()


    def get_fps(self):
        return self._fps


    def _main_loop(self):

        while 1:
            # limitar FPS y al mismo tiempo obtener el deltatime (en ms) y
            # convertir a segundos
            dt = self._clock.tick(self._fps) / 1000

            for event in pygame.event.get():
                # si se apreto el boton de cerrar
                if event.type == pygame.QUIT:
                    sys.exit()

            self._loop(dt)
