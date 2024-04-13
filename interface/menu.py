import pygame
import config

pygame.init()


class Menu:
    def __init__(self):
        self.window = pygame.Surface((config.wight, config.height))
        self.objects = []

    def add_objects(self, *objects):
        self.objects.extend(objects)
    def del_objects(self, objects):
        for obj in objects:
            self.objects.remove(obj)
    def get_add_object(self, obj):
        surf_copy = config.surf
        surf_copy.objects.append(obj)
        return surf_copy
    def get_del_object(self, obj):
        surf_copy = config.surf
        if obj in surf_copy.objects:
            surf_copy.objects.remove(obj)
        return surf_copy