import pygame
import config
pygame.init()
class DrawText:
    def draw_text(self, silvers, golds, rubins):
        for surf_obj in config.surf.objects:
            if surf_obj.name == 'silvers':
                config.surf.window.blit(silvers, (surf_obj.w + 16, surf_obj.h))
            elif surf_obj.name == 'golds':
                config.surf.window.blit(golds, (surf_obj.w + 16, surf_obj.h))
            elif surf_obj.name == 'rubins':
                config.surf.window.blit(rubins, (surf_obj.w + 16, surf_obj.h))