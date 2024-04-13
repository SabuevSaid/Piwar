import pygame
import interface.background
import interface.button
from config import pixels
import config
pygame.init()
class MenuInterface:
    def interface(self):
        menu_background = interface.background.Background(
            pygame.image.load('interface/textures/menu_textures/menu_background.png'), 0, 0, (pixels * 20, pixels * 10),
            'menu_background')
        menu_play_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_play_button.png'), 240, 128,
            (pixels * 5, pixels * 2), 'menu_play_button', config.game)
        menu_models_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_models_button.png'), 128, 128,
            (pixels * 6, pixels * 2), 'menu_models_button', config.models)
        menu_pers_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_pers_button.png'), 0, 128,
            (pixels * 2, pixels * 2), 'menu_pers_button', config.personages)
        menu_shop_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_shop_button.png'), 32, 128,
            (pixels * 2, pixels * 2), 'menu_shop_button', config.shop)
        menu_skins_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_skins_button.png'), 64, 128,
            (pixels * 2, pixels * 2), 'menu_skins_button', config.skins)
        menu_profil_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_profil_button.png'), 0, 0,
            (pixels * 2, pixels * 2), 'menu_profil_button', config.profil)
        menu_xp_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_xp_button.png'), 0, 48, (pixels * 2, pixels * 3),
            'menu_xp_button', config.xp)
        menu_settings_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_settings_button.png'), 288, 0,
            (pixels * 2, pixels * 1), 'menu_settings_button', config.settings)
        menu_rubins_background = interface.background.Background(
            pygame.image.load('interface/textures/menu_textures/menu_rubins_background.png'), 256, 0,
            (pixels * 2, pixels * 1), 'rubins')
        menu_golds_background = interface.background.Background(
            pygame.image.load('interface/textures/menu_textures/menu_golds_background.png'), 224, 0,
            (pixels * 2, pixels * 1), 'golds')
        menu_silvers_background = interface.background.Background(
            pygame.image.load('interface/textures/menu_textures/menu_silvers_background.png'), 192, 0,
            (pixels * 2, pixels * 1), 'silvers')
        menu_pipass_button = interface.button.Button(
            pygame.image.load('interface/textures/menu_textures/menu_pipass_button.png'), 288, 48,
            (pixels * 2, pixels * 3), 'menu_pipass_button', config.pipass)

        config.main_menu.add_objects(menu_background, menu_play_button, menu_models_button, menu_pers_button, menu_shop_button, menu_skins_button, menu_profil_button, menu_xp_button, menu_settings_button, menu_rubins_background, menu_golds_background, menu_silvers_background, menu_pipass_button)