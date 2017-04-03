import pygame

class Mouse:

    M_LEFT   = 0
    M_MIDDLE = 1
    M_RIGHT  = 2

    def get_position(self):
        return pygame.mouse.get_pos()

    def is_pressed(self, key):
        return pygame.mouse.get_pressed()[key]
