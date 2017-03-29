import graphics

class Assets:

    sprites = {}

    def load_sprite(self, name, image_path):
        s = graphics.Sprite(image_path)
        sprites[name] = s

    def get_sprite(self, name):
        return sprites[name]
