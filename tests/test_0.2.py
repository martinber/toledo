'''
Este es un ejemplo de prueba para comprobar que toledo funcione bien.

Se prueban las funciones de toledo 0.2:

    Viejo:

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

# ignoren esto
import sys
sys.path.append("../")

import toledo

screen_size = [1000, 800]
screen = toledo.graphics.Screen(screen_size)

keyboard = toledo.input.Keyboard()
# objeto que maneja todo lo que sea el mouse
mouse = toledo.input.Mouse()

sprite_ball = toledo.graphics.Sprite("./test_assets/ball.png")

# pelota que se va a mover con el mouse
rect_ball = toledo.util.Rect(0, 0, 111, 111)
# pelota fija que va a girar respecto de su centro
rect_ball_2 = toledo.util.Rect(400, 500, 111, 111)
# pelota fija que va a girar respecto a su borde superior izquierdo
rect_ball_3 = toledo.util.Rect(700, 500, 111, 111)

# angulo de rotación en grados de las pelotas
angle_ball = 0

def myloop(dt):
    '''
    Ahora recibe un parámetro dt que es el deltatime, el tiempo que pasó entre
    el frame anterior y el actual. Se usa para calcular los movimientos de una
    forma independiente al framerate.
    '''
    # por culpa de python, ignoren esto
    global angle_ball

    # obtener la posición del mouse y usarlo para mover la pelota
    x, y = mouse.get_position()
    rect_ball.x = x
    rect_ball.y = y

    # con las flechas escalar las imágenes
    if keyboard.is_pressed(keyboard.K_UP):
        rect_ball_2.h -= 200 * dt
        rect_ball_3.h -= 200 * dt
    if keyboard.is_pressed(keyboard.K_DOWN):
        rect_ball_2.h += 200 * dt
        rect_ball_3.h += 200 * dt
    if keyboard.is_pressed(keyboard.K_LEFT):
        rect_ball_2.w -= 200 * dt
        rect_ball_3.w -= 200 * dt
    if keyboard.is_pressed(keyboard.K_RIGHT):
        rect_ball_2.w += 200 * dt
        rect_ball_3.w += 200 * dt

    # con los botones del mouse rotar las imágenes
    if mouse.is_pressed(mouse.M_LEFT):
        angle_ball += 80 * dt
    if mouse.is_pressed(mouse.M_RIGHT):
        angle_ball -= 80 * dt

    screen.fill(toledo.graphics.Color.from_name("black"))

    # dibujar la pelota normalmente
    screen.draw(sprite_ball, rect_ball)
    # dibujar la pelota con rotación y respecto a su centro
    screen.draw(sprite_ball, rect_ball_2, angle_ball,
                anchor=screen.ANCHOR_CENTER, smooth=True)
    # dibujar la pelota con rotación y respecto a su esquina superior izquieda
    screen.draw(sprite_ball, rect_ball_3, angle_ball,
                anchor=screen.ANCHOR_TOP_LEFT, smooth=True)

    screen.update()


control = toledo.Controller(myloop, 60)
control.start()
