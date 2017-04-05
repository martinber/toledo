import pygame

class Rect:
    '''
    Representa a un rectángulo, tiene una posición y un tamaño.

    Parameters
    ----------
    x : int
        Posición x del borde superior izquierdo
    y : int
        Posición y del borde superior izquierdo
    w : int
        Ancho del rectángulo
    h : int
        Alto del rectángulo
    '''

    x = 0
    '''
    int : Posición x del borde superior izquierdo
    '''

    y = 0
    '''
    int : Posición y del borde superior izquierdo
    '''

    w = 0
    '''
    int : Ancho del rectángulo
    '''

    h = 0
    '''
    int : Alto del rectángulo
    '''


    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    def get_pygame_rect(self):
        '''
        Devuelve un rectángulo de tipo ``pygame.Rect`` para ser usado en
        ``pygame``

        Returns
        -------
        pygame.Rect
            Rectángulo que se puede usar en las funciones de ``pygame``
        '''
        return pygame.Rect([self.x, self.y], [self.w, self.h])
