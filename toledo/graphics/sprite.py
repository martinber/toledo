import pygame

class Sprite:
    '''
    Representa a un sprite, que vendría a ser una imagen que va a ser mostrada
    en la pantalla.

    Recomendado usar imágenes PNG de 24 o 32 bits.

    Parameters
    ----------
    image_path : str
        Path de la imagen, por ejemplo: ``"./sprites/auto.png"``.
    '''

    def __init__(self, image_path):
        self._image = pygame.image.load(image_path)


    def get_pygame_image(self):
        '''
        Devuelve la imagen o surface de ``pygame``. Normalmente no deberían usar
        esta funcion a no ser que sepan lo que hacen.

        Returns
        -------
        pygame.Surface
            Surface de ``pygame``.
        '''
        return self._image
