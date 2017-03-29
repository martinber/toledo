import pygame

class Screen:


    def __init__(self, size):
        self._screen = pygame.display.set_mode(size)


    def fill(self, color):
        self._screen.fill(color.get_components())


    def draw(self, sprite, rect):
        self._screen.blit(sprite.get_pygame_image(),
                          rect.get_pygame_rect())


    def update(self):
        pygame.display.flip()
