

def Controller:

    def __init__(self, init, loop, fps):
        self._init = init
        self._loop = loop
        self._fps = fps

        self._clock = pygame.time.Clock()


    def start(self):
        self._main_loop()


    def get_fps(self):
        return self._fps


    def _main_loop(self):

        self._init()
        while 1:
            clock.tick(self._fps)

            for event in pygame.event.get():
                # si se apreto el boton de cerrar
                if event.type == pygame.QUIT:
                    sys.exit()
