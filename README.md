Este es un framework, que es algo así como un conjunto de cosas (funciones,
objetos) que tienen todo lo que haga falta para hacer un juego.

En vez de usar **pygame** directamente, uno usa a **toledo**. **toledo** se
encarga de hacer todo (a escondidas usa **pygame** pero no te importa).

Lo hago porque a veces **pygame** es difícil de usar o porque le faltan cosas.

Actualmente la versión es **toledo 0.2**

# Ejemplos

Ver los ejemplos en la carpeta `tests`. Hay un ejemplo para cada versión de
toledo.

# Notas

- Por ahora antes de que correr los ejemplos hay que hacer `cd` a la carpeta
- Para poder escalar/rotar imágenes con antialiasing, las imágenes deben ser de
    32 o 34 bits
- Suele tirar segfault cuando el tamaño de la imagen es de 0px (creo)
- No dibujen imágenes rotadas **y** escaladas negativamente **con** anclaje
    top-left. Esa combinación no anda, pero pueden hacer esas cosas por separado
    o dos de esas cosas al mismo tiempo, pero las tres juntas no. Es porque no
    me puse a hacer la matemática para ese caso.
- Tenemos problemas de stuttering culpa de `pygame`/`sdl`. Si uso otro método
    gasto mucha CPU, por ahora lo dejo así.
- Hay problemas de rendmimiento cuando escalo las texturas muy grandes. No se si
    es problema de escalado o de dibujado de texturas grandes.
- Los sprites vibran mucho cuando son rotados debido a redondeos, no sé como
    solucionar eso.

# Cambios

## toledo 0.1

- Crear pantalla
- Cargar sprites
- Leer el teclado (solamente polling)
- El controlador
- Pintar y actualizar la pantalla
- Dibujar sprites (sin rotar ni escalar)

## toledo 0.2

- Leer el mouse (solamente polling)
- Dibujar sprites (rotados y escalados)
- Dibujar sprites con anchor en _center_ o _top-left_
- Deltatime

## toledo 0.3

- Documentación
- Más teclas para el teclado
- ???

# TODO

- Eventos
- Excepciones
- Sonidos
- Documentacion
