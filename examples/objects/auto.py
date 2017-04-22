import math
import toledo
import bala


class Auto:
    '''
    Auto manejado por el jugador con las flechitas. Tira tiros cuando se apreta
    el espacio.
    '''

    def __init__(self, juego, x, y):
        '''
        Crea el auto en la posición dada.

        Debe obtener como argumento al ``Juego`` para poder obtener a los demás
        objetos, para leer el teclado, mouse, pantalla, etc.
        '''
        self.juego = juego
        self.rect = toledo.util.Rect(x, y, 50, 25)

        # angulo al cual está mirando, en grados sentido contrario agujas del
        # reloj
        self.angulo = 0

        # guarda el tiempo que falta para poder disparar en segundos (0
        # significa listo, 1.24 significa que faltan 1.24 segundos para poder
        # disparar de nuevo.
        self.reload = 0

        # velocidad en px/s
        self.velocidad = 0

        # obtener sprite
        self.sprite = juego.sprite_auto


    def loop(self, dt):
        # disminuir el tiempo de reload, ``dt`` es el tiempo pasado entre el
        # frame anterior y actual en segundos.
        self.reload -= dt

        # no dejar que ``reload`` sea menor a 0
        if self.reload < 0:
            self.reload = 0

        # moverse acorde a lo que tiene que ser
        self.mover(dt)

        # ver si estoy chocando algo
        self.checkear_colisiones()

        # guardar teclado en variable temporal porque el nombre es largo
        t = self.juego.teclado
        # ver si hay que disparar
        if t.is_pressed(t.K_SPACE):
            self.disparar()


    def dibujar(self):
        '''
        Se dibuja a si mismo
        '''
        # guardar en variable temporal porque el nombre es largo
        s = self.juego.pantalla
        s.draw(self.sprite, self.rect, self.angulo, s.ANCHOR_CENTER)


    def mover(self, dt):
        '''
        Función que calcula las físicas del auto a partir de la velocidad y las
        teclas presionadas.

        Esto podría estar en el ``loop()`` pero lo separo en otra función para
        que quede más organizado.

        Todos los cambios de velocidad, ángulo o posición dependen del dt.
        '''
        # guardar teclado en variable temporal porque el nombre es largo
        t = self.juego.teclado

        if t.is_pressed(t.K_UP):
            # acelerar
            self.velocidad += 30 * dt

        if t.is_pressed(t.K_DOWN):
            # frenar
            if self.velocidad > 0:
                self.velocidad -= 60 * dt
                # para que no haga marcha atrás, ya que está frenando
                if self.velocidad < 0:
                    self.velocidad = 0

            # marcha atrás
            else:
                self.velocidad -= 10 * dt

        # limitar velocidad
        if self.velocidad > 200:
            self.velocidad = 200
        elif self.velocidad < 50:
            self.velocidad = 50

        # doblar (cantidad proporcional a la velocidad)
        if t.is_pressed(t.K_RIGHT):
            self.angulo -= self.velocidad * dt
        if t.is_pressed(t.K_LEFT):
            self.angulo += self.velocidad * dt

        # variable temporal con angulo en radianes
        a = math.radians(self.angulo)
        # moverse en la dirección que se esta mirando
        self.rect.x += self.velocidad * math.cos(a) * dt
        self.rect.y -= self.velocidad * math.sin(a) * dt


    def disparar(self):
        '''
        Intentar disparar (antes mira si el arma está recargada).
        '''
        pass


    def checkear_colisiones(self):
        '''
        Ver si estoy chocando una bomba o si me estoy yendo de la pantalla
        '''
        pass
