import toledo.graphics

class Assets:

    sprites = {}

    def load_sprite(self, name, image_path):
        s = toledo.graphics.Sprite(image_path)
        self.sprites[name] = s

    def get_sprite(self, name):
        return self.sprites[name]
