import os
import toledo
import mundo

class Juego:
    '''
    Este es un objeto que contiene al mundo. Se encarga de guardar todo lo que
    se necesite:

    * El mundo.
    * Controladores de pantalla, teclado y mouse.
    * El loop principal.
    * Sprites.
    
    Solamente puede haber una sola instancia de este objeto. No tiene sentido
    tener dos juegos. La idea es que este objeto se puede extender cuando uno
    necesite hacer varios niveles (que supone tener varios mundos), pero por
    ahora es como un objeto base que guarda todo y que no hace muchas cosas.
    '''

    def iniciar(self):
        '''
        Inicializa todo y comienza el juego.

        Crea un mundo, una pantalla, controlador de teclado, mouse y carga los
        sprites. Después inicia el controlador de toledo para empezar el loop.
        '''

        self.tamano_pantalla = [800, 600]
        self.pantalla = toledo.graphics.Screen(self.tamano_pantalla)

        self.teclado = toledo.input.Keyboard()
        self.mouse = toledo.input.Mouse()

        # cargar sprites
        self.path_assets = os.path.dirname(__file__) + "/assets"
        self.sprite_fondo = toledo.graphics.Sprite(
                self.path_assets + "/fondo.png")
        self.sprite_auto = toledo.graphics.Sprite(
                self.path_assets + "/jeep.png")
        self.sprite_bomba = toledo.graphics.Sprite(
                self.path_assets + "/bomba.png")
        self.sprite_bala = toledo.graphics.Sprite(
                self.path_assets + "/bala.png")


        # crear el mundo, como argumento lleva el juego, que es ``self``
        self.mundo = mundo.Mundo(self)

        # crear el controlador y decirle que llame al loop que pertenece a este
        # objeto
        control = toledo.Controller(self.loop, 60)
        control.start()


    def loop(self, dt):
        '''
        Loop principal del juego.

        En realidad no hace nada, lo único que hace es llamar al loop del mundo.

        Si este juego tuviera varios niveles, tendríamos a varios mundos y acá
        llamaríamos al mundo correcto y haríamos cosas para cambiar de nivel,
        etc.
        '''
        self.mundo.loop(dt)

