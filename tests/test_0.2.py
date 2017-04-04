'''
Este es un ejemplo de prueba para comprobar que toledo funcione bien.

Se prueban las funciones de toledo 0.2:

    - Crear pantalla
    - Cargar sprites
    - El controlador
    - Pintar y actualizar la pantalla

    Nuevo:

    - Leer el mouse (solamente polling)
    - Dibujar sprites (rotados y escalados)
    - Dibujar sprites con anchor en top-left o center
    - Deltatime
'''

# TODO: Mejor ejemplo

# ignoren esto
import sys
sys.path.append("../")

# importar toledo
import toledo

# crear pantalla, hay que darle el tamano de la pantalla en un vector
tamano_pantalla = [1000, 800]
screen = toledo.graphics.Screen(tamano_pantalla)

# crear objeto que maneja todo lo que sea teclado y otro para el mouse
keyboard = toledo.input.Keyboard()
mouse = toledo.input.Mouse()

# cargar la imagen de una pelota
sprite_ball = toledo.graphics.Sprite("./test_assets/ball.png")
# crear un rectangulo que va a representar a la pelota, hay que darle un
# vector que es la posicion y otro que es el tamano
rect_ball = toledo.util.Rect(0, 0, 111, 111)
# otro para otra pelota más
rect_ball_2 = toledo.util.Rect(0, 0, 111, 111)
# crear una variable que representa el ángulo de rotacion
angle_ball = 0

def myloop(dt):
    '''
    Esta funcion es llamada por el controlador 60 veces por segundo. Además
    es pasado un argumento que es el tiempo pasado entre este frame y el
    anterior en segundos
    '''
    global angle_ball

    x, y = mouse.get_position()
    rect_ball.x = x
    rect_ball.y = y

    if keyboard.is_pressed(keyboard.K_UP):
        rect_ball.h -= 200 * dt
        rect_ball_2.y -= 200 * dt
    if keyboard.is_pressed(keyboard.K_DOWN):
        rect_ball.h += 200 * dt
        rect_ball_2.y += 200 * dt
    if keyboard.is_pressed(keyboard.K_LEFT):
        rect_ball.w -= 200 * dt
        rect_ball_2.x -= 200 * dt
    if keyboard.is_pressed(keyboard.K_RIGHT):
        rect_ball.w += 200 * dt
        rect_ball_2.x += 200 * dt

    if mouse.is_pressed(mouse.M_LEFT):
        angle_ball += 80 * dt
    if mouse.is_pressed(mouse.M_RIGHT):
        angle_ball -= 80 * dt

    # pintar la pantalla de negro para tapar el frame anterior, fijense que pasa
    # si borran o comentan esta linea
    screen.fill(toledo.graphics.color.BLACK)
    # dibujar las pelotas en las coodenadas del rectangulo y con la rotación
    # dada
    screen.draw(sprite_ball, rect_ball, angle_ball, anchor=screen.ANCHOR_CENTER, smooth=True)
    screen.draw(sprite_ball, rect_ball, angle_ball, anchor=screen.ANCHOR_TOP_LEFT, smooth=True)
    screen.draw(sprite_ball, rect_ball_2)
    # mostrar la pantalla
    screen.update()


# crear un controlador, es un objeto que se encarga de llamar a tus funciones en
# el momento correcto.
# sirve sobre todo para que llame a nuestro loop 60 veces por segundo
control = toledo.Controller(myloop, 60)

# empieza a llamar a tus funciones, el programa entra a esta función y no sale
# hasta que se cierre el juego
control.start()
