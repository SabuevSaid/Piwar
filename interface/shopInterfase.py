import interface.background
import interface.button
import pygame
import config
import box
pygame.init()

class ShopInterface:
    def __init__(self):
        self.shop_background = interface.background.Background(pygame.image.load('p1.png'), 0, 0,
                                                          (config.pixels * 20, config.pixels * 10), 'shop_background')
        self.shop_color_box = box.Box(130, 80, (40, 32), 'shop_color_box_button', 'color_box')
        self.shop_box_button = interface.button.Button(pygame.image.load('boxs/default_box.png'), 130, 80, (40, 32),
                                                  'shop_box_button')
        self.shop_box_button.replace_buttons = [self.shop_box_button, self.shop_color_box]
        self.menu_rubins_background = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_rubins_background.png'), 140, 90,
            (config.pixels * 2, config.pixels * 1), 'rubins', next_window=config.main_menu)
        self.menu_golds_background = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_golds_background.png'), 140, 90,
            (config.pixels * 2, config.pixels * 1), 'golds', next_window=config.main_menu)
        self.menu_silvers_background = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_silvers_background.png'), 140, 90,
            (config.pixels * 2, config.pixels * 1), 'silvers', next_window=config.main_menu)
    def pr(self):
        print(self.shop_color_box.prize)
        if type(self.shop_color_box.prize) == tuple:
            if self.shop_color_box.prize[0] == 'silver':
                self.prize = self.menu_silvers_background
            elif self.shop_color_box.prize[0] == 'gold':
                self.prize = self.menu_golds_background
            elif self.shop_color_box.prize[0] == 'rubin':
                self.prize = self.menu_rubins_background
            else:
                self.prize = self.menu_rubins_background
        else:
            self.prize = self.shop_color_box.prize
        return self.prize
    def interface(self):
        config.shop.add_objects(self.shop_background, self.shop_box_button)
        self.shop_color_box.replace_buttons = [self.shop_color_box, self.pr()]