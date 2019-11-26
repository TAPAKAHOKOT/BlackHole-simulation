import random
import pygame as pg


class Settings():
    def __init__(self, screen_width, screen_height):
        """BLACK HOLE SETTINGS"""
        self.tors_allowed = True
        self.hint = False

        self.hint_alpha = 0
        self.text_alpha = 0

        self.dot_color = 255, 255, 255

        self.object_dot = []
        self.staying_dots = []

        self.moving_direct = 1
        self.black_hole_following = False

        self.speed_hole_koef = 1

        self.dark_hole_speed = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1],
                                [-1, -1], [0, 0]]
        self.whole_speed_max = 5
        self.whole_speed_min = 40

        self.dot_num = 1000

        self.tors_speed_koef = 1000

        self.min_dot_radius = 1
        self.max_dot_radius = 3

        self.max_speed = 25
        self.min_speed = 800

        self.hint_hole = False

        self.hint_hole_alpha = 0

        self.dark_whole_index = 1

        self.staying_dots_part = 3

        self.screen_part_whole_rad = 3

        """MAIN SETTINGS"""
        self.font = 'Times New Roman'
        self.fps = 1
        # self.font = 'Agency FB'

        """DK"""
        self.lang_hover_on = 2
        self.lang_heights = [0, 0]

        self.slider_pos_now = 0
        self.slider_pos_old = 0

        """
        self.fon = pg.image.load('img/fon.jpg')
        self.fon = pg.transform.scale(self.fon, (screen_width, screen_height))

        self.fon_surf = pg.Surface((screen_width, screen_height))
        self.fon_surf.fill((0, 0, 0))
        self.fon_surf.set_alpha(150)
        self.for_rect = pg.Rect((0, 0, screen_width, screen_height))
        """
        # screen.blit(self.fon_surf, self.fon)

        """SOLAR SYSTEM SETTINGS"""
        self.size_koef = 1
        self.size_num = 1

        self.size_bool = False
        self.tt = 5

        self.planets_x_cors = []
        self.planets_y_cors = []

        for k in range(9):
            self.planets_x_cors.append(0)
            self.planets_y_cors.append(0)

        self.dots_colors = [(255, 180, 180), (255, 255, 255), (180, 180, 255),
                            (255, 255, 180), (255, 180, 255)]
        self.fps = 0

        self.time_1 = 0

        self.time_2 = 0

        self.hint_solar = False

        self.hint_solar_alpha = 0

        """txt файлы"""
        self.lang_txt_change = 0
        self.files_types = ['_eng', '_ru']

        self.all_text = [[], []]
        for k in range(2):
            self.all_txt = open(
                'text/all_text' + self.files_types[k] + '.txt', 'r')
            self.all_txt = self.all_txt.read().split('|')
            self.all_text[k] = self.all_txt
        print(self.all_text)

        # Текст с описанием всех планет солнечной системы, включая солнце
        self.text_planets = []
        for k in range(2):
            self.file = open('text/text_planets' +
                             self.files_types[k] + '.txt', 'r')
            self.text_planets.append(self.file.read().split('|'))
            self.file.close()
        self.text_arr = self.text_planets[0]

        # Текс помощи для управления черной дырой
        self.hole_hint_txt = []
        for k in range(2):
            self.file = open('text/hint_hole' +
                             self.files_types[k] + '.txt', 'r')
            self.hole_hint_txt.append(self.file.read())
            self.file.close()
        self.text_hole = self.hole_hint_txt[self.lang_txt_change]

        # Текс помощи для управления солнечной системой
        self.solar_hint_txt = []
        for k in range(2):
            self.file = open('text/hint_solar' +
                             self.files_types[k] + '.txt', 'r')
            self.solar_hint_txt.append(self.file.read())
            self.file.close()
        self.text_solar = self.solar_hint_txt[self.lang_txt_change]

        self.zoom_off = False

        self.myfont = 0
        self.title = 0

        self.frame = False

        self.screen_rect = 0

        self.click = 1

        self.time_hold = 0

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.middle = [self.screen_width // 2, self.screen_height // 2]

        self.new_x_for_planets = self.middle[0]
        self.new_y_for_planets = self.middle[1]

        self.follow_koef = 0

        self.max_size_koef_arr = [4, 90, 40, 40, 70, 10, 10, 20, 20]

        for k in range(len(self.max_size_koef_arr)):
            self.max_size_koef_arr[k] /= 2

        self.x_speed = 0.3
        self.y_speed = 0.3

        self.change_speed_counter = 0

        self.hole_x = self.screen_width // 2
        self.hole_y = self.screen_height // 2

        self.settings_frame = False
        self.set_alpha = 0
        self.settings_chosen = 2
        self.hover_on = -1
        self.heights = [0, 0, 0]
        self.x_points = [self.screen_width - 200,
                         self.screen_width - 170,
                         self.screen_width - 140,
                         self.screen_width - 110,
                         self.screen_width - 80,
                         self.screen_width - 40]

        self.gravity_point_x = self.hole_x
        self.gravity_point_y = self.hole_y

        # # QUESTION:
        self.question_img = pg.image.load('img/question.png')
        self.question_img = pg.transform.scale(self.question_img, (20, 20))

        self.settings_img = pg.image.load('img/settings_ico.png')
        self.settings_img = pg.transform.scale(self.settings_img, (20, 20))

        self.mouse_cors = [0, 0]

        self.solar_time = 1982

        # Sun System settings
        self.dot_hole_num = 400
        self.obj_dot_hole = []
        self.sun_system_koef = 1
        self.i = 1

        self.slider_x1 = int(self.screen_width // 2 - 5)
        self.slider_y1 = int(self.screen_height - 50)
        self.slider_hold = False

        self.size_slider_y = self.screen_height // 2
        self.size_slider_x = self.screen_width - 40

        self.size_slider_y_hold = False

        self.red_border = False

        self.speed_of_mooving_koef = 0.3

        self.update_size_moving = False
        self.max_size_koef = self.max_size_koef_arr[0]
        # plsnets of the sun system settings
        # Sun Mercury Venus Earth Mars Jupyter Saturn Uranus Neptun
        earth_speed = 1
        self.planets_speed = [
            0,  # The Sun
            365 / 88 * earth_speed,  # Mercury
            365 / 225 * earth_speed,  # Venus
            earth_speed,  # Earth
            365 / 687 * earth_speed,  # Mars
            earth_speed / 12,  # Jupyter
            earth_speed / 29,  # Saturn
            earth_speed / 84,  # Uranus
            earth_speed / 165  # Neptune
        ]
        for k in range(len(self.planets_speed)):
            self.planets_speed[k] *= self.speed_of_mooving_koef
        print(self.planets_speed)

        self.freeze_speed = 0
        self.zoomed = False

        self.planets_heights = [0, 66, 185, 251, 326, 1226, 2218, 4554, 7656]
        self.planets_widths = [0, 100, 188, 260, 395, 1353, 2484, 4990, 7831]

        for k in range(len(self.planets_heights)):
            self.planets_heights[k] *= 2
        self.planets_names = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars',
                              'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        self.planets_img = []
        self.object_planets = []
        self.planets_rad = []
        self.planets_x = []
        self.planets_y = []

        """Sun settings"""
        self.sun_rad = int(200 * self.size_koef)

        self.sun_rad_koef = self.sun_rad / 100

        self.sun_x_cor = self.screen_width // 2 - self.sun_rad // 2
        self.sun_y_cor = self.screen_height // 2 - self.sun_rad // 2

        self.planets_x.append(self.sun_x_cor)
        self.planets_y.append(self.sun_y_cor)

        self.planets_rad.append(self.sun_rad)

        self.sun_img = pg.image.load("img/sun.png").convert_alpha()
        # self.sun_img = pg.transform.scale(self.sun_img, (self.sun_rad, self.sun_rad))

        self.planets_img.append(self.sun_img)

        """Mercury settings"""
        self.planets_rad.append(self.sun_rad // 72)

        self.planet_x_cor = self.sun_x_cor + 100
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/mercury.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Venus settings"""
        self.planets_rad.append(self.sun_rad // 28.8)

        self.planet_x_cor = self.sun_x_cor + 188
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/venus.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Earth settings"""
        self.planets_rad.append(self.sun_rad // 27.7)

        self.planet_x_cor = self.sun_x_cor + 260
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/earth.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Mars settings"""
        self.planets_rad.append(self.sun_rad // 51.4)

        self.planet_x_cor = self.sun_x_cor + 395
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/mars.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Jupiter settings"""
        self.planets_rad.append(self.sun_rad // 2.5)

        self.planet_x_cor = self.sun_x_cor + 1353
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/jupiter.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Saturn settings"""
        self.planets_rad.append(self.sun_rad // 3.3)

        self.planet_x_cor = self.sun_x_cor + 2484
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/saturn.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Uranus settings"""
        self.planets_rad.append(self.sun_rad // 6.8)

        self.planet_x_cor = self.sun_x_cor + 4990
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/uranus.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        """Neptune settings"""
        self.planets_rad.append(self.sun_rad // 10)

        self.planet_x_cor = self.sun_x_cor + 7831
        self.planet_y_cor = self.screen_height // 2 - \
            self.planets_rad[self.i] // 2

        self.planets_x.append(self.planet_x_cor)
        self.planets_y.append(self.planet_y_cor)

        self.planet_img = pg.image.load("img/neptune.png").convert_alpha()
        # self.planet_img = pg.transform.scale(self.planet_img, (self.planets_rad[self.i], self.planets_rad[self.i]))

        self.i += 1
        self.planets_img.append(self.planet_img)

        for k in range(len(self.planets_rad)):
            self.planets_rad[k] *= 2

        self.planets_rad = [*map(int, self.planets_rad)]

        for k in range(len(self.planets_img)):
            self.planets_img[k] = pg.transform.scale(
                self.planets_img[k],
                (
                    int(self.planets_rad[k] * self.max_size_koef_arr[k]),
                    int(self.planets_rad[k] * self.max_size_koef_arr[k])
                ))

        print(self.planets_rad)

        """Asteroids"""
        self.arr_astro = []
        self.astro_num = 300

        self.astro_img = pg.image.load("img/meteor.png").convert_alpha()
        # self.astro_img = pg.transform.scale(self.astro_img, (3, 3))

        """Satellite"""
        self.salt_info =\
            {
                3: {},
                5: {},
                6: {},
                7: {},
                8: {}
            }

        for k in self.salt_info.keys():
            self.salt_info[k]["speed"] = []
            self.salt_info[k]["a"] = []
            self.salt_info[k]["b"] = []
            self.salt_info[k]["rad"] = []
            self.salt_info[k]["pos"] = []
            self.salt_info[k]["img"] = []

        """Earth"""
        """The Moon"""
        d_s = 100

        self.salt_info[3]["speed"].append(13)
        self.salt_info[3]["a"].append(d_s)
        self.salt_info[3]["b"].append(d_s)
        self.salt_info[3]["rad"].append(self.sun_rad // 108)
        self.salt_info[3]["pos"].append(random.randint(0, 1000))
        self.salt_info[3]["img"].append(
            pg.image.load("img/moon.png").convert_alpha())

        """Jupyter"""
        """IO"""
        self.salt_info[5]["speed"].append(17.334 / 13.07 * 12)
        self.salt_info[5]["a"].append(d_s)
        self.salt_info[5]["b"].append(d_s)
        self.salt_info[5]["rad"].append(self.sun_rad // 108)
        self.salt_info[5]["pos"].append(random.randint(0, 1000))
        self.salt_info[5]["img"].append(
            pg.image.load("img/io.jpg").convert_alpha())

        """Europ"""
        self.salt_info[5]["speed"].append(13.74 / 13.07 * 12)
        self.salt_info[5]["a"].append(1.5 * d_s)
        self.salt_info[5]["b"].append(1.5 * d_s)
        self.salt_info[5]["rad"].append(self.sun_rad // 55)
        self.salt_info[5]["pos"].append(random.randint(0, 1000))
        self.salt_info[5]["img"].append(
            pg.image.load("img/europ.jpg").convert_alpha())

        """Ganimed"""
        self.salt_info[5]["speed"].append(10.88 / 13.07 * 12)
        self.salt_info[5]["a"].append(2.5 * d_s)
        self.salt_info[5]["b"].append(2.5 * d_s)
        self.salt_info[5]["rad"].append(self.sun_rad // 74)
        self.salt_info[5]["pos"].append(random.randint(0, 1000))
        self.salt_info[5]["img"].append(
            pg.image.load("img/ganimed.jpg").convert_alpha())

        """Kallisto"""
        self.salt_info[5]["speed"].append(8.2 / 13.07 * 12)
        self.salt_info[5]["a"].append(4.75 * d_s)
        self.salt_info[5]["b"].append(4.75 * d_s)
        self.salt_info[5]["rad"].append(self.sun_rad // 81)
        self.salt_info[5]["pos"].append(random.randint(0, 1000))
        self.salt_info[5]["img"].append(
            pg.image.load("img/kallisto.gif").convert_alpha())

        """Saturn"""
        """Japet"""
        self.salt_info[6]["speed"].append(2.9 / 9.69 * 29)
        self.salt_info[6]["a"].append(8.75 * d_s)
        self.salt_info[6]["b"].append(8.75 * d_s)
        self.salt_info[6]["rad"].append(self.sun_rad // 260)
        self.salt_info[6]["pos"].append(random.randint(0, 1000))
        self.salt_info[6]["img"].append(
            pg.image.load("img/japet.png").convert_alpha())

        """Rea"""
        self.salt_info[6]["speed"].append(6.75 / 9.69 * 29)
        self.salt_info[6]["a"].append(1.3 * d_s)
        self.salt_info[6]["b"].append(1.3 * d_s)
        self.salt_info[6]["rad"].append(self.sun_rad // 75)
        self.salt_info[6]["pos"].append(random.randint(0, 1000))
        self.salt_info[6]["img"].append(
            pg.image.load("img/rea.jpg").convert_alpha())

        """Titan"""
        self.salt_info[6]["speed"].append(1.6 / 9.69 * 29)
        self.salt_info[6]["a"].append(3 * d_s)
        self.salt_info[6]["b"].append(3 * d_s)
        self.salt_info[6]["rad"].append(self.sun_rad // 74)
        self.salt_info[6]["pos"].append(random.randint(0, 1000))
        self.salt_info[6]["img"].append(
            pg.image.load("img/titan.png").convert_alpha())

        """Uranus"""
        """Titania"""
        self.salt_info[7]["speed"].append(3.3 / 6.8 * 84)
        self.salt_info[7]["a"].append(d_s)
        self.salt_info[7]["b"].append(d_s)
        self.salt_info[7]["rad"].append(self.sun_rad // 250)
        self.salt_info[7]["pos"].append(random.randint(0, 1000))
        self.salt_info[7]["img"].append(
            pg.image.load("img/titania.png").convert_alpha())

        """Oberton"""
        self.salt_info[7]["speed"].append(2 / 6.8 * 84)
        self.salt_info[7]["a"].append(1.45 * d_s)
        self.salt_info[7]["b"].append(1.45 * d_s)
        self.salt_info[7]["rad"].append(self.sun_rad // 260)
        self.salt_info[7]["pos"].append(random.randint(0, 1000))
        self.salt_info[7]["img"].append(
            pg.image.load("img/oberon.jpg").convert_alpha())

        """Neptune"""
        """Triron"""
        self.salt_info[8]["speed"].append(4.7 / 5.5 * 165)
        self.salt_info[8]["a"].append(1.45 * d_s)
        self.salt_info[8]["b"].append(1.45 * d_s)
        self.salt_info[8]["rad"].append(self.sun_rad // 152)
        self.salt_info[8]["pos"].append(random.randint(0, 1000))
        self.salt_info[8]["img"].append(
            pg.image.load("img/triton.png").convert_alpha())

        print(self.planets_speed)
