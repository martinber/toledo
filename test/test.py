'''
Este es un ejemplo de prueba para comprobar que toledo funcione bien.
'''

# importar todas mis cosas
import ../toledo

# crear pantalla, hay que darle el tamano de la pantalla en un vector
tamano_pantalla = [1000, 800]
screen = toledo.graphics.Screen(tamano_pantalla)

# crear objetos que manejan todo lo que sea mouse y teclado
keyboard = toledo.input.Keyboard()
mouse = toledo.input.Mouse()

# crear un objeto que administra las imagenes y sonidos
assets = toledo.Assets()

# cargar la imagen de una pelota
im_pelota = assets.load_sprite("ball.png")
# crear un rectangulo que va a representar a la pelota, hay que darle un
# vector que es la posicion y otro que es el tamano
rect_pelota = toledo.utils.Rect([0, 0], [111, 111])

# crear un controlador, es un objeto que se encarga de llamar a tus funciones en
# el momento correcto.
# sirve sobre todo para que llame a nuestro loop 60 veces por segundo
control = toledo.Controller(init=myinit(), loop=myloop(), fps=60)

# empieza a llamar a tus funciones, el programa entra a esta función y no sale
# hasta que se cierre el juego
control.start()

def myinit():
    '''
    Esta funcion es llamada por el controlador cuando se terminan de cargar los
    assets.
    '''
    print("Empezó el juego!")

def myloop():
    '''
    Esta funcion es llamada por el controlador 60 veces por segundo.
    '''

    if keyboard.is_pressed(keyboard.K_UP):
        rect_pelota.y -= 5
    if keyboard.is_pressed(keyboard.K_DOWN):
        rect_pelota.y += 5
    if keyboard.is_pressed(keyboard.K_LEFT):
        rect_pelota.x -= 5
    if keyboard.is_pressed(keyboard.K_RIGHT):
        rect_pelota.x += 5

    # ver si la pelota se fue afuera de la pantalla
    if rect_pelota.x < 0:
        rect_pelota.x = 0
    if rect_pelota.y < 0:
        rect_pelota.y = 0
    if rect_pelota.x + rect_pelota.w > tamano_pantalla[0]:
        rect_pelota.x = tamano_pantalla[0] - rect_pelota.w
    if rect_pelota.y + rect_pelota.h > tamano_pantalla[1]:
        rect_pelota.y = tamano_pantalla[1] - rect_pelota.h

    # pintar la pantalla de negro para tapar el frame anterior, fijense que pasa
    # si borran o comentan esta linea
    screen.fill(toboso.graphics.color.BLACK)
    # dibujar la pelota en las coodenadas del rectangulo
    screen.draw(im_pelota, rect_pelota)
    # mostrar la pantalla
    screen.update()
