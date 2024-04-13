import pygame
import random
import interface.button
import interface.menu
import personage
import config

pygame.init()


class Box:
    def __init__(self, w, h, size, name, type, next_window=False, add_button=False, del_button=False, replace_buttons=False):
        self.color = self.get_color()
        self.prize = self.get_prize()
        self.w, self.h = w, h
        self.size = size
        self.name = name
        self.type = type
        self.texture = pygame.image.load(f'boxs/{self.color}.png')
        self.rect = pygame.Rect(w, h, size[0], size[1])
        self.next_window = next_window
        self.add_button = add_button
        self.del_button = del_button
        self.replace_buttons = replace_buttons

    def get_color(self):
        colors = {tuple([1]): 'white_box',
                  tuple(range(2, 10)): 'yellow_box',
                  tuple(range(10, 40)): 'red_box',
                   tuple(range(40, 100)): 'green_box',
                   tuple(range(100, 250)): 'purple_box',
                   tuple(range(250, 500)): 'blue_box',
                   tuple(range(500, 1001)): 'grey_box'}
        random_num = random.randint(1, 1001)
        for col in colors:
            if random_num in col:
                return colors[col]
    def get_prize(self):
        prizes = {'white_box': {tuple(range(1, 5)): ('rubin', 200),
                                                                 tuple(range(5, 20)): ('rubin', 150),
                                                                 tuple(range(20, 50)): (self.get_random_personage(125, 150, 175)),
                                                                 tuple(range(50, 101)): (self.get_random_skin(50, 60, 70))},
                       'yellow_box': {tuple(range(1, 5)): ('rubin', 100),
                                                                 tuple(range(5, 20)): (self.get_random_personage(100, 125)),
                                                                 tuple(range(30, 50)): (self.get_random_skin(40, 50)),
                                                                 tuple(range(20, 30)): ('gold', 500),
                                                                 tuple(range(50, 101)): ('power', 100)},
                       'red_box': {tuple(range(1, 5)): ('rubin', 50),
                                                                 tuple(range(5, 20)): (self.get_random_personage(50, 75, 100)),
                                                                 tuple(range(20, 35)): (self.get_random_skin(30, 40)),
                                                                 tuple(range(35, 50)): ('gold', 200),
                                                                 tuple(range(50, 101)): ('power', 75)},
                       'green_box': {tuple(range(1, 5)): ('rubin', 25),
                                                                 tuple(range(5, 20)): (self.get_random_personage(25, 50)),
                                                                 tuple(range(30, 40)): (self.get_random_skin(20, 30)),
                                                                 tuple(range(20, 30)): ('gold', 75),
                                                                 tuple(range(40, 70)): ('silver', 1000),
                                                                 tuple(range(50, 101)): ('power', 75)},
                       'purple_box': {tuple(range(1, 5)): ('rubin', 10),
                                                                 tuple(range(5, 20)): (self.get_random_personage(25)),
                                                                 tuple(range(20, 30)): (self.get_random_skin(10, 20)),
                                                                 tuple(range(30, 40)): ('gold', 50),
                                                                 tuple(range(40, 70)): ('silver', 500),
                                                                 tuple(range(50, 101)): ('power', 50)},
                       'blue_box': {tuple(range(1, 5)): ('rubin', 3),
                                                                 tuple(range(5, 20)): (self.get_random_skin(10)),
                                                                 tuple(range(20, 35)): ('gold', 25),
                                                                 tuple(range(35, 70)): ('silver', 300),
                                                                 tuple(range(50, 101)): ('power', 30)},
                       'grey_box': {tuple(range(1, 5)): ('rubin', 1),
                                                                 tuple(range(5, 20)): ('gold', 5),
                                                                 tuple(range(20, 50)): ('power', 20),
                                                                 tuple(range(50, 101)): ('silver', 200)}}
        random_num = random.randint(1, 100)
        for ran in prizes[self.color]:
            if random_num in ran:
                return prizes[self.color][ran]

    def get_random_skin(self, *rubins):
        skins = {10: (config.sew, ), 20: (config.sew, ), 30: (config.sew, ), 40: (config.sew, ), 50: (config.sew, ), 60: (config.sew, ), 70: (config.sew, )}
        random_rubins = random.choice(rubins)
        return random.choice(skins[random_rubins])
    def get_random_personage(self, *rubins):
        personages = {25: (config.sew, ), 50: (config.sew, ), 75: (config.sew, ), 100: (config.sew, ), 125: (config.sew, ), 150: (config.sew, ), 175: (config.sew, )}
        random_rubins = random.choice(rubins)
        return random.choice(personages[random_rubins])
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
    def draw(self):
        config.surf.window.blit(self.texture, (self.w, self.h))