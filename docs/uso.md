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
rectángulo `toledo.util.Rect`

```
screen.update()
```

Actualiza lo que ve el jugador


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

## Assets

```
assets = toledo.Assets()
```

Crea un objeto que se encarga de guardar todos los sprites que necesitas

```
assets.load_sprite(name, path)
```

Crea un sprite a partir del archivo ubicado en el path y lo guarda con el nombre
dado

```
assets.get_sprite(name)
```

Devuelve el sprite guardado con ese nombre

## Controller

```
control = toledo.Controller(init, loop, fps)
```

Crea un controlador que llama a las funciones en el momento indocado
