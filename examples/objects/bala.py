import toledo
import math
import bomba


class Bala:
    '''
    Una bala que viaja el linea recta hasta chocar contra una bomba o hasta
    salirse de la pantalla.
    '''

    def __init__(self, juego, x, y, velocidad, direccion):
        '''
        Crear la bala
        '''
        self.juego = juego
        self.velocidad = velocidad
        self.direccion = direccion

        self.rect = toledo.util.Rect(x, y, 8, 8)

        self.sprite = juego.sprite_bala


    def loop(self, dt):
        '''
        Moverse acorde al dt, ángulo y velocidad.
        '''
        # variable temporal con angulo en radianes
        a = math.radians(self.direccion)
        # moverse en la dirección que se esta mirando
        self.rect.x += self.velocidad * math.cos(a) * dt
        self.rect.y -= self.velocidad * math.sin(a) * dt

        # ver si hay colisiones
        self.checkear_colisiones()


    def dibujar(self):
        '''
        Dibujarse a si mismo.
        '''
        # guardar en variable temporal porque el nombre es largo
        s = self.juego.pantalla
        s.draw(self.sprite, self.rect, anchor=s.ANCHOR_CENTER)


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
                if distancia < 16: # suma de radios de 25/2 y 8/2
                    # borrarse a si mismo y a la bomba
                    self.juego.mundo.eliminar(self)
                    self.juego.mundo.eliminar(objeto)

        # ver si se va de la pantalla
        if self.rect.x < 0:
            self.juego.mundo.eliminar(self)
        if self.rect.y < 0:
            self.juego.mundo.eliminar(self)
        if self.rect.x > self.juego.tamano_pantalla[0]:
            self.juego.mundo.eliminar(self)
        if self.rect.y > self.juego.tamano_pantalla[1]:
            self.juego.mundo.eliminar(self)
