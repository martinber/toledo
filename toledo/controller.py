import pygame
import sys

class Controller:
    '''
    Objeto que se encarga del flujo del programa, del loop principal.

    Llama a la función dada un cierto número de veces por segundo implementando
    un loop. Además chequea si el juego está siendo cerrado por el usuario
    leyendo los eventos de ``pygame``.

    Se debe llamar a la función ``start()`` que comienza el loop principal.

    Examples
    --------
    ::

        def loop(dt):
            print("Tiempo entre frame actual y anterior en segundos:", dt)

        control = toledo.Controller(loop, 60)
        control.start()

        print("El juego se está cerrando")

    Parameters
    ----------
    loop : Callable[[float], [None]]
        Función a llamar varias veces por segundo. La función debe aceptar un
        argumento numérico que es el deltatime entre el frame actual y el
        anterior.
    fps : float
        Número de veces por segundo que se llamará a la función dada.
    '''

    def __init__(self, loop, fps):
        self._loop = loop
        self._fps = fps

        self._clock = pygame.time.Clock()


    def start(self):
        '''
        Comenzar a llamar a la función dada.

        Una vez que el programa entra a esta función, no continúa hasta que se
        cierre el juego. Entonces el código que esté después de esta llamada se
        ejecutará recién en el cierre del juego.

        Detecta cuando el jugador cierra el juego y termina la ejecución del
        loop.
        '''
        self._main_loop()


    def get_fps(self):
        '''
        Devuelve el parámetro ``fps`` dado en el constructor.

        Returns
        -------
        float
            FPS que se están respetando actualmente.
        '''
        return self._fps


    def _main_loop(self):

        while 1:
            # limitar FPS y al mismo tiempo obtener el deltatime (en ms) y
            # convertir a segundos
            dt = self._clock.tick(self._fps) / 1000

            for event in pygame.event.get():
                # si se apreto el boton de cerrar
                if event.type == pygame.QUIT:
                    sys.exit()

            self._loop(dt)
