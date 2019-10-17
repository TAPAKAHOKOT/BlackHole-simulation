import pygame as pg
from random import randint
import math as m

class Astro():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.img = self.settings.astro_img

        self.rad = randint(14, 40)

        self.img = pg.transform.scale(self.img, (self.rad,self.rad))

        self.x = self.settings.planets_x[0]

        self.xxx = randint(self.settings.planets_x[5],
                                            self.settings.planets_x[6])
        self.yyy = randint(self.settings.planets_heights[5],
                                            self.settings.planets_heights[6])


        self.y = randint(self.settings.planets_y[6], self.settings.planets_y[5])

        self.color = (255,0,0)

        self.pos = (self.x, self.y)

        self.v = randint(int(self.settings.planets_speed[4] * 5),
                                        int(self.settings.planets_speed[4]*7))/4

        self.v /= 10

        self.t = randint(1, 150)


        self.x_0 = self.settings.middle[0]
        self.y_0 = self.settings.middle[1]


    def draw(self):
        # self.x *= self.settings.size_koef
        # self.y *= self.settings.size_koef
        #
        # self.pos = (int(self.x), int(self.y))
        self.astro = self.screen.blit(self.img, self.pos)

    def draw_shadow(self):
        self.shadow = pg.draw.circle(self.screen, self.color, self.pos, 0)

    def update(self):

        self.a = self.xxx * self.settings.size_koef
        self.b = self.yyy * self.settings.size_koef


        self.x_cor = self.a*m.sin(self.v*self.t) + self.x_0
        self.y_cor = self.b*m.cos(self.v*self.t) + self.y_0


        try:
            minus = 0.15 / self.v

            for k in range(10):
                self.dot_x_cor = self.a*m.sin(self.v*(self.t-minus)) + self.x_0
                self.dot_y_cor = self.b*m.cos(self.v*(self.t-minus)) + self.y_0

                self.pos_dot = (int(self.dot_x_cor), int(self.dot_y_cor))

                self.arr_dot_pos[k] = self.pos_dot
                minus += 0.1 / self.v
        except: None


        self.t += 0.01

        # self.rad *= self.settings.size_koef

        self.x = int(self.x_cor)
        self.y = int(self.y_cor)

        self.pos = (self.x, self.y)

        # self.settings.planets_x_cors[self.i] = self.x
        # self.settings.planets_y_cors[self.i] = self.y
