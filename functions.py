import pygame as pg
import sys
from dots import Dot
import random
import math as m
from dot_hole import Dot_hole
from planets import Planets
from asteroids import Astro
import time


"""Функция обномления всей информации на экране"""


def screen_update(screen, settings, clock):

    object_dot = []

    # Заливка экрана черным фоном
    screen.fill((0, 0, 0))

    create_lang_changer(screen, settings)

    # dark_hole_mooving(screen, settings)

    # if time.perf_counter() - settings.time_1 >= 1:
    #     settings.time_1 = time.perf_counter()-0.5
    #     settings.fps /= 2

    # settings.fps += 1
    #
    # fps_num = round(settings.fps/(time.perf_counter() - settings.time_1))

    settings.fps = round(clock.get_fps())

    text_title = settings.hint_myfont.render(str(settings.fps),
                                             True, (255, 255, 255))
    screen.blit(text_title, (10, settings.screen_height - 30))

    if settings.click == 1:
        """Запускается, если режим черной дыры"""
        black_hole_mode(screen, settings)

    elif settings.click == -1:
        """Запускается, если режим солнечной системы"""

        solar_system_mode(screen, settings)

    draw_hint(screen, settings)

    # Включение/отключение поля с текстом по мере приближения и отдаления
    if settings.size_koef >= settings.max_size_koef_arr[settings.follow_koef] / 1.1:
        settings.frame = True
    else:
        settings.frame = False

    # обновление окна
    pg.display.flip()


"""Режим солнечной системы"""


def solar_system_mode(screen, settings):
    text = settings.all_text[settings.lang_txt_change][4]

    text_title = settings.myfont.render(str(settings.solar_time) + text,
                                        True, (255, 255, 255))
    screen.blit(text_title, (settings.screen_width // 2 - 10, 20))

    time_slider(screen, settings)
    size_slider(screen, settings)

    using_sliders(screen, settings)

    # Обновление положений всех планет
    if not settings.zoomed:
        list(map(lambda i: i.update(), settings.object_planets))

    # Прорисовка всех точек
    list(map(lambda i: i.draw_dot(settings.red_border), settings.obj_dot_hole))

    # обновление всех точек
    update_dot_hole(screen, settings)
# Обновление положения планет, для следования за выбранной планетой
    settings.new_x_for_planets =\
        settings.object_planets[settings.follow_koef].x_cor
    settings.new_y_for_planets =\
        settings.object_planets[settings.follow_koef].y_cor
    update_planets_cors(screen, settings)

    # Создает поле с текстом при достаточном приближении к планете
    if settings.frame:
        create_frame(screen, settings)


"""Режим черной дыры"""


def black_hole_mode(screen, settings):
    if settings.settings_frame:
        if settings.set_alpha < 200:
            settings.set_alpha += 4
        create_settings_frame(screen, settings)
    else:
        if settings.set_alpha > 0:
            settings.set_alpha -= 4
            create_settings_frame(screen, settings)

    settings.settings_img = settings.settings_img.convert()
    settings.settings_img.set_alpha(120)
    screen.blit(settings.settings_img, (settings.screen_width - 30, 10))

    ar = random.randint(0, settings.dot_num - 1)
    p = settings.object_dot[ar]
    p.rad = random.randint(settings.min_dot_radius, settings.max_dot_radius)

    # Создание формы центра черной дыры

    dark_dot = pg.draw.circle(screen, (0, 0, 0), (settings.gravity_point_x,
                                                  settings.gravity_point_y), 10)
    # Я знаю, тебе страшно это читать
    # Прорисовка всех звезд
    update_dot(screen, settings)

    def clip_check(i):
        i.draw_dot()

        if i.rect.clip(dark_dot):
            try:
                if i.last_dot.clip(dark_dot):
                    settings.object_dot.remove(i)
                    create_dot(screen, settings)
            except AttributeError:
                print("Dot' object has no attribute 'last_dot'")

    [clip_check(i) for i in settings.object_dot]

    # Передвижение черной дыры за курсором при нажатии лкм
    black_hole_following(screen, settings)
    # orange_dot_2 = pg.draw.circle(screen, (221,75,12), (settings.gravity_point_x, settings.gravity_point_y), 13)
    # white_dot = pg.draw.circle(screen, (249,239,221), (settings.gravity_point_x, settings.gravity_point_y), 12)
    dark_dot = pg.draw.circle(screen, (0, 0, 0),
                              (settings.gravity_point_x, settings.gravity_point_y), 30)


"""Рисует подсказки управления"""


def draw_hint(screen, settings):
    settings.question_img = settings.question_img.convert()
    # settings.question_img.set_alpha(90)
    screen.blit(settings.question_img, (10, 10))

    if settings.hint:
        if settings.hint_alpha < 60:
            settings.hint_alpha += 1
            settings.text_alpha += 4
        create_hint(screen, settings)
    else:
        if settings.hint_alpha > 0:
            settings.hint_alpha -= 1
            settings.text_alpha -= 4
            create_hint(screen, settings)

    if settings.hint_hole:
        if settings.hint_hole_alpha < 240:
            settings.hint_hole_alpha += 4
            # settings.text_alpha += 4
        hole_hint(screen, settings)
    else:
        if settings.hint_hole_alpha > 0:
            settings.hint_hole_alpha -= 4
            hole_hint(screen, settings)

    if settings.hint_solar:
        if settings.hint_solar_alpha < 240:
            settings.hint_solar_alpha += 4
            # settings.text_alpha += 4
        solar_hint(screen, settings)
    else:
        if settings.hint_solar_alpha > 0:
            settings.hint_solar_alpha -= 4
            solar_hint(screen, settings)


"""Проверка использования слайдера"""


def using_sliders(screen, settings):
    if settings.slider_hold:
        m_pos = pg.mouse.get_pos()[0]

        if m_pos > settings.screen_width // 1.5:
            m_pos = settings.screen_width // 1.5
        elif m_pos < settings.screen_width // 3:
            m_pos = settings.screen_width // 3

        for i in settings.object_planets:
            # i.t = 210 * 13
            i.t += round((settings.slider_x1 - m_pos)
                         / (-settings.size_koef * 30), 3)
            i.update()

        for i in settings.arr_astro:
            # i.t = 210 * 13
            i.t += (settings.slider_x1 - m_pos)\
                / (-settings.size_koef * 30)
            i.update()

        settings.slider_x1 = m_pos

    step = ((settings.max_size_koef_arr[settings.follow_koef])
            / (settings.screen_height // 2.65 - settings.screen_height // 1.5))
    if settings.size_slider_y_hold:

        m_pos = pg.mouse.get_pos()[1]
        if m_pos > settings.screen_height // 1.5:
            m_pos = settings.screen_height // 1.5
        elif m_pos < settings.screen_height // 2.65:
            m_pos = settings.screen_height // 2.65

        settings.size_slider_y = m_pos

        settings.size_koef =\
            (m_pos - settings.screen_height // 1.5) * step + 0.015

        settings.slider_pos_old = settings.slider_pos_now
        settings.slider_pos_now = m_pos

        if settings.slider_pos_old > settings.slider_pos_now:
            for i in settings.obj_dot_hole:
                i.zoom_on(settings.size_koef, settings.max_size_koef)
        elif settings.slider_pos_old < settings.slider_pos_now:
            for i in settings.obj_dot_hole:
                i.zoom_off(settings.size_koef)

        update_planets_size(screen, settings)
        # settings.size_slider_y = m_pos

    else:
        settings.size_slider_y = (settings.size_koef +
                                  settings.screen_height // 1.5 * step - 0.015) / (step)


"""Инициализация всех точек при черной дыре"""


def dot_init(settings, screen):
    for k in range(settings.dot_num):
        dot = Dot(settings, screen)
        settings.object_dot.append(dot)


"""Инициализация астероидов"""


def astro_init(screen, settings):
    for k in range(settings.astro_num):
        astro = Astro(screen, settings)
        settings.arr_astro.append(astro)


"""Инициализация всех точек при солнечной системе"""


def dot_hole_init(settings, screen):
    for k in range(settings.dot_hole_num):
        dot = Dot_hole(settings, screen)
        settings.obj_dot_hole.append(dot)


"""Обновление всех точек при Черной дыре"""


def update_dot(screen, settings):
    if settings.object_dot:
        list(map(lambda i: i.update(settings), settings.object_dot))


"""Обновление всех точек при Солнечной системе"""


def update_dot_hole(screen, settings):
    list(map(lambda i: i.update(), settings.obj_dot_hole))


"""Создание всех планет"""


def create_planets(screen, settings):
    print('\n')
    for k in range(len(settings.planets_img)):
        planet = Planets(settings, screen, k)
        print(settings.planets_names[k]
              + settings.all_text[settings.lang_txt_change][0]
              + '( ' + str(planet.x) + '; ' + str(planet.y) + ')')
        settings.object_planets.append(planet)
        planet.draw_planets()


"""Обновление всех планет"""


def update_system(screen, settings):
    planets = Planets(settings, screen)
    planets.update(settings)


"""Создание всех точек при черной дыре"""


def create_dot(screen, settings):
    dot = Dot(settings, screen)
    settings.object_dot.append(dot)
    dot.draw_dot()


"""Изменение центра гравитации при смене положения черной дыры"""


def change_gravity(screen, settings, x, y):
    settings.hole_x = x
    settings.hole_y = y

    settings.gravity_point_x = int(x)
    settings.gravity_point_y = int(y)

    # Перебор всех точек
    for i in settings.object_dot:
        i.proj_dot_x = abs(i.x - settings.gravity_point_x)
        i.proj_dot_y = abs(i.y - settings.gravity_point_y)

        i.gravity_coef_x = settings.gravity_point_x / settings.screen_width
        i.gravity_coef_y = settings.gravity_point_y / settings.screen_height

        i.del_x = settings.screen_width * i.gravity_coef_x
        i.del_y = settings.screen_height * i.gravity_coef_y
    # Перезапуск движения
    restart_moving(screen, settings)


"""Перезапуск движения"""


def restart_moving(screen, settings):
    settings.staying_dots.clear()
    for i in settings.object_dot:
        i.tors_speed = random.randint(1000, 5000) / settings.tors_speed_koef

        i.radius_dot_dist = m.sqrt(i.proj_dot_x**2 + i.proj_dot_y**2)
        i.step = random.randint(settings.max_speed, settings.min_speed)
        i.staying = random.randint(1, settings.staying_dots_part)

        if i.dark_whole == 1:
            i.speed_x = 0
            i.speed_y = 0

            i.dot_speed_whole = random.randint(settings.whole_speed_max,
                                               settings.whole_speed_min)

            if i.radius_dot_dist <= i.whole_rad\
                    and i.radius_dot_dist >= i.whole_rad // 1.5:
                i.speed_x = abs((i.x -
                                 settings.screen_width * i.gravity_coef_x) / i.step)
                i.speed_y = abs((i.y -
                                 settings.screen_height * i.gravity_coef_y) / i.step)
            elif i.radius_dot_dist < i.whole_rad // 1.5\
                    and i.radius_dot_dist >= i.whole_rad // 2:
                i.speed_x = abs((i.x -
                                 settings.screen_width * i.gravity_coef_x) / (i.step / 2))
                i.speed_y = abs((i.y -
                                 settings.screen_height * i.gravity_coef_y) / (i.step / 2))
            elif i.radius_dot_dist < i.whole_rad // 2:
                i.speed_x = abs((i.x -
                                 settings.screen_width * i.gravity_coef_x) / (i.step / 10))
                i.speed_y = abs((i.y -
                                 settings.screen_height * i.gravity_coef_y) / (i.step / 10))

        elif i.dark_whole == -1:
            i.staying_arg = 0
            i.step = random.randint(settings.max_speed, settings.min_speed)
            i.speed_x = abs((i.x -
                             settings.screen_width * i.gravity_coef_x) / i.step)
            i.speed_y = abs((i.y -
                             settings.screen_height * i.gravity_coef_y) / i.step)
            if i.staying == 1 and sum(settings.staying_dots)\
                    < settings.dot_num // settings.staying_dots_part:
                i.staying_arg = 1
                i.speed_x = 0
                i.speed_y = 0

        settings.staying_dots.append(i.staying_arg)


"""Изменение размеров планет при приближении или отдалении"""


def update_planets_size(screen, settings, check=10):

    if not settings.red_border:
        for i in settings.arr_astro:
            index = settings.arr_astro.index(i)

            if settings.size_koef < 0.07:
                i.img = pg.transform.scale(settings.astro_img, (3, 3))
            elif settings.size_koef < 0.2:
                i.img = pg.transform.scale(settings.astro_img, (4, 4))
            else:
                i.img = pg.transform.scale(settings.astro_img, (6, 6))

        for i in settings.object_planets:
            index = settings.object_planets.index(i)

            if int(settings.planets_rad[index] * settings.size_koef) > 1:
                if i.shadow.clip(settings.screen_rect)\
                        or check == index or check == 'all':

                    i.planet_img = pg.transform.scale(settings.planets_img[index],
                                                      (int(settings.planets_rad[index] * settings.size_koef),
                                                       int(settings.planets_rad[index] * settings.size_koef)))
                else:
                    i.planet_img = pg.transform.scale(settings.planets_img[index],
                                                      (int(settings.planets_rad[index] * 0.001),
                                                       int(settings.planets_rad[index] * 0.001)))
            else:
                i.planet_img = pg.transform.scale(settings.planets_img[index],
                                                  (2, 2))


"""Попытка сделать движущуюся черную дыру (отключено)"""


def dark_hole_mooving(screen, settings):

    settings.hole_x += settings.x_speed * 0.8 * settings.speed_hole_koef
    settings.hole_y += settings.y_speed * 0.8 * settings.speed_hole_koef

    if settings.hole_x > settings.screen_width:
        settings.hole_x = 0
    elif settings.hole_x < 0:
        settings.hole_x = settings.screen_width

    if settings.hole_y > settings.screen_height:
        settings.hole_y = 0
    elif settings.hole_y < 0:
        settings.hole_y = settings.screen_height

    x = settings.hole_x
    y = settings.hole_y

    settings.change_speed_counter += 1

    if settings.change_speed_counter == -100:
        settings.x_speed = random.randint(-10, 10) / 10
        settings.y_speed = random.randint(-10, 10) / 10

        settings.change_speed_counter = 0

    settings.gravity_point_x += int(x)
    settings.gravity_point_y += int(y)

    settings.staying_dots.clear()
    change_gravity(screen, settings, x, y)
    restart_moving(screen, settings)


"""Изменение координат точек при планетах"""


def update_dots_in_solar_cors(screen, settings):
    for i in settings.obj_dot_hole:

        i.x += settings.new_x_for_planets
        i.y += settings.new_y_for_planets

        i.pos_change()


"""Изменение координат планет"""


def update_planets_cors(screen, settings):

    koef = settings.follow_koef
    x = settings.new_x_for_planets
    y = settings.new_y_for_planets

    """Астероиды"""
    for i in settings.arr_astro:
        if koef == 0:
            i.x_0 = settings.middle[0]
            i.y_0 = settings.middle[1]
        else:
            i.x_0 += settings.middle[0] - x\
                - int(settings.planets_rad[koef] // 2 * settings.size_koef)
            i.y_0 += settings.middle[1] - y\
                - int(settings.planets_rad[koef] // 2 * settings.size_koef)

        i.update()
        if not settings.red_border:
            i.draw()
        else:
            i.draw_shadow()

    """Планеты"""
    for i in settings.object_planets:
        if koef == 0:
            i.x_0 = settings.middle[0]
            i.y_0 = settings.middle[1]
        else:
            i.x_0 += settings.middle[0] - x\
                - int(settings.planets_rad[koef] // 2 * settings.size_koef)
            i.y_0 += settings.middle[1] - y\
                - int(settings.planets_rad[koef] // 2 * settings.size_koef)

        i.update()
        i.draw_planets_rect()
        if not settings.red_border:
            if settings.size_koef > 1:
                if i.shadow.clip(settings.screen_rect):
                    try:
                        update_planets_size(screen, settings, koef)
                    except:
                        None
                    i.draw_planets()
            else:
                try:
                    update_planets_size(screen, settings, koef)
                except:
                    None
                i.draw_planets()


"""Добавление пунктов смены языка"""


def create_lang_changer(screen, settings):
    width = settings.screen_width
    height = settings.screen_height

    x, size, txt = 3, 60, "Ru"
    for k in range(2):

        if settings.lang_hover_on == k:
            if settings.lang_heights[k] < 5:
                settings.lang_heights[k] += 1
        else:
            if settings.lang_heights[k] > 0:
                settings.lang_heights[k] -= 1

        y = settings.lang_heights[k]

        hint = pg.Rect((width - size, height - 30 - y, width, height))
        hint_surf = pg.Surface((30, 30))
        hint_surf.fill((255, 255, 255))
        hint_surf.set_alpha(50 + 100 * abs(settings.lang_txt_change - k))
        screen.blit(hint_surf, hint)

        text_title = settings.myfont.render(txt, True, (0, 0, 0))
        screen.blit(text_title, (width - (size - x), height - 27 - y))

        x, size, txt = 1, 30, "Eng"


"""Добавление меню подсказки"""


def create_hint(screen, settings):
    x = 0
    hint = pg.Rect((0, 0, 480, 100))
    hint_surf = pg.Surface((480, 100))
    hint_surf.fill((100, 100, 100))
    hint_surf.set_alpha(settings.hint_alpha / 2)
    screen.blit(hint_surf, hint)

    hint_2 = pg.Rect((40, 20, 190, 50))
    hint_surf_2 = pg.Surface((190, 50))
    hint_surf_2.fill((100, 100, 100))
    hint_surf_2.set_alpha(settings.hint_alpha * 2)
    screen.blit(hint_surf_2, hint_2)

    if settings.lang_txt_change == 1:
        x = 15
    color = (settings.text_alpha, settings.text_alpha, settings.text_alpha)
    text_title = settings.myfont.render(
        settings.all_text[settings.lang_txt_change][1], True, (0, 0, 0))
    screen.blit(text_title, (70 + x, 32))

    hint_3 = pg.Rect((250, 20, 200, 50))
    hint_surf_3 = pg.Surface((200, 50))
    hint_surf_3.fill((100, 100, 100))
    hint_surf_3.set_alpha(settings.hint_alpha * 2)
    screen.blit(hint_surf_3, hint_3)

    color = (settings.text_alpha, settings.text_alpha, settings.text_alpha)
    text_title = settings.myfont.render(
        settings.all_text[settings.lang_txt_change][2], True, (0, 0, 0))
    screen.blit(text_title, (270, 32))


"""Создание подсказки для режима с черной дырой"""


def hole_hint(screen, settings):
    txt = settings.text_hole.split('|')
    hint_4 = pg.Rect((0, 100, 240, 500))
    hint_surf_4 = pg.Surface((240, 500))
    hint_surf_4.fill((30, 30, 30))
    hint_surf_4.set_alpha(settings.hint_hole_alpha // 4)
    screen.blit(hint_surf_4, hint_4)

    koef = 450 / len(txt)
    y = 0
    for k in range(len(txt)):
        txt_hint = pg.Rect((0, 140 + y, 240, 140 + y))
        txt_hint_surf = pg.Surface((240, 60))
        txt_hint_surf.fill((30, 30, 30))
        txt_hint_surf.set_alpha(settings.hint_hole_alpha)
        screen.blit(txt_hint_surf, txt_hint)

        y += koef
    y = 0
    for k in range(len(txt)):
        color = (settings.text_alpha, settings.text_alpha, settings.text_alpha)
        text = settings.myfont.render(txt[k], True, (0, 0, 0))
        screen.blit(text, (5, 160 + y))
        y += koef


"""Создание подсказки для режима с солнечной системой"""


def solar_hint(screen, settings):
    txt = settings.text_solar.split('|')
    hint_5 = pg.Rect((240, 100, 240, 500))
    hint_surf_5 = pg.Surface((240, 500))
    hint_surf_5.fill((30, 30, 30))
    hint_surf_5.set_alpha(settings.hint_solar_alpha / 4)
    screen.blit(hint_surf_5, hint_5)

    koef = 450 / len(txt)
    y = 0
    for k in range(len(txt)):
        txt_hint = pg.Rect((240, 140 + y, 240, 140 + y))
        txt_hint_surf = pg.Surface((240, 60))
        txt_hint_surf.fill((30, 30, 30))
        txt_hint_surf.set_alpha(settings.hint_solar_alpha)
        screen.blit(txt_hint_surf, txt_hint)

        y += koef
    y = 0
    for k in range(len(txt)):
        color = (settings.text_alpha, settings.text_alpha, settings.text_alpha)
        text = settings.myfont.render(txt[k], True, (0, 0, 0))
        screen.blit(text, (245, 160 + y))
        y += koef


"""создание поля с текстом"""


def create_frame(screen, settings):
    text = settings.text_arr[settings.follow_koef].split('[')
    text[0] = text[0].replace('\n', ' ')
    text[1] = text[1].split('\n')

    left_frame = pg.Rect((0, settings.screen_height // 8,
                          settings.screen_width + 30, settings.screen_height // 6))

    left_surf = pg.Surface((settings.screen_width // 6 + 30,
                            settings.screen_height - settings.screen_height // 4))

    left_surf.fill((20, 20, 20))
    left_surf.set_alpha(50)
    text_title = settings.title.render(text[0], True, (255, 255, 255))

    screen.blit(left_surf, left_frame)
    screen.blit(text_title, (35, settings.screen_height // 8))

    for k in range(len(text[1])):
        text_about = settings.hint_title.render(
            text[1][k], True, (255, 255, 255))
        screen.blit(text_about, (40, settings.screen_height // 6 + k * 28))


"""Перемещение черной дыры за мышкой"""


def black_hole_following(screen, settings):
    if settings.black_hole_following:
        x, y = pg.mouse.get_pos()

        settings.staying_dots.clear()
        change_gravity(screen, settings, x, y)


"""Создает слидер для перемотки времени"""


def time_slider(screen, settings):
    pg.draw.line(screen, (15, 15, 15),
                 [settings.screen_width // 3, settings.screen_height - 40],
                 [settings.screen_width // 1.5, settings.screen_height - 40], 2)

    x_1 = settings.slider_x1
    x_2 = int(5)

    y_1 = settings.slider_y1
    y_2 = int(20)

    pg.draw.rect(screen, (100, 100, 100), (x_1, y_1, x_2, y_2))


"""Создает слайер для зума"""


def size_slider(screen, settings):
    pg.draw.line(screen, (15, 15, 15),
                 [settings.screen_width - 30, settings.screen_height // 2.65],
                 [settings.screen_width - 30, settings.screen_height // 1.5], 2)

    x_1 = settings.size_slider_x
    x_2 = int(20)

    y_1 = settings.size_slider_y
    y_2 = int(5)

    pg.draw.rect(screen, (100, 100, 100), (x_1, y_1, x_2, y_2))


"""Создать вкладку настроек"""


def create_settings_frame(screen, settings):
    text = settings.text_arr[settings.follow_koef].split('[')
    text[0] = text[0].replace('\n', ' ')
    text[1] = text[1].split('\n')

    left_frame = pg.Rect((settings.screen_width - 250, 0,
                          settings.screen_width - 30, 30))

    left_surf = pg.Surface((250, 50))

    left_surf.fill((40, 40, 40))
    left_surf.set_alpha(settings.set_alpha)

    screen.blit(left_surf, left_frame)

    text_title = settings.hint_myfont.render(settings.all_text[settings.lang_txt_change][3],
                                             False, (0, 0, 0))
    screen.blit(text_title, (settings.screen_width - 245, 0))

    arr = ['250', '500', '1000']
    y = 200
    color = (0, 0, 0)

    for k in range(3):
        if settings.hover_on == k:
            if settings.heights[k] < 5:
                settings.heights[k] += 1
        else:
            if settings.heights[k] > 0:
                settings.heights[k] -= 1

        if settings.settings_chosen == k:
            color = (240, 240, 240)
        else:
            color = (0, 0, 0)

        text_title = settings.hint_title.render(arr[k], False, color)
        text_title.set_alpha(settings.set_alpha)
        screen.blit(text_title, (settings.screen_width -
                                 y, 20 - settings.heights[k]))

        y -= 60


"""Изменение кол-ва точек при нажатии на вкладку настроек"""


def change_num_dots(screen, settings):

    settings.first_time = time.perf_counter()
    settings.object_dot.clear()
    settings.staying_dots.clear()
    dot_init(settings, screen)

    for i in settings.object_dot:
        i.draw_dot()

        i.staying = random.randint(1, settings.staying_dots_part)

        if i.dark_whole == -1 and i.staying == 1 and sum(settings.staying_dots)\
                < settings.dot_num // settings.staying_dots_part:
            i.staying_arg = 1
            i.speed_x = 0
            i.speed_y = 0
        else:
            i.staying_arg = 0

        settings.staying_dots.append(i.staying_arg)


"""Изменяет файлы с текстом под нужный язык"""


def change_lang(settings):
    settings.text_hole =\
        settings.hole_hint_txt[settings.lang_txt_change]
    settings.text_solar =\
        settings.solar_hint_txt[settings.lang_txt_change]
    settings.text_arr =\
        settings.text_planets[settings.lang_txt_change]


def check_change_lang(screen, settings):
    width = settings.screen_width
    height = settings.screen_height

    if pg.mouse.get_pos()[0] > width - 60\
            and pg.mouse.get_pos()[0] < width - 30\
            and pg.mouse.get_pos()[1] > height - 35\
            and pg.mouse.get_pos()[1] < height:
        settings.lang_txt_change = 1
        change_lang(settings)
        return 0
    elif pg.mouse.get_pos()[0] > width - 30\
            and pg.mouse.get_pos()[0] < width\
            and pg.mouse.get_pos()[1] > height - 35\
            and pg.mouse.get_pos()[1] < height:
        settings.lang_txt_change = 0
        change_lang(settings)
        return 0
    else:
        return 1


"""Проверка собыйти мыши"""


def check_mouse_events(screen, settings, event):
    settings.size_bool = False

    settings.freeze_speed = 0
    settings.zoomed = False

    for i in settings.arr_astro:
        i.x_0 = settings.middle[0]
        i.y_0 = settings.middle[1]

    for i in settings.object_planets:
        i.x_0 = settings.middle[0]
        i.y_0 = settings.middle[1]

    """Левая кнопка мыши"""
    if event.button == 1:

        if check_change_lang(screen, settings):

            if settings.click == 1:
                if pg.mouse.get_pos()[0] > settings.x_points[0]\
                        and pg.mouse.get_pos()[0] < settings.x_points[1]\
                        and pg.mouse.get_pos()[1] < 50\
                        and pg.mouse.get_pos()[1] > 30:

                    if settings.settings_chosen != 0:
                        settings.settings_chosen = 0
                        settings.dot_num = 250
                        change_num_dots(screen, settings)

                elif pg.mouse.get_pos()[0] > settings.x_points[2]\
                        and pg.mouse.get_pos()[0] < settings.x_points[3]\
                        and pg.mouse.get_pos()[1] < 50\
                        and pg.mouse.get_pos()[1] > 30:
                    if settings.settings_chosen != 1:
                        settings.settings_chosen = 1
                        settings.dot_num = 500
                        change_num_dots(screen, settings)

                elif pg.mouse.get_pos()[0] > settings.x_points[4]\
                        and pg.mouse.get_pos()[0] < settings.x_points[5]\
                        and pg.mouse.get_pos()[1] < 50\
                        and pg.mouse.get_pos()[1] > 30:
                    if settings.settings_chosen != 2:
                        settings.settings_chosen = 2
                        settings.dot_num = 1000
                        change_num_dots(screen, settings)

                else:
                    settings.black_hole_following = True

        if settings.click == -1:
            plus = 20
            for k in range(9):
                if pg.mouse.get_pos()[0] > settings.planets_x_cors[k] - plus\
                    and pg.mouse.get_pos()[0] < settings.planets_x_cors[k]\
                        + settings.planets_rad[k] * settings.size_koef + plus\
                    and pg.mouse.get_pos()[1] > settings.planets_y_cors[k] - plus\
                    and pg.mouse.get_pos()[1] < settings.planets_y_cors[k]\
                        + settings.planets_rad[k] * settings.size_koef + plus:
                    if settings.size_koef >= settings.max_size_koef:
                        check = True

                    else:
                        check = False

                    settings.follow_koef = k

                    settings.max_size_koef =\
                        settings.max_size_koef_arr[settings.follow_koef]

                    if settings.size_koef > settings.max_size_koef or check == True:
                        settings.size_koef = settings.max_size_koef

                    update_planets_size(screen, settings, settings.follow_koef)
            if settings.slider_x1 - 55 < pg.mouse.get_pos()[0] < settings.slider_x1 + 65\
                    and settings.slider_y1 - 10 < pg.mouse.get_pos()[1] < settings.slider_y1 + 30:
                settings.slider_hold = True
            elif settings.size_slider_x - 10 < pg.mouse.get_pos()[0] < settings.size_slider_x + 30\
                    and settings.size_slider_y - 25 < pg.mouse.get_pos()[1] < settings.size_slider_y + 35:
                settings.size_slider_y_hold = True

    """Правая кнопка мыши"""
    if event.button == 3:
        if settings.click == -1:
            if settings.size_koef >= settings.max_size_koef:
                check = True
            else:
                check = False

            settings.follow_koef += 1

            if settings.follow_koef > 8:
                settings.follow_koef = 0

            settings.max_size_koef =\
                settings.max_size_koef_arr[settings.follow_koef]

            if settings.size_koef > settings.max_size_koef or check == True:
                settings.size_koef = settings.max_size_koef

            update_planets_size(screen, settings, settings.follow_koef)

        elif settings.click != -1:

            settings.first_time = time.perf_counter()
            settings.object_dot.clear()
            settings.staying_dots.clear()
            dot_init(settings, screen)

            for i in settings.object_dot:
                i.draw_dot()

                i.staying = random.randint(1, settings.staying_dots_part)

                if i.dark_whole == -1 and i.staying == 1\
                    and sum(settings.staying_dots) <\
                        settings.dot_num // settings.staying_dots_part:
                    i.staying_arg = 1
                    i.speed_x = 0
                    i.speed_y = 0
                else:
                    i.staying_arg = 0

                settings.staying_dots.append(i.staying_arg)

    """Колесико мыши вверх"""
    if event.button == 4:
        if settings.sun_system_koef == 1:
            if settings.speed_hole_koef != 1:
                settings.max_speed = 25
                settings.min_speed = 800

                settings.speed_hole_koef = 1

                settings.tors_speed_koef = 1000

                settings.whole_speed_max = 5
                settings.whole_speed_min = 40
                restart_moving(screen, settings)
                #
                # for i in settings.object_dot:
                #     if i.tors_size
        else:
            for i in settings.obj_dot_hole:
                i.zoom_on(settings.size_koef, settings.max_size_koef)

            if settings.size_koef < settings.max_size_koef:
                check = True
            else:
                check = False

            if settings.size_koef >= settings.max_size_koef:
                None
            elif settings.size_koef >= 25:
                settings.size_koef += 4

            elif settings.size_koef >= 12:
                settings.size_koef += 1.5

            elif settings.size_koef >= 6:
                settings.size_koef += 1

            elif settings.size_koef >= 4:
                settings.size_koef += 0.5

            elif settings.size_koef >= 1:
                settings.size_koef += 0.15

            elif settings.size_koef >= 0.1:
                settings.size_koef += 0.03

            elif settings.size_koef >= 0.01:
                settings.size_koef += 0.006
            else:
                settings.size_koef += 0.006

            if settings.size_koef > settings.max_size_koef:
                settings.size_koef = settings.max_size_koef
            if settings.size_koef != 14 and check == True:

                update_planets_size(screen, settings)
                # settings.new_x_for_planets =\
                #     settings.object_planets[settings.follow_koef].x
                # settings.new_y_for_planets =\
                #     settings.object_planets[settings.follow_koef].y
                # update_planets_cors(screen, settings)

    """Колесико мыши вниз"""
    if event.button == 5:
        if settings.sun_system_koef == 1:
            if settings.speed_hole_koef != 0.01:
                settings.max_speed = 10000
                settings.min_speed = 100000

                settings.speed_hole_koef = 0.01

                settings.tors_speed_koef = 200000

                settings.whole_speed_max = 5000
                settings.whole_speed_min = 500000000
                restart_moving(screen, settings)

        else:
            for i in settings.obj_dot_hole:
                i.zoom_off(settings.size_koef)
            if settings.size_koef >= 25:
                settings.size_koef -= 5

            if settings.size_koef >= 10:
                settings.size_koef -= 2

            if settings.size_koef >= 6:
                settings.size_koef -= 1

            elif settings.size_koef >= 4:
                settings.size_koef -= 0.25

            elif settings.size_koef >= 1:
                settings.size_koef -= 0.2

            elif settings.size_koef >= 0.1:
                settings.size_koef -= 0.03

            elif settings.size_koef >= 0.015:
                settings.size_koef -= 0.006

            if settings.size_koef - 0.015 <= 0:
                settings.size_koef = 0.015

            update_planets_size(screen, settings)
            settings.new_x_for_planets =\
                settings.object_planets[settings.follow_koef].x
            settings.new_y_for_planets =\
                settings.object_planets[settings.follow_koef].y
            update_planets_cors(screen, settings)

    """Нажатие на колесико мыши"""
    if event.button == 2:
        settings.time_hold = time.perf_counter()

        """
        if settings.sun_system_koef == -1:
            for i in settings.object_planets:
                i.t -= 10

                print(0)
                i.update()
        """


"""Функция для изменения системы (на черную дыру или солнечную)"""


def change_system(screen, settings):
    settings.click *= -1
    if settings.click == -1:
        pg.mouse.set_visible(True)
    elif settings.click == 1:
        pg.mouse.set_visible(True)

    settings.sun_system_koef *= -1

    if settings.sun_system_koef == -1:
        settings.staying_dots.clear()
        settings.object_dot.clear()
    else:
        dot_init(settings, screen)

        dark_dot = pg.draw.circle(screen, (0, 0, 0),
                                  (settings.gravity_point_x, settings.gravity_point_y), 10)

        for i in settings.object_dot:
            i.draw_dot()
            if i.rect.clip(dark_dot):
                settings.object_dot.remove(i)
                create_dot(screen, settings)


"""проверка всех событий"""


def check_events(screen, settings):
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:

            width = settings.screen_width
            height = settings.screen_height

            if pg.mouse.get_pos()[0] > width - 60\
                    and pg.mouse.get_pos()[0] < width - 30\
                    and pg.mouse.get_pos()[1] > height - 35\
                    and pg.mouse.get_pos()[1] < height:
                settings.lang_hover_on = 0
            elif pg.mouse.get_pos()[0] > width - 30\
                    and pg.mouse.get_pos()[0] < width\
                    and pg.mouse.get_pos()[1] > height - 35\
                    and pg.mouse.get_pos()[1] < height:
                settings.lang_hover_on = 1
            else:
                settings.lang_hover_on = 2

            if pg.mouse.get_pos()[0] > settings.screen_width - 200\
                    and pg.mouse.get_pos()[0] < settings.screen_width - 170\
                    and pg.mouse.get_pos()[1] < 50 \
                    and pg.mouse.get_pos()[1] > 30:
                settings.hover_on = 0

            elif pg.mouse.get_pos()[0] > settings.screen_width - 140\
                    and pg.mouse.get_pos()[0] < settings.screen_width - 110\
                    and pg.mouse.get_pos()[1] < 50\
                    and pg.mouse.get_pos()[1] > 30:
                settings.hover_on = 1

            elif pg.mouse.get_pos()[0] > settings.screen_width - 80\
                    and pg.mouse.get_pos()[0] < settings.screen_width - 40\
                    and pg.mouse.get_pos()[1] < 50\
                    and pg.mouse.get_pos()[1] > 30:
                settings.hover_on = 2
            else:
                settings.hover_on = -1

            if pg.mouse.get_pos()[0] > settings.screen_width - 35\
                    and pg.mouse.get_pos()[0] < settings.screen_width - 5\
                    and pg.mouse.get_pos()[1] < 35 \
                    and pg.mouse.get_pos()[1] > 5:
                settings.settings_frame = True
            elif settings.settings_frame == True\
                    and pg.mouse.get_pos()[0] > settings.screen_width - 250\
                    and pg.mouse.get_pos()[0] < settings.screen_width - 5\
                    and pg.mouse.get_pos()[1] < 55 \
                    and pg.mouse.get_pos()[1] > 5:
                settings.settings_frame = True
            else:
                settings.settings_frame = False

            if settings.hint:
                if pg.mouse.get_pos()[0] > 250 and pg.mouse.get_pos()[0] < 450\
                        and pg.mouse.get_pos()[1] > 20\
                        and pg.mouse.get_pos()[1] < 70:
                    settings.hint_solar = True
                else:
                    settings.hint_solar = False

                if pg.mouse.get_pos()[0] > 40 and pg.mouse.get_pos()[0] < 230\
                        and pg.mouse.get_pos()[1] > 20\
                        and pg.mouse.get_pos()[1] < 70:
                    settings.hint_hole = True
                else:
                    settings.hint_hole = False

            if pg.mouse.get_pos()[0] > 10 and pg.mouse.get_pos()[0] < 35\
                    and pg.mouse.get_pos()[1] > 10\
                    and pg.mouse.get_pos()[1] < 35:
                settings.question_img.set_alpha(60)
            else:
                settings.question_img.set_alpha(240)

            if pg.mouse.get_pos()[0] > 13 and pg.mouse.get_pos()[0] < 35\
                    and pg.mouse.get_pos()[1] > 13\
                    and pg.mouse.get_pos()[1] < 35:
                settings.hint = True

            if pg.mouse.get_pos()[1] > 110 or pg.mouse.get_pos()[0] > 510:
                settings.hint = False
        """Если клавиша мыши отжата, то"""
        if event.type == pg.MOUSEBUTTONUP:

            """Отжата левая кнопка мыши"""
            if event.button == 1:
                settings.black_hole_following = False

                settings.slider_hold = False
                settings.size_slider_y_hold = False
                settings.zoom_event = False

            """Отжато колесико"""
            if event.button == 2:
                if time.perf_counter() - settings.time_hold >= 0.2:
                    change_system(screen, settings)
                else:
                    if settings.speed_hole_koef != 0.1:
                        settings.max_speed = 100
                        settings.min_speed = 5000

                        settings.speed_hole_koef = 0.1

                        settings.tors_speed_koef = 10000

                        settings.whole_speed_max = 100
                        settings.whole_speed_min = 1000
                        restart_moving(screen, settings)

        # Событие нажатие мыши
        if event.type == pg.MOUSEBUTTONDOWN:
            check_mouse_events(screen, settings, event)

        # Событие нажание крестика
        if event.type == pg.QUIT:
            print(len(settings.object_dot))
            sys.exit()
        # Событие нажатие на клавишу клавиатуры
        elif event.type == pg.KEYDOWN:
            if settings.sun_system_koef == -1:

                if settings.size_koef >= settings.max_size_koef:
                    check = True
                else:
                    check = False

                if event.key == pg.K_0:
                    # settings.zoom_speed = 0.05
                    # settings.size_bool = True
                    settings.follow_koef = 0
                    # settings.freeze_speed = 1
                    # settings.max_size_koef = 6

                elif event.key == pg.K_1:
                    settings.follow_koef = 1

                elif event.key == pg.K_2:
                    settings.follow_koef = 2

                elif event.key == pg.K_3:
                    settings.follow_koef = 3

                elif event.key == pg.K_4:
                    settings.follow_koef = 4

                elif event.key == pg.K_5:
                    settings.follow_koef = 5

                elif event.key == pg.K_6:
                    settings.follow_koef = 6

                elif event.key == pg.K_7:
                    settings.follow_koef = 7

                elif event.key == pg.K_8:
                    settings.follow_koef = 8

                settings.max_size_koef =\
                    settings.max_size_koef_arr[settings.follow_koef]
                # settings.size_num = settings.max_size_koef_arr[settings.follow_koef]

                update_planets_size(screen, settings, settings.follow_koef)

                if settings.size_koef > settings.max_size_koef or check == True:
                    settings.size_koef = settings.max_size_koef

                    update_planets_size(screen, settings, settings.follow_koef)

                keys = pg.key.get_pressed()

                if keys[pg.K_b] and keys[pg.K_r] and keys[pg.K_d]\
                        and keys[pg.K_LALT]:
                    if settings.red_border:
                        settings.red_border = False
                        update_planets_size(screen, settings, 'all')

                    else:
                        settings.red_border = True
                        update_planets_size(screen, settings, 'all')

            """Проверка для выхода из проги"""
            if event.key == pg.K_ESCAPE:
                print('\n')
                print('Size koef. : ' + str(settings.size_koef))
                print('Num of the dots (solar system) = '
                      + str(len(settings.obj_dot_hole)))
                sys.exit()

            keys = pg.key.get_pressed()
            if keys[pg.K_c] and keys[pg.K_LALT] and keys[pg.K_LCTRL]:
                if settings.click != -1:
                    settings.dark_whole_index *= -1

                    for i in settings.object_dot:
                        i.proj_dot_x = abs(i.x - settings.gravity_point_x)
                        i.proj_dot_y = abs(i.y - settings.gravity_point_y)

                        i.dark_whole *= -1
                    restart_moving(screen, settings)

            if event.key == pg.K_g:
                change_system(screen, settings)


# Плавное приближение
"""
Плавное приближение и отдаление
if settings.zoom_off:
    settings.size_koef -= 1

    update_planets_size(screen, settings)

    if settings.size_koef <= 4:
        settings.zoom_off = False
"""
# Отменяет плавное приближение при выборе планеты
# settings.size_bool = False

# Плавное приближение при выборе планеты
"""
if settings.size_bool:

    settings.size_koef += settings.zoom_speed

    update_planets_size(screen, settings)

    settings.update_size_moving = False


    if settings.size_koef >= settings.size_num:
        settings.size_bool = False
"""


# Картинка на фоне
"""
if settings.click == -1:
    screen.fill((0,0,0))
else:
    screen.blit(settings.fon, (0, 0))
    screen.blit(settings.fon_surf, settings.for_rect)
"""
