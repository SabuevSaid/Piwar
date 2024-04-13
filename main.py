import pygame
import config
import interface.menuIntrerface
import interface.shopInterfase
import acount
import interface.draw_text
import box
pygame.init()
interface.menuIntrerface.MenuInterface().interface()
interface.shopInterfase.ShopInterface().interface()
my_acount = acount.Acount('Said', 0, 0, 0, 0, [], [])
while config.play:
    rubins = config.text.render(str(my_acount.rubins), 1, (0, 0, 0))
    silvers = config.text.render(str(my_acount.silvers), 1, (0, 0, 0))
    golds = config.text.render(str(my_acount.golds), 1, (0, 0, 0))
    pygame.display.update()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            config.play = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                for but in config.surf.objects:
                    if but.type in ('button', 'color_box', 'default_box'):
                        but_click = but.click(pygame.mouse.get_pos())
                        if but_click:
                            if but.type == 'color_box':
                                my_acount.add(but.prize)
                            config.surf = but_click
                            if but.name == 'menu_shop_button':
                                config.surf.objects = []
                                interface.shopInterfase.ShopInterface().interface()
                            break
    for surf_obj in config.surf.objects:
        surf_obj.draw()
    interface.draw_text.DrawText().draw_text(silvers, golds, rubins)
    config.display.blit(config.surf.window, (0, 0))
    config.fps.tick(15)
pygame.quit()
