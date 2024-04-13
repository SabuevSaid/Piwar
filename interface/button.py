import interface.background
import pygame
import config
import interface.menu
pygame.init()


class Button(interface.background.Background):
    def __init__(self, texture, w, h, size, name, next_window=False, add_button=False, del_button=False, replace_buttons=False):
        super().__init__(texture, w, h, size, name)
        self.type = 'button'
        self.next_window = next_window
        self.rect = pygame.Rect(w, h, size[0], size[1])
        self.add_button = add_button
        self.del_button = del_button
        self.replace_buttons = replace_buttons

    def click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.next_window:
                return self.next_window
            elif self.add_button:
                return config.surf.get_add_object(self.add_button)
            elif self.del_button:
                return config.surf.get_del_object(self.del_button)
            elif self.replace_buttons:
                return config.surf.get_add_object(self.replace_buttons[1]).get_del_object(self.replace_buttons[0])
        return False