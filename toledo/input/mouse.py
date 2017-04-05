import pygame

class Mouse:
    '''
    Representa al mouse y tiene todo lo necesario para leerlo.

    Más abajo se pueden ver las constantes que se pueden usar. Cada una
    representa a un botón.
    '''

    M_LEFT   = 0
    M_MIDDLE = 1
    M_RIGHT  = 2

    def get_position(self):
        '''
        Devuelve un tuple conteniendo la posición ``(x, y)`` del mouse.

        Si el mouse está fuera de la ventana, se devuelve la última posición
        conocida antes de que éste se haya ido fuera de la ventana.

        Returns
        -------
        Tuple[int]
            Tuple con la posición ``(x, y)`` actual del mouse.
        '''
        return pygame.mouse.get_pos()


    def is_pressed(self, button):
        '''
        Devuelve ``True`` si el botón está apretado y ``False`` en caso
        contrario.

        Examples
        --------
        ::

            mouse = toledo.input.Keyboard()
            ...
            if mouse.is_pressed(mouse.M_LEFT):
                print("El botón izquierdo está presionado")

        Parameters
        ----------
        button : int
            Código de la tecla a la que se le quiere conocer el estado. Usar las
            constantes definidas en esta clase.

        Returns
        -------
        bool
            ``True`` si el botón está apretado y ``False`` en caso contrario.
        '''
        return pygame.mouse.get_pressed()[button]
