Este es un framework, que es algo así como un conjunto de cosas (funciones,
objetos) que tienen todo lo que haga falta para hacer un juego.

En vez de usar **pygame** directamente, uno usa a **toledo**. **toledo** se
encarga de hacer todo (a escondidas usa **pygame** pero no te importa).

Lo hago porque a veces **pygame** es difícil de usar o porque le faltan cosas.

Actualmente la versión es **toledo 0.1**

# Ejemplos

Ver los ejemplos en la carpeta `tests`. Hay un ejemplo para cada versión de
toledo.

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
- Delta-time (creo que con esto se soluciona el stuttering)
- ???

# TODO

- Eventos
- Excepciones
- Sonidos
