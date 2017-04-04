import pygame

class Sprite:

    def __init__(self, image_path):
        self._image = pygame.image.load(image_path)


    def get_pygame_image(self):
        return self._image
