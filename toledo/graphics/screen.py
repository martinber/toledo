import pygame
import math

class Screen:
    '''
    Se encarga de controlar lo que ve el jugador en la pantalla.

    Primero se debe crear una instancia de este objeto, luego, en cada loop del
    juego uno debe (en orden):

    - Pintar la pantalla con ``fill()`` para tapar el frame anterior.
    - Dibujar todos los sprites con ``draw()``.
    - Actualizar la pantalla con ``update()``.
    '''

    ANCHOR_TOP_LEFT = 0
    ANCHOR_CENTER   = 1

    def __init__(self, size):
        '''
        Crear una pantalla a partir de un tamaño.

        Parameters
        ----------
        size : List[int]
            Tamaño de la pantalla, ``[w, h]``.
        '''
        self._screen = pygame.display.set_mode(size)


    def fill(self, color):
        '''
        Pintar la pantalla completamente de un color.

        Parameters
        ----------
        color : toledo.graphics.Color
            Color a usar.
        '''
        self._screen.fill(color.get_components())


    def draw(self, sprite, rect, angle=0, smooth=False, anchor=None):
        '''
        Dibujar un sprite en la pantalla.

        No se verán los cambios hasta que se llame a la función
        ``Screen.update()``.

        Parameters
        ----------
        sprite : toledo.graphics.Sprite
            Sprite a dibujar.
        rect : toledo.Rect
            Posición en la pantalla en donde dibujar. Se respeta el tamaño dado.
        angle : :obj:`float`, optional
            Ángulo de rotación en grados, sentido contrario a las agujas del
            reloj.
        smooth : :obj:`bool`, optional
            Si usar o no antialiasing.
        anchor : :obj:`int`, optional
            Tipo de anclaje a usar, (por ej. si centrado o esquinado). Usar las
            constantes definidas. Ej: ``Screen.ANCHOR_CENTER`` o
            ``Screen.ANCHOR_TOP_LEFT``.
            Por defecto es un anclaje top-left.

        Examples
        --------
        ::

            screen = toledo.graphics.Screen(screen_size)
            ...
            def loop():
                ...
                screen.draw(sprite_ball, rect_ball, angle=angle_ball,
                            smooth=True, anchor=screen.ANCHOR_TOP_LEFT)

        '''
        image = sprite.get_pygame_image()
        size = [int(rect.w), int(rect.h)]
        angle = angle % 360

        if size[0] == 0 or size[1] == 0:
            return

        pos = self._get_pos(rect, angle, anchor)
        # el orden importa
        image = self._scale_image(image, size, smooth)
        image = self._rotate_image(image, angle, smooth)

        self._screen.blit(image, pos)

    def update(self):
        '''
        Actualiza lo que se ve en pantalla.
        '''
        pygame.display.flip()


    def _scale_image(self, image, size, smooth):
        '''
        Escalar imagen al tamaño dado.

        Parameters
        ----------
        image : pygame.Surface
            Imagen a escalar.
        size : List[int]
            Tamaño a escalar, ``[w, h]``.
        smooth : bool
            Si usar o no antialiasing.

        Returns
        -------
        pygame.Surface
            Imagen escalada.
        '''
        # hacer copia para no modificar la lista original
        size = size[:]

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

    def _rotate_image(self, image, angle, smooth):
        '''
        Rotar imagen al ángulo dado.

        Parameters
        ----------
        image : pygame.Surface
            Imagen a escalar.
        angle : float
            Ángulo de rotación en grados, sentido contrario a las agujas del
            reloj.
        smooth : bool
            Si usar o no antialiasing.

        Returns
        -------
        pygame.Surface
            Imagen rotada.
        '''
        if smooth:
            return pygame.transform.rotozoom(image, angle, 1)
        else:
            return pygame.transform.rotate(image, angle)


    def _get_pos(self, rect, angle, anchor):
        '''
        Calcular la posición correcta en donde dibujar la textura. ``pygame``
        necesita la posición de la esquina superior izquierda.

        Implementa el comportamiento de los anchors.

        Parameters
        ----------
        rect : toledo.Rect
            Posición y tamaño de la imagen dada por el usuario (no es el tamaño
            final luego de la rotación).
        angle : float
            Ángulo de rotación en grados, sentido contrario a las agujas del
            reloj.
        anchor : int
            Tipo de anclaje a usar.

        Returns
        -------
        List[int]
            Posición en la cual hay que dibujar la imagen con ``pygame`` para
            que quede en la posición correcta. ``[x, y]``.
        '''
        pos = [None, None]
        angle_rads = math.radians(angle)
        # calcular tamaño de la imagen ya rotada, siempre positivo. Puede que
        # haya una mejor forma pero funciona
        rotated_size = [
            abs(abs(rect.w) * math.cos(angle_rads)) + abs(abs(rect.h) * math.sin(angle_rads)),
            abs(abs(rect.h) * math.cos(angle_rads)) + abs(abs(rect.w) * math.sin(angle_rads))
        ]

        if anchor == None:
            anchor = self.ANCHOR_TOP_LEFT

        if anchor == self.ANCHOR_CENTER:
            pos = [rect.x - rotated_size[0] / 2,
                   rect.y - rotated_size[1] / 2]
        elif anchor == self.ANCHOR_TOP_LEFT:
            # corrección para imagenes rotadas. También puede que haya una mejor
            # forma
            if angle > 0 and angle <= 90:
                correction = [
                    0,
                    abs(abs(rect.w) * math.sin(angle_rads))
                ]
            elif angle > 90 and angle <= 180:
                correction = [
                    abs(abs(rect.w) * math.cos(angle_rads)),
                    rotated_size[1]
                ]
            elif angle > 180 and angle <= 270:
                correction = [
                    rotated_size[0],
                    abs(abs(rect.h) * math.cos(angle_rads)),
                ]
            else:
                correction = [
                    abs(abs(rect.h) * math.sin(angle_rads)),
                    0
                ]

            # cuando el ancho es negativo, el borde izquierdo pasa a ser el que
            # originalmente era el derecho
            if rect.w < 0:
                pos[0] = rect.x - abs(rect.w)
            else:
                pos[0] = rect.x - correction[0]
            # lo mismo para el borde superior
            if rect.h < 0:
                pos[1] = rect.y - abs(rect.h)
            else:
                pos[1] = rect.y - correction[1]
        else:
            print("ERROR")

        return pos
