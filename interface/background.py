import config

class Background:
    def __init__(self, texture, w, h, size, name):
        self.type = 'background'
        self.texture = texture
        self.name = name
        self.w, self.h = w, h
        self.size = size
    def draw(self):
        config.surf.window.blit(self.texture, (self.w, self.h))