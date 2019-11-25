import pygame as pg
import random
import math as m


class Dot_hole():
    def __init__(self, settings, screen):
        self.create_plus = 500
        self.screen = screen
        self.rad = 0
        self.settings = settings

        self.track_size = 20

        self.all_track_colors = []

        self.last_pos = []

        self.tors_speed = random.randint(1000, 5000) / settings.tors_speed_koef

        self.dot_pos_num = random.randint(1, 4)
        self.dot_in_middle_chanse = random.randint(1, 7)
        self.step = random.randint(100, 800)

        # self.dot_speed_whole = random.randint(settings.whole_speed_max, settings.whole_speed_min)

        self.gravity_coef_x = settings.gravity_point_x / settings.screen_width
        self.gravity_coef_y = settings.gravity_point_y / settings.screen_height

        self.del_x = settings.gravity_point_x
        self.del_y = settings.gravity_point_y

        # self.dark_whole = settings.dark_whole_index

        if self.dot_in_middle_chanse == 3:
            self.x = random.randint(settings.screen_width // 4,
                                    settings.screen_width // 4 * 3)
            self.y = random.randint(settings.screen_height // 4,
                                    settings.screen_height // 4 * 3)

        elif self.dot_pos_num == 1:
            self.x = random.randint(-self.create_plus,
                                    settings.screen_width + self.create_plus)
            self.y = random.randint(-self.create_plus,
                                    settings.screen_height // 4)

        elif self.dot_pos_num == 2:
            self.x = random.randint(settings.screen_width // 4 * 3,
                                    settings.screen_width + self.create_plus)
            self.y = random.randint(-self.create_plus,
                                    settings.screen_height + self.create_plus)

        elif self.dot_pos_num == 3:
            self.x = random.randint(-self.create_plus,
                                    settings.screen_width + self.create_plus)
            self.y = random.randint(settings.screen_height // 4 * 3,
                                    settings.screen_height + self.create_plus)

        elif self.dot_pos_num == 4:
            self.x = random.randint(-self.create_plus,
                                    settings.screen_width // 4)
            self.y = random.randint(-self.create_plus,
                                    settings.screen_height + self.create_plus)

        self.proj_dot_x = abs(self.x - settings.gravity_point_x)
        self.proj_dot_y = abs(self.y - settings.gravity_point_y)

        self.color = settings.dots_colors[random.randint(0,
                                                         len(settings.dots_colors) - 1)]

        self.radius_dot_dist = m.sqrt(self.proj_dot_x**2 + self.proj_dot_y**2)

        self.whole_rad = settings.screen_height // settings.screen_part_whole_rad

        self.x_int = int(self.x)
        self.y_int = int(self.y)
        self.pos = self.x_int, self.y_int

        self.speed_x = abs((self.x -
                            settings.screen_width * self.gravity_coef_x) / self.step)
        self.speed_y = abs((self.y -
                            settings.screen_height * self.gravity_coef_y) / self.step)
        self.arr = []

        for k in range(self.track_size):
            self.arr.append(0)

        for k in range(self.track_size):
            self.arr[k] = self.pos

    def draw_dot(self, red_border):
        if not red_border:
            self.rect = pg.draw.circle(
                self.screen, self.color, self.pos, self.rad)
        else:

            for k in range(1, self.track_size + 1, 4):
                self.rect = pg.draw.circle(self.screen,
                                           (255, 0, 255), self.arr[-k], 0)

            self.rect = pg.draw.circle(self.screen, (255, 0, 0), self.pos, 1)

    def update(self):
        x = 0

        # if random.randint(1, 5000) == 3:
        #     self.rad = random.randint(0, 1)
    def pos_change(self):
        for k in range(self.track_size):
            if k == self.track_size - 1:
                self.arr[k] = self.pos
            else:
                self.arr[k] = self.arr[k + 1]
        self.pos = (int(self.x), int(self.y))

    def zoom_off(self, size_koef):
        if size_koef > 0.015:
            if self.x < self.del_x - 1:
                self.x += self.speed_x
            elif self.x > self.del_x + 1:
                self.x -= self.speed_x

            if self.y > self.del_y + 1:
                self.y -= self.speed_y
            elif self.y < self.del_y - 1:
                self.y += self.speed_y

            # p = round((self.settings.screen_height // 1.5 - self.settings.size_slider_y) /
            #           abs(self.settings.screen_height // 2.65 - self.settings.screen_height // 1.5), 3)
            # #
            # distance_x = (self.x - self.settings.screen_width // 2) / \
            #     (self.settings.screen_height // 1.5 - self.settings.size_slider_y) * \
            #     abs(self.settings.screen_height // 2.65 -
            #         self.settings.screen_height // 1.5)
            # #
            # self.x = self.settings.screen_width // 2 + distance_x * p
            #
            # distance_y = (self.y - self.settings.screen_height *
            #               self.gravity_coef_y) * (p ** -1) * (1 - self.step / 100000)
            # self.y = self.settings.screen_height // 2 + distance_y * p

            self.pos_change()

    def zoom_on(self, size_koef, max_size):
        if size_koef < max_size:
            if self.x < self.del_x - 1:
                self.x -= self.speed_x
            elif self.x > self.del_x + 1:
                self.x += self.speed_x

            if self.y > self.del_y + 1:
                self.y += self.speed_y
            elif self.y < self.del_y - 1:
                self.y -= self.speed_y

            self.pos_change()
