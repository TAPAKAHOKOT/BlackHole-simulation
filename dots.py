import pygame as pg
import random
import math as m


class Dot():
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.m_y = 1
        self.m_x = 1

        self.rad = random.randint(settings.min_dot_radius,
                                  settings.max_dot_radius)

        self.tors_speed = random.randint(1000, 5000) / settings.tors_speed_koef

        self.dot_pos_num = random.randint(1, 4)
        self.dot_in_middle_chanse = random.randint(1, 10)
        self.step = random.randint(settings.max_speed, settings.min_speed)
        self.staying = random.randint(1, settings.staying_dots_part)
        self.staying_arg = 0

        self.move_koef = False

        self.dot_speed_whole = random.randint(settings.whole_speed_max,
                                              settings.whole_speed_min)

        self.gravity_coef_x = settings.gravity_point_x / settings.screen_width
        self.gravity_coef_y = settings.gravity_point_y / settings.screen_height

        self.del_x = settings.gravity_point_x
        self.del_y = settings.gravity_point_y

        self.dark_whole = settings.dark_whole_index

        if self.dot_in_middle_chanse >= 7:
            self.x = random.randint(settings.screen_width // 4,
                                    settings.screen_width // 4 * 3)
            self.y = random.randint(settings.screen_height // 4,
                                    settings.screen_height // 4 * 3)

        elif self.dot_pos_num == 1:
            self.x = random.randint(0, settings.screen_width)
            self.y = random.randint(0, settings.screen_height // 4)

        elif self.dot_pos_num == 2:
            self.x = random.randint(settings.screen_width // 4 * 3,
                                    settings.screen_width)
            self.y = random.randint(0, settings.screen_height)

        elif self.dot_pos_num == 3:
            self.x = random.randint(0, settings.screen_width)
            self.y = random.randint(settings.screen_height // 4 * 3,
                                    settings.screen_height)

        elif self.dot_pos_num == 4:
            self.x = random.randint(0, settings.screen_width // 4)
            self.y = random.randint(0, settings.screen_height)

        self.proj_dot_x = abs(self.x - settings.gravity_point_x)
        self.proj_dot_y = abs(self.y - settings.gravity_point_y)

        self.color = settings.dots_colors[random.randint(0,
                                                         len(settings.dots_colors) - 1)]

        self.radius_dot_dist = m.sqrt(self.proj_dot_x**2 + self.proj_dot_y**2)

        self.whole_rad = settings.screen_height // settings.screen_part_whole_rad

        self.x_int = int(self.x)
        self.y_int = int(self.y)

        self.tors_intensive = 1

        self.pos = self.x_int, self.y_int

        if self.dark_whole == 1:
            self.speed_x = 0
            self.speed_y = 0

            if self.radius_dot_dist <= settings.screen_height\
                    // settings.staying_dots_part:
                self.speed_x = abs((self.x -
                                    settings.screen_width * self.gravity_coef_x) / self.step)
                self.speed_y = abs((self.y -
                                    settings.screen_height * self.gravity_coef_y) / self.step)

        elif self.dark_whole == -1:
            self.speed_x = abs((self.x -
                                settings.screen_width * self.gravity_coef_x) / self.step)
            self.speed_y = abs((self.y -
                                settings.screen_height * self.gravity_coef_y) / self.step)

            if self.staying == 1 and sum(settings.staying_dots)\
                    < settings.dot_num // settings.staying_dots_part:

                self.staying_arg = 1
                self.speed_x = 0
                self.speed_y = 0
                self.rad = random.randint(2, 4)

        settings.staying_dots.append(self.staying_arg)

        self.tors_size = 20
        self.tors_max = 100
        self.arr = []

        for k in range(self.tors_size):
            self.arr.append(0)

        for k in range(self.tors_size):
            self.arr[k] = self.pos

    def draw_dot(self):

        # if self.last_pos != self.pos:
        if self.move_koef:
            for k in range(self.tors_size):
                # if k >= self.tors_max:
                #     break
                if k % self.tors_intensive == 0:
                    if k != 0:
                        self.all_dots = pg.draw.circle(self.screen,
                                                       self.color, self.arr[k], 0)
                    else:
                        self.last_dot = pg.draw.circle(self.screen,
                                                       (0, 0, 0), self.arr[k], 1)
        self.rect = pg.draw.circle(self.screen, self.color, self.pos, self.rad)

    def moving(self, settings, speed, mooving_arround_speed=2):
        self.dot_speed_whole -= speed

        if self.y >= settings.gravity_point_y:
            if self.radius_dot_dist == 0:
                self.radius_dot_dist = 0.00001
            self.tilt = m.acos(self.proj_2_dot_x / (self.radius_dot_dist))\
                - m.radians(self.tors_speed * mooving_arround_speed)

            self.y_2 = self.radius_dot_dist * m.sin(self.tilt)

        elif self.y < settings.gravity_point_y:
            self.tilt = m.acos(self.proj_2_dot_x / self.radius_dot_dist)\
                + m.radians(self.tors_speed * mooving_arround_speed)

            self.y_2 = self.radius_dot_dist * m.sin(self.tilt) * (-1)

        self.x_2 = self.radius_dot_dist * m.cos(self.tilt)

        self.x = self.x_2 + settings.gravity_point_x
        self.y = self.y_2 + settings.gravity_point_y

        self.dot_speed_whole = round(self.dot_speed_whole, 10)

        if self.dot_speed_whole <= 1:
            self.dot_speed_whole = 1

        self.speed_x = self.proj_dot_rad_x / self.dot_speed_whole
        self.speed_y = self.proj_dot_rad_y / self.dot_speed_whole

        self.move_koef = True

    def change_speed(self, settings):

        if self.whole_rad // 8 <= self.radius_dot_dist < self.whole_rad // 6:
            self.m_x = self.m_y = 0.003
        else:
            self.m_x = self.m_y = 1

        if self.radius_dot_dist < self.whole_rad // 0.5\
                and self.radius_dot_dist >= self.whole_rad // 0.6:
            if not settings.black_hole_following:
                self.moving(settings, 1, 0.002)

            else:
                self.moving(settings, 1, 0.04)

            self.speed_x = 0
            self.speed_y = 0
            # self.tors_max = 0
            # self.tors_intensive = 3

        elif self.radius_dot_dist < self.whole_rad // 0.5\
                and self.radius_dot_dist >= self.whole_rad // 0.6:
            if not settings.black_hole_following:
                self.moving(settings, 1, 0.025)

            else:
                self.moving(settings, 1, 0.05)

            self.speed_x = 0
            self.speed_y = 0
            # self.tors_max = 45
            # self.tors_intensive = 1

        elif self.radius_dot_dist < self.whole_rad // 0.6\
                and self.radius_dot_dist >= self.whole_rad // 0.7:
            if not settings.black_hole_following:
                self.moving(settings, 1, 0.05)

            else:
                self.moving(settings, 1, 0.1)

            self.speed_x = 0
            self.speed_y = 0
            # self.tors_intensive = 2

        elif self.radius_dot_dist < self.whole_rad // 0.7\
                and self.radius_dot_dist >= self.whole_rad // 0.8:
            if not settings.black_hole_following:
                self.moving(settings, 1, 0.1)

            else:
                self.moving(settings, 1, 0.2)

            self.speed_x = 0
            self.speed_y = 0
            # self.tors_intensive = 2

        elif self.whole_rad // 0.9 <= self.radius_dot_dist < self.whole_rad // 0.8:
            if not settings.black_hole_following:
                self.moving(settings, 1, 0.25)

            else:
                self.moving(settings, 1, 0.5)

            self.speed_x = 0
            self.speed_y = 0
            # self.tors_intensive = 3

        elif self.whole_rad <= self.radius_dot_dist < self.whole_rad // 0.9:
            if not settings.black_hole_following:
                self.moving(settings, 1, 0.5)
            else:
                self.moving(settings, 1, 1)

            self.speed_x = 0
            self.speed_y = 0
            # self.tors_size = 15
            # self.tors_intensive = 1

        elif self.whole_rad // 1.5 <= self.radius_dot_dist < self.whole_rad:
            if not settings.black_hole_following:
                self.moving(settings, 1, 1)
            else:
                self.moving(settings, 1, 2)

            # self.speed_x = 0
            # self.speed_y = 0

        elif self.whole_rad // 2 <= self.radius_dot_dist < self.whole_rad // 1.5:
            self.moving(settings, 1)

        elif self.whole_rad // 3.5 <= self.radius_dot_dist < self.whole_rad // 2:
            self.moving(settings, 1)

        elif self.whole_rad // 6 <= self.radius_dot_dist < self.whole_rad // 3.5:
            self.moving(settings, 3, 5)

        elif self.whole_rad // 8 <= self.radius_dot_dist < self.whole_rad // 6:
            self.moving(settings, 3, 10)

        elif self.radius_dot_dist < self.whole_rad // 8:
            self.moving(settings, 10)

        else:
            self.move_koef = False

    """Функция для изменения координат точек"""

    def change_cors(self, settings):
        if self.dark_whole == 1:
            self.proj_dot_x = abs(self.x - settings.gravity_point_x)
            self.proj_dot_y = abs(self.y - settings.gravity_point_y)

            self.proj_2_dot_x = self.x - settings.gravity_point_x
            self.proj_2_dot_y = settings.gravity_point_y - self.y

            self.proj_dot_rad_x = abs(self.x -
                                      settings.screen_width * self.gravity_coef_x)
            self.proj_dot_rad_y = abs(self.y -
                                      settings.screen_height * self.gravity_coef_y)
            #
            self.radius_dot_dist = m.sqrt(self.proj_dot_x * self.proj_dot_x +
                                          self.proj_dot_y * self.proj_dot_y)
            self.change_speed(settings)

    """"""

    def check(self, settings):
        for k in range(self.tors_size):
            if k == self.tors_size - 1:
                self.arr[k] = self.pos
            else:
                self.arr[k] = self.arr[k + 1]

    """"""

    def update(self, settings):
        if self.y >= settings.screen_height * self.gravity_coef_y:
            self.y_koef = 1
        else:
            self.y_koef = -1
        self.change_cors(settings)

        sp_x = self.speed_x * self.m_x
        sp_y = self.speed_y * self.m_y

        if self.x < self.del_x - 1:
            self.x += sp_x
        elif self.x > self.del_x + 1:
            self.x -= sp_x

        if self.y > self.del_y + 1:
            self.y -= sp_y
        elif self.y < self.del_y - 1:
            self.y += sp_y

        self.check(settings)

        self.pos = (int(self.x), int(self.y))
