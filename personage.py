import pygame
import config
pygame.init()
class Personage:
    def __init__(self, texture, name, w, h, size, speed, shot, xp, damage):
        self.texture = texture
        self.name = name
        self.w, self.h = w, h
        self.type = 'personage'
        self.size = size
        self.speed = speed
        self.shot = shot
        self.xp = xp
        self.damage = damage
    def walk(self):
        pass
    def jump(self):
        pass
    def shots(self):
        pass
    def update(self):
        pass
    def draw(self):
        config.surf.window.blit(self.texture, (self.w, self.h))