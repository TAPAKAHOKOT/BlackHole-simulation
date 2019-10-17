import pygame as pg
import random
import math as m

"""Класс планет солнечной системы"""
class Planets():
    """Инициализация класса планет солнечной системы"""
    def __init__(self, settings, screen, i):

        self.screen = screen
        self.settings = settings

        self.v = self.settings.planets_speed[i] / 2

        self.t = 1

        self.x_cor = 0
        self.y_cor = 0

        self.i = i

        self.x = self.settings.planets_x[self.i]
        self.y = self.settings.planets_y[self.i]

        self.zoom_speed = 0.5
        self.x_0 = self.settings.middle[0]
        self.y_0 = self.settings.middle[1]

        self.pos_dot = (self.x, self.y)
        self.dot_color = 100

        self.r = False

        self.arr_dot_pos = []
        for k in range(10):
            self.arr_dot_pos.append(self.pos_dot)

        self.planet_img = pg.transform.scale(self.settings.planets_img[self.i],
        (self.settings.planets_rad[self.i], self.settings.planets_rad[self.i]))

    """Функция отображения картинок планет"""
    def draw_planets(self):
        self.planet = self.screen.blit(self.planet_img, (self.x, self.y))

    # def update_lines(self):
    #     self.line = pg.draw.line(self.screen, (50, 50,50),
    #     [self.x + self.settings.planets_rad[self.i]//2*self.settings.size_koef,
    #     self.y + self.settings.planets_rad[self.i]//2*self.settings.size_koef],
    #     [self.settings.middle[0], self.settings.middle[1]])

    """Функция отображения границ планет"""
    def draw_planets_rect(self):
        border_color = (255 * self.settings.red_border, 0, 0)

        self.shadow = pg.draw.rect(self.screen, border_color, [self.x, self.y,
        self.settings.planets_rad[self.i] * self.settings.size_koef,
        self.settings.planets_rad[self.i] * self.settings.size_koef], 1)
        self.dot_color = 150

        for k in range(10):
            pg.draw.circle(self.screen, (self.dot_color,
                    self.dot_color,self.dot_color), self.arr_dot_pos[k], 0)

            self.dot_color -= 15
    # def draw_ellipse(self):

        # Отображение линий к центру в режиме разработчика
        if self.settings.red_border:
            self.line = pg.draw.line(self.screen, (0, 200,0),
            [self.x + self.settings.planets_rad[self.i]\
                                                //2*self.settings.size_koef,
            self.y + self.settings.planets_rad[self.i]\
                                                //2*self.settings.size_koef],
            [self.settings.middle[0], self.settings.middle[1]])


    """Функция обновления положения планет"""
    def update(self):


        # if self.i == 3:
        #     if self.r and self.x > self.settings.middle[0]\
        #                 and self.y < self.settings.middle[1]:
        #         self.r = False
        #         self.settings.solar_time -= 1
        #     elif self.r and self.x > self.settings.middle[0]\
        #                 and self.y > self.settings.middle[1]:
        #         self.r = False
        #         self.settings.solar_time += 1
        #     elif not self.r and self.x < self.settings.middle[0]:
        #         self.r = True

        self.a = (self.settings.planets_x[self.i]\
            + self.settings.planets_heights[self.i]) * self.settings.size_koef

        self.b = (self.settings.planets_heights[self.i])\
                                                * self.settings.size_koef * 2

        if self.i != 0:
            self.x_cor = self.a*m.sin(self.v*self.t) + self.x_0
            self.y_cor = self.b*m.cos(self.v*self.t) + self.y_0


            try:
                minus = 0.15 / self.v

                for k in range(10):
                    self.dot_x_cor = self.a*m.sin(self.v*(self.t-minus))\
                                + self.x_0 + self.settings.planets_rad[self.i]\
                                //2*self.settings.size_koef

                    self.dot_y_cor = self.b*m.cos(self.v*(self.t-minus))\
                                + self.y_0 + self.settings.planets_rad[self.i]\
                                //2*self.settings.size_koef

                    self.pos_dot = (int(self.dot_x_cor), int(self.dot_y_cor))

                    self.arr_dot_pos[k] = self.pos_dot
                    minus += 0.1 / self.v
            except: None


            if self.settings.freeze_speed == 0:
                self.t += 0.01

            self.x = int(self.x_cor)
            self.y = int(self.y_cor)

            self.settings.planets_x_cors[self.i] = self.x
            self.settings.planets_y_cors[self.i] = self.y
        else:
            self.x = self.x_0 - self.settings.planets_rad[0]\
                                                    *self.settings.size_koef//2
            self.y = self.y_0 - self.settings.planets_rad[0]\
                                                    *self.settings.size_koef//2

            self.settings.planets_x_cors[self.i] = self.x
            self.settings.planets_y_cors[self.i] = self.y