class Color:
    '''
    Representa a un color.

    Examples
    --------
    Hay varias formas de crear un color, acá hay varias formas::

        # crear un color vacío, que por defecto es negro
        c = toledo.graphics.Color()

        # crear un color a partir de un tuple de componentes
        tuple = (r, g, b)
        c = toledo.graphics.Color.from_tuple(tuple)

        # crear un color desde sus componentes
        c = toledo.graphics.Color.from_values(r, g, b)

        # crear un color ya definido
        c = toledo.graphics.Color.from_name("red")
        c = toledo.graphics.Color.from_name("black")

    '''

    # definiciones de colores
    _NAMES = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }

    def __init__(self):
        self._components = (0, 0, 0)


    @classmethod
    def from_tuple(cls, components):
        '''
        Crear color desde un tuple (r, g, b).

        Los valores deben ser enteros entre 0 y 255.

        Parameters
        ----------
        components : Tuple[int]
            Componentes RGB a usar, es un tuple (r, g, b) con enteros entre 0 y
            255.

        Returns
        -------
        toledo.graphics.Color
            Instancia de un color.
        '''
        c = cls()
        c.set_tuple(components)

        return c


    @classmethod
    def from_values(cls, r, g, b):
        '''
        Crear color desde 3 enteros que corresponden a R, G y B.

        Los valores deben ser enteros entre 0 y 255.

        Parameters
        ----------
        r : int
            Componente roja. Entero de 0 a 255.
        g : int
            Componente verde. Entero de 0 a 255.
        b : int
            Componente azul. Entero de 0 a 255.

        Returns
        -------
        toledo.graphics.Color
            Instancia de un color.
        '''
        c = cls()
        c.set_values(r, g, b)

        return c


    @classmethod
    def from_name(cls, name):
        '''
        Crear color desde un nombre, usando una constante ya definida.

        Se puede usar cualquiera de los nombres definidos:

        - ``"black"``
        - ``"white"``
        - ``"red"``
        - ``"green"``
        - ``"blue"``

        Parameters
        ----------
        components : str
            Nombre que representa el color a crear.

        Returns
        -------
        toledo.graphics.Color
            Instancia de un color.
        '''
        return cls.from_tuple(cls._NAMES[name])


    def set_tuple(self, components):
        '''
        Setear color desde un tuple (r, g, b).

        Los valores están entre 0 y 255.

        Parameters
        ----------
        components : Tuple[int]
            Componentes RGB a usar, es un tuple (r, g, b) con enteros entre 0 y
            255.
        '''
        self._components = components


    def set_values(self, r, g, b):
        '''
        Setear color desde 3 valores RGB.

        Los valores están entre 0 y 255.

        Parameters
        ----------
        r : int
            Componente roja. Entero de 0 a 255.
        g : int
            Componente verde. Entero de 0 a 255.
        b : int
            Componente azul. Entero de 0 a 255.
        '''
        self._components = (r, g, b)


    def get_tuple(self):
        '''
        Obtener componentes como un tuple (r, g, b)

        Los valores están entre 0 y 255.

        Returns
        -------
        Tuple[int]
            Tuple que representa a las componentes R, G y B.
        '''
        return self._components
