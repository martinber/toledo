import math
import toledo
import bomba


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

        # setear variables
        self.maxvel = 200
        self.minvel = -100 # marcha atrás
        self.aceleracion = 130
        self.freno = -300
        self.marcha_atras = -90
        self.rozamiento = 50


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
        s.draw(self.sprite, self.rect, self.angulo, anchor=s.ANCHOR_CENTER)


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
            # frenar
            if self.velocidad < 0:
                self.velocidad -= self.freno * dt
                # para que no haga hacia delante, ya que está frenando
                if self.velocidad > 0:
                    self.velocidad = 0

            # acelerar
            else:
                self.velocidad += self.aceleracion * dt

        if t.is_pressed(t.K_DOWN):
            # frenar
            if self.velocidad > 0:
                self.velocidad += self.freno * dt
                # para que no haga marcha atrás, ya que está frenando
                if self.velocidad < 0:
                    self.velocidad = 0

            # marcha atrás
            else:
                self.velocidad += self.marcha_atras * dt

        # aplicar rozamiento
        if self.velocidad > 0:
            self.velocidad -= self.rozamiento * dt
            # para que se pase para el otro lado
            if self.velocidad < 0:
                self.velocidad = 0
        else:
            self.velocidad += self.rozamiento * dt
            # para que se pase para el otro lado
            if self.velocidad > 0:
                self.velocidad = 0


        # limitar velocidad
        if self.velocidad > self.maxvel:
            self.velocidad = self.maxvel
        elif self.velocidad < self.minvel:
            self.velocidad = self.minvel

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
        print("a")
        self.juego.mundo.eliminar(self)


    def checkear_colisiones(self):
        '''
        Ver si estoy chocando una bomba o si me estoy yendo de la pantalla
        '''
        # mirar todos los objetos del mundo
        objetos = self.juego.mundo.objetos
        for objeto in objetos:
            # si el objeto es una bomba
            if type(objeto) is bomba.Bomba:
                # ver si hay colision
                distancia_x = abs(self.rect.x - objeto.rect.x)
                distancia_y = abs(self.rect.y - objeto.rect.y)
                distancia = math.sqrt(distancia_x**2 + distancia_y**2)
                if distancia < 25: # suma de ambos radios de 25/2
                    # borrarse a si mismo y a la bomba
                    self.juego.mundo.eliminar(self)
                    self.juego.mundo.eliminar(objeto)

        # ver si se va de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
            self.velocidad = 0
        if self.rect.y < 0:
            self.rect.y = 0
            self.velocidad = 0
        if self.rect.x > self.juego.tamano_pantalla[0]:
            self.rect.x = self.juego.tamano_pantalla[0]
            self.velocidad = 0
        if self.rect.y > self.juego.tamano_pantalla[1]:
            self.rect.y = self.juego.tamano_pantalla[1]
            self.velocidad = 0


