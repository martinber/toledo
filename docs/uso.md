Acá pongo todas las funciones de **toledo** que por ahora necesitan

## graphics

### Color

```
color = toledo.graphics.Color()
```

Crea un objeto Color que por defecto es negro

```
color = toledo.graphics.Color.from_values(r, g, b)
```

Crea un color a partir de las componentes

### Sprite

```
sprite = toledo.graphics.Sprite(path)
```

Crea un sprite (imagen) a partir del archivo dado por el path (ej.
`"imagenes/auto.png"`)

### Screen

```
screen = toledo.graphics.Screen(size)
```

Crea una pantalla del tamaño dado en la lista (ej. [1920, 1080])

```
screen.fill(color)
```

Pinta la pantalla del color dado por el argumento. El argumento debe ser un
objeto `toledo.graphics.Color`

```
screen.draw(sprite, rect)
```

Dibuja el sprite (`toledo.graphics.Sprite`) en la posicion dada por el
rectángulo `toledo.util.Rect`. Pero la pantalla no se muestra al jugador hasta
que uno llame a la función `screen.update()`

```
screen.update()
```

Actualiza lo que ve el jugador.


## input

### Keyboard

```
keyboard = toledo.input.Keyboard()
```

Crea un objeto que se encarga del teclado

```
keyboard.is_pressed(key)
```

Devuelve `True` si la tecla está apretada o `False` en el caso contrario.

Por ahora, `key` puede ser:

```
keyboard.K_UP
keyboard.K_DOWN
keyboard.K_LEFT
keyboard.K_RIGHT
keyboard.K_SPACE
keyboard.K_RETURN
```

## Controller

```
control = toledo.Controller(init, loop, fps)
```

Crea un controlador que más tarde se va a encargar de llamar a tus funciones
(`init` y `loop`) en el momento indicado.

```
control.start()
```

Indica al controlador que empiece a trabajar. El programa entra a esa función y
no sale hasta que se cierre el juego, entonces siempre va a ser la última línea
del programa.

Cuando uno llama a esa función, el controlador va a cargar todas las imágenes
y sonidos, cuando se terminen de cargar las cosas, se va a ejecutar la función
`init()`. Después va a ejecutar la función `loop()` 60 veces por segundo para
siempre (si `fps` es igual a 60).
