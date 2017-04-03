import pygame

class Screen:

    ANCHOR_TOP_LEFT = 0
    ANCHOR_CENTER   = 1

    def __init__(self, size):
        self._screen = pygame.display.set_mode(size)


    def fill(self, color):
        self._screen.fill(color.get_components())


    def draw(self, sprite, rect, smooth=False, anchor=None):
        image = sprite.get_pygame_image()
        image = self._scale_image(image, rect, smooth)


        # TODO: Mover a otra funcion
        if anchor == None:
            anchor = self.ANCHOR_TOP_LEFT
        if anchor == self.ANCHOR_CENTER:
            pos = (rect.x - abs(rect.w) / 2,
                   rect.y - abs(rect.h) / 2)
        elif anchor == self.ANCHOR_TOP_LEFT:
            pos = (rect.x, rect.y)
        else:
            print("ERROR")


        self._screen.blit(image, pos)

    def draw_rotated(self, sprite, rect, angle,
                     smooth=False, anchor=None):

        # TODO: ROtado de imagenes y su calculo de anchor
        self.draw(sprite, rect, smooth, anchor)


    def update(self):
        pygame.display.flip()


    def _scale_image(self, image, rect, smooth):
        size = [int(rect.w), int(rect.h)]

        if size[0] < 0:
            size[0] *= -1
            image = pygame.transform.flip(image, True, False)
        if size[1] < 0:
            size[1] *= -1
            image = pygame.transform.flip(image, False, True)

        if smooth:
            return pygame.transform.smoothscale(image, size)
        else:
            return pygame.transform.scale(image, size)
