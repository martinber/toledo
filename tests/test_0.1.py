'''
Este es un ejemplo de prueba para comprobar que toledo funcione bien.

Se prueban las funciones de toledo 0.1:

    - Crear pantalla
    - Cargar sprites
    - Leer el teclado (solamente polling)
    - El controlador
    - Pintar y actualizar la pantalla
    - Dibujar sprites (sin rotar ni escalar)
'''

# ignoren esto
import sys
sys.path.append("../")

# importar toledo
import toledo

# crear pantalla, hay que darle el tamano de la pantalla en un vector
tamano_pantalla = [1000, 800]
screen = toledo.graphics.Screen(tamano_pantalla)

# crear objeto que maneja todo lo que sea teclado
keyboard = toledo.input.Keyboard()

# cargar la imagen de una pelota
sprite_ball = toledo.graphics.Sprite("./test_assets/ball.png")
# crear un rectangulo que va a representar a la pelota, (x, y, w, h)
rect_ball = toledo.util.Rect(0, 0, 111, 111)

def myloop(dt):
    '''
    Esta funcion es llamada por el controlador 60 veces por segundo.
    '''

    if keyboard.is_pressed(keyboard.K_UP):
        rect_ball.y -= 5
    if keyboard.is_pressed(keyboard.K_DOWN):
        rect_ball.y += 5
    if keyboard.is_pressed(keyboard.K_LEFT):
        rect_ball.x -= 5
    if keyboard.is_pressed(keyboard.K_RIGHT):
        rect_ball.x += 5

    # pintar la pantalla de negro para tapar el frame anterior, fijense que pasa
    # si borran o comentan esta linea
    screen.fill(toledo.graphics.Color.from_name("black"))
    # dibujar la pelota en las coodenadas del rectangulo
    screen.draw(sprite_ball, rect_ball)
    # mostrar la pantalla
    screen.update()


# crear un controlador, es un objeto que se encarga de llamar a tus funciones en
# el momento correcto.
# sirve sobre todo para que llame a nuestro loop 60 veces por segundo
control = toledo.Controller(myloop, 60)

# empieza a llamar a tus funciones, el programa entra a esta función y no sale
# hasta que se cierre el juego
control.start()
