class Color:

    def __init__(self):
        '''
        Crea un color negro
        '''
        self._components = (0, 0, 0)

    @classmethod
    def from_tuple(cls, components):
        '''
        Crear color desde un tuple (r, g, b)

        Los valores están entre 0 y 255.
        '''
        c = cls()
        c.set_components(components)

        return c

    @classmethod
    def from_values(cls, r, g, b):
        '''
        Crear color desde 3 valores RGB.

        Los valores están entre 0 y 255.
        '''
        c = cls()
        c.set_components(r, g, b)

        return c

    def set_components(self, components):
        '''
        Setear color desde un tuple (r, g, b)

        Los valores están entre 0 y 255.
        '''
        self._components = components

    def set_components(self, r, g, b):
        '''
        Setear color desde 3 valores RGB.

        Los valores están entre 0 y 255.
        '''
        self._components = (r, g, b)

    def get_components(self):
        '''
        Obtener componentes como un tuple (r, g, b)

        Los valores están entre 0 y 255.
        '''
        return self._components


# Definiciones de colores
BLACK = Color.from_values(0, 0, 0)
WHITE = Color.from_values(255, 255, 255)
