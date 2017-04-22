import toledo

import auto
import bomba
import bala

class Mundo:
    '''
    Este objeto representa a un mundo, que sería un nivel del juego, aunque este
    juego tiene un solo nivel y por lo tanto un solo mundo.

    Contiene todos los objetos del nivel y se encarga de coordinarlos, lo que
    este objeto tiene que hacer es llamar a la función ``loop()`` de cada objeto
    de la pantalla y además tiene que dibujar a todos ellos.
    '''

    def __init__(self, juego):
        '''
        Construye al mundo.

        Crea todos los objetos que van a aparecer apenas empieza el nivel/juego.
        '''
        self.juego = juego

        # lista con todos los objetos del mundo
        self.objetos = []

        # crear objetos y agregarlos a la lista
        self.objetos.append(auto.Auto(self.juego, 100, 100)) # crear auto
        for i in range(10): # para crear 10 bombas
            self.objetos.append(bomba.Bomba(juego)) # bomba en posición aleatoria

        # cargar fondo y un rectángulo que dice donde se dibujará
        self.sprite_fondo = juego.sprite_fondo
        self.rect_fondo = toledo.util.Rect(
                0, 0, juego.tamano_pantalla[0], juego.tamano_pantalla[1])
        

    def loop(self, dt):

        # llamar al loop de todos los objetos
        for objeto in self.objetos:
            objeto.loop(dt)

        # una vez que se haya llamado al ``loop()`` de todos los objetos
        # dibujamos a todos, pero primero dibujamos al fondo para que quede
        # abajo.
        # en juegos más complejos deberíamos llamar al ``dibujar()`` de cada
        # objeto en un orden determinado porque los últimos objetos se dibujan
        # arriba.
        self.juego.pantalla.draw(self.sprite_fondo, self.rect_fondo)
        for objeto in self.objetos:
            objeto.dibujar()
        self.juego.pantalla.update()


    def eliminar(self, objeto):
        '''
        Borrar del mundo al objeto dado.

        Buscar al objeto dado en la lista de objetos, y al encontrarlo sacarlo
        de la lista.
        '''
        for i in range(len(self.objetos)):
            if objeto is self.objetos[i]:
                self.objetos.pop(i)
                break
