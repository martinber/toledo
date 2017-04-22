'''
Este es un ejemplo de como usar objetos.

Es buena idea no usar variables globales, conviene que todas las variables
pertenezcan a un objeto. Los objetos que se van a usar son:

* Juego: Este es la base de todo, contiene todas las cosas.
* Mundo: Este objeto contiene a todos los objetos que están en el juego. Es como
  un nivel del juego.
* Bomba: Una bomba que se mueve por todos lados y explota en contacto con el
  auto
* Auto: Un autito controlado por el jugador que tira tiros
* Bala: Una bala disparada por el auto

En este archivo lo único que hacemos es crear el objeto *juego* y le decimos que
empiece. De esta forma la única variable global que existe es ``juego``.
'''

import toledo
import juego

juego = juego.Juego()
juego.iniciar()

