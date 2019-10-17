import  os
import shutil
import sys

main_dir = 'D:/Python/PyGame/Black_hole_test'
v_arr = ['64', '32']

for k in range(2):
    v = v_arr[k]

    dir_here = main_dir
    os.chdir(dir_here)

    try: shutil.rmtree('Black Hole x' + v)
    except: None


    if v == '32':
        python_name = 'python32'
        python_v = '32'
    else:
        python_name = 'python'
        python_v = '-amd64'

    if v == '64':
        os.system(python_name + ' setup.py build')
    else:
        os.system(python_name + ' setup-32.py build')

    os.chdir(dir_here + '/build')

    os.rename(main_dir + "/build/exe.win" + python_v + "-3.7",
                main_dir + "/Black Hole x" + v)

    os.chdir(dir_here)
    shutil.rmtree('build')


    dir_build = main_dir + "/Black Hole x" + v
    os.chdir(dir_build)


    os.makedirs('img')
    os.makedirs('music')
    os.makedirs('text')
    os.makedirs('font')

    os.rename('font.ttf', 'font/font.ttf')

    os.rename('earth.png', 'img/earth.png')
    os.rename('jupiter.png', 'img/jupiter.png')
    os.rename('mars.png', 'img/mars.png')
    os.rename('mercury.png', 'img/mercury.png')
    os.rename('neptune.png', 'img/neptune.png')
    os.rename('saturn.png', 'img/saturn.png')
    os.rename('sun.png', 'img/sun.png')
    os.rename('uranus.png', 'img/uranus.png')
    os.rename('venus.png', 'img/venus.png')
    os.rename('meteor.png', 'img/meteor.png')

    os.rename('question.png', 'img/question.png')
    os.rename('settings_ico.png', 'img/settings_ico.png')

    os.rename('music.mp3', 'music/music.mp3')

    if v == '32':
        try: os.remove('python37.dll')
        except: pass
        os.rename('python37-32.dll', 'python37.dll')
        os.rename('vcruntime140-32.dll', 'vcruntime140.dll')

    os.rename('all_text_eng.txt', 'text/all_text_eng.txt')
    os.rename('all_text_ru.txt', 'text/all_text_ru.txt')

    os.rename('hint_hole_eng.txt', 'text/hint_hole_eng.txt')
    os.rename('hint_hole_ru.txt', 'text/hint_hole_ru.txt')

    os.rename('hint_solar_eng.txt', 'text/hint_solar_eng.txt')
    os.rename('hint_solar_ru.txt', 'text/hint_solar_ru.txt')

    os.rename('text_planets_eng.txt', 'text/text_planets_eng.txt')
    os.rename('text_planets_ru.txt', 'text/text_planets_ru.txt')

sys.exit()
