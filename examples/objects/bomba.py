import random
import toledo


class Bomba:
    '''
    Es una bomba que se puede romper con una bala o que explota cuando choca con
    el auto
    '''

    def __init__(self, juego):
        '''
        Crea la bomba en un lugar aleatorio de la pantalla
        '''

        self.juego = juego

        # crear rectangulo con posicion aleatoria
        x = random.randrange(0, juego.tamano_pantalla[0])
        y = random.randrange(0, juego.tamano_pantalla[1])
        self.rect = toledo.util.Rect(x, y, 25, 25)

        # cargar sprite
        self.sprite = self.juego.sprite_bomba


    def loop(self, dt):
        '''
        En realidad la bomba no hace nada en su loop, pero hay que definir la
        función de todas formas.
        '''
        pass


    def dibujar(self):
        '''
        Dibujarse a si mismo.
        '''
        # guardar en variable temporal porque el nombre es largo
        s = self.juego.pantalla
        s.draw(self.sprite, self.rect, anchor=s.ANCHOR_CENTER)

