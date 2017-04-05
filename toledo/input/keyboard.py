import pygame

class Keyboard:
    '''
    Representa al teclado y tiene todo lo necesario para leerlo.

    Más abajo se pueden ver las constantes que se pueden usar. Cada una
    representa a una tecla. Tienen los mismos valores y nombres que los de
    ``pygame``.
    '''

    # Por ahora hardcodeo esto así, solamente las flechitas y algunas mas, pero
    # despues lo voy a mejorar
    K_UP = pygame.K_UP
    K_DOWN = pygame.K_DOWN
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT
    K_SPACE = pygame.K_SPACE
    K_RETURN = pygame.K_RETURN

    def is_pressed(self, key):
        '''
        Devuelve ``True`` si la tecla está apretada y ``False`` en caso
        contrario.

        Examples
        --------
        ::

            keyb = toledo.input.Keyboard()
            ...
            if keyb.is_pressed(keyb.K_UP):
                print("Flecha arriba está presionada en este momento")

        Parameters
        ----------
        key : int
            Código de la tecla a la que se le quiere conocer el estado. Usar las
            constantes definidas en esta clase.

        Returns
        -------
        bool
            ``True`` si la tecla está apretada y ``False`` en caso contrario.
        '''
        keys = pygame.key.get_pressed()

        return keys[key]
