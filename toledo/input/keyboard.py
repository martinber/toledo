import pygame

class Keyboard:

    # Por ahora hardcodeo esto así, solamente las flechitas y algunas mas, pero
    # despues lo voy a mejorar
    K_UP = pygame.K_UP
    K_DOWN = pygame.K_DOWN
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT
    K_SPACE = pygame.K_SPACE
    K_RETURN = pygame.K_RETURN

    def is_pressed(self, key):
        keys = pygame.key.get_pressed()

        return keys[key]
