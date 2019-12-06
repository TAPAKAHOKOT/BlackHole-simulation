import pygame as pg
import random
import math as m

"""Класс планет солнечной системы"""


class Planets():
    """Инициализация класса планет солнечной системы"""

    def __init__(self, settings, screen, i):
        self.omg = 1
        self.kek = 1

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
        if self.i in self.settings.salt_info.keys():

            print(self.settings.salt_info.keys())
            self.salt_info = self.settings.salt_info[self.i]

            self.salt_speed = self.salt_info["speed"]
            self.salt_a = self.salt_info["a"]
            self.salt_b = self.salt_info["b"]
            self.salt_rad = self.salt_info["rad"]
            self.salt_pos = self.salt_info["pos"]
            self.salt_img = self.salt_info["img"]

        self.shadow = pg.Rect(self.x, self.y,
                              self.settings.planets_rad[self.i] *
                              self.settings.size_koef * 3,
                              self.settings.planets_rad[self.i] * self.settings.size_koef * 3)

    """Функция отображения картинок планет"""

    def draw_planets(self):
        # if self.settings.size_koef < 0.05:
        #     pg.draw.circle(self.screen, (200, 200, 200),
        #                    (int(self.x + self.settings.planets_rad[self.i] // 2 * self.settings.size_koef),
        #                     int(self.y + self.settings.planets_rad[self.i] // 2 * self.settings.size_koef)),
        #                    int((self.settings.planets_rad[self.i] // 2) * self.settings.size_koef))

        if self.i in self.settings.salt_info.keys():
            for k in range(len(self.salt_speed)):
                self.s_a = self.salt_a[k] * self.settings.size_koef
                self.s_b = self.salt_b[k] * self.settings.size_koef
                self.r = self.settings.planets_rad[self.i] * \
                    self.settings.size_koef

                self.l = self.t + self.salt_pos[k]
                #
                # self.a_t, self.b_t = 100 * self.settings.size_koef, 50 * self.settings.size_koef
                self.x_t = int(self.s_a * m.sin(self.v *
                                                self.l * self.salt_speed[k]) + self.x + self.r // 2)
                self.y_t = int(self.s_b * m.cos(self.v *
                                                self.l * self.salt_speed[k]) + self.y + self.r // 2)

                self.rad_t = self.salt_rad[k] * self.settings.size_koef

                if self.rad_t < 1:
                    self.rad_t = 0.5

                self.im = pg.transform.scale(
                    self.salt_img[k], (int(self.rad_t * 4), int(self.rad_t * 4)))

                if self.salt_rad[k] != 0:
                    self.screen.blit(self.im, (self.x_t, self.y_t))
                else:
                    if self.settings.size_koef > 0.12:
                        pg.draw.circle(self.screen, (255, 250, 255),
                                       (self.x_t, self.y_t), 0)
        self.planet = self.screen.blit(
            self.planet_img, (self.x, self.y))

    # def update_lines(self):
    #     self.line = pg.draw.line(self.screen, (50, 50, 50),
    #                              [self.x + self.settings.planets_rad[self.i] // 2 * self.settings.size_koef,
    #                               self.y + self.settings.planets_rad[self.i] // 2 * self.settings.size_koef],
    #                              [self.settings.middle[0], self.settings.middle[1]])

    """Функция отображения границ планет"""

    def draw_planets_rect(self):
        border_color = (255 * self.settings.red_border, 0, 0)

        # self.shadow = pg.draw.rect(self.screen, border_color, [self.x, self.y,
        #                                                        self.settings.planets_rad[self.i] *
        #                                                        self.settings.size_koef,
        #                                                        self.settings.planets_rad[self.i] * self.settings.size_koef], 1)
        self.shadow = pg.Rect(self.x, self.y,
                              self.settings.planets_rad[self.i] *
                              self.settings.size_koef * 3,
                              self.settings.planets_rad[self.i] * self.settings.size_koef * 3)
        self.dot_color = 150

        for k in range(10):
            pg.draw.circle(self.screen, (self.dot_color,
                                         self.dot_color, self.dot_color), self.arr_dot_pos[k], 0)

            self.dot_color -= 15
    # def draw_ellipse(self):

        # Отображение линий к центру в режиме разработчика
        if self.settings.red_border:
            self.line = pg.draw.line(self.screen, (0, 200, 0),
                                     [self.x + self.settings.planets_rad[self.i]
                                      // 2 * self.settings.size_koef,
                                      self.y +
                                      self.settings.planets_rad[self.i]
                                      // 2 * self.settings.size_koef],
                                     [self.settings.middle[0], self.settings.middle[1]])

    """Функция обновления положения планет"""

    def update(self):

        if self.i == 3:
            if self.r and self.x > self.settings.middle[0]\
                    and self.y < self.settings.middle[1]:
                self.r = False

            elif self.r and self.x > self.settings.middle[0]\
                    and self.y > self.settings.middle[1]:
                self.r = False
                # self.settings.solar_time += 1
                self.settings.solar_time = 1982 + round(self.t / 34)
                # print(round(self.t / 34))
                # print(1982 - self.settings.solar_time)

            elif not self.r and self.x < self.settings.middle[0]:
                if self.y > self.settings.middle[1]:
                    # self.settings.solar_time -= 1
                    self.settings.solar_time = 1982 + round(self.t / 34)

                self.r = True

        self.a = (self.settings.planets_x[self.i]
                  + self.settings.planets_heights[self.i]) * self.settings.size_koef

        self.b = (self.settings.planets_heights[self.i])\
            * self.settings.size_koef * 2

        if self.i != 0:
            self.x_cor = self.a * m.sin(self.v * self.t) + self.x_0
            self.y_cor = self.b * m.cos(self.v * self.t) + self.y_0

            try:
                minus = 0.15 / self.v

                for k in range(10):
                    self.dot_x_cor = self.a * m.sin(self.v * (self.t - minus))\
                        + self.x_0 + self.settings.planets_rad[self.i]\
                        // 2 * self.settings.size_koef

                    self.dot_y_cor = self.b * m.cos(self.v * (self.t - minus))\
                        + self.y_0 + self.settings.planets_rad[self.i]\
                        // 2 * self.settings.size_koef

                    self.pos_dot = (int(self.dot_x_cor), int(self.dot_y_cor))

                    self.arr_dot_pos[k] = self.pos_dot
                    minus += 0.1 / self.v
            except:
                None

            if self.settings.freeze_speed == 0:
                self.t += 0.01

            self.x = int(self.x_cor)
            self.y = int(self.y_cor)

            self.settings.planets_x_cors[self.i] = self.x
            self.settings.planets_y_cors[self.i] = self.y
        else:
            self.x = self.x_0 - self.settings.planets_rad[0]\
                * self.settings.size_koef // 2
            self.y = self.y_0 - self.settings.planets_rad[0]\
                * self.settings.size_koef // 2

            self.settings.planets_x_cors[self.i] = self.x
            self.settings.planets_y_cors[self.i] = self.y
