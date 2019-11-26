import pygame as pg
import random
from settings import Settings
from dots import Dot
from dot_hole import Dot_hole
import functions as fu
import time
from pygame.locals import *


# Начинаем отсчет времени
time.perf_counter()

"""Main игровая функция"""


def run_game():
    flags = FULLSCREEN | DOUBLEBUF

    # Инциализация pygame
    pg.init()

    # Старт музыки
    pg.mixer.music.load('music/music.mp3')
    pg.mixer.music.play()

    # Зацикливание музыки
    pg.mixer.music.play(loops=-1)
    pg.mixer.music.set_volume(10)

    # Узнаем параметры окна пк
    infoObject = pg.display.Info()
    pg.font.init()  # you have to call this at the start,
    # if you want to use t1his module.5

    # Передача инфы о размерах эрана в настройки
    width = infoObject.current_w
    height = infoObject.current_h

    clock = pg.time.Clock()

    print('Screen size: ' + str(width) + 'x' + str(height))

    screen = pg.display.set_mode((width,
                                  height), DOUBLEBUF | FULLSCREEN)
    # screen = pg.display.set_mode((width//2, height//2))
    screen.set_alpha(None)
    settings = Settings(width, height)
    screen.convert_alpha()

    # Создание двух силей написания текста, для заголовка и обычного текста
    settings.title = pg.font.SysFont(settings.font, 56)
    settings.myfont = pg.font.SysFont(settings.font, 18)

    settings.hint_title = pg.font.SysFont(settings.font, 24)
    settings.hint_myfont = pg.font.SysFont(settings.font, 14)

    # screen = pg.display.set_mode(resolution, flags, bpp)

    # Инициализация нужных объектов
    fu.dot_init(settings, screen)
    fu.dot_hole_init(settings, screen)
    fu.create_planets(screen, settings)
    fu.astro_init(screen, settings)

    # Создание переменной с информацией о размерах экрана
    settings.screen_rect = pg.Rect(-100, -100, width + 200, height + 200)
    print(settings.screen_rect)

    # Прорисовка всех точке
    list(map(lambda i: i.draw_dot(), settings.object_dot))

    """Main цикл программы"""
    while True:
        clock.tick(60)
        fu.screen_update(screen, settings, clock)
        fu.check_events(screen, settings)


# Запуск main function приложения
if __name__ == '__main__':
    run_game()
    pg.quit()

# python -m cProfile -s time main.py
