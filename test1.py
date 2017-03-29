'''
Este es un ejemplo de prueba para comprobar que toledo funcione bien.
'''

# importar todas mis cosas
import toledo

# crear pantalla, hay que darle el tamano de la pantalla en un vector
tamano_pantalla = [1000, 800]
screen = toledo.graphics.Screen(tamano_pantalla)

# crear un objeto que administra las imagenes y sonidos
assets = toledo.Assets()

# cargar la imagen de una pelota
assets.load_sprite("ball", "./test_assets/ball.png")
# crear un rectangulo que va a representar a la pelota, hay que darle un
# vector que es la posicion y otro que es el tamano
rect_ball = toledo.util.Rect(0, 0, 111, 111)

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

    # pintar la pantalla de negro para tapar el frame anterior, fijense que pasa
    # si borran o comentan esta linea
    screen.fill(toledo.graphics.color.BLACK)
    # dibujar la pelota en las coodenadas del rectangulo
    screen.draw(assets.get_sprite("ball"), rect_ball)
    # mostrar la pantalla
    screen.update()


# crear un controlador, es un objeto que se encarga de llamar a tus funciones en
# el momento correcto.
# sirve sobre todo para que llame a nuestro loop 60 veces por segundo
control = toledo.Controller(init=myinit, loop=myloop, fps=60)

# empieza a llamar a tus funciones, el programa entra a esta función y no sale
# hasta que se cierre el juego
control.start()
