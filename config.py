import pygame
from interface.menu import Menu
from personage import Personage


fps = pygame.time.Clock()
pixels = 16
wight, height = (pixels * 20, pixels * 10)  # (960, 640)
display = pygame.display.set_mode((wight, height))
text = pygame.font.Font('PIXY.ttf', 14)
play = True

sew = Personage(pygame.image.load('sew.png'), 'sew', 130, 80, (40, 32), 15, None, 5000, 1000)

main_menu = Menu()
game = Menu()
models = Menu()
personages = Menu()
shop = Menu()
skins = Menu()
profil = Menu()
xp = Menu()
settings = Menu()
pipass = Menu()

surf = main_menu
