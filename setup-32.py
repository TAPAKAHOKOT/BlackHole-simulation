import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\igrok\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\igrok\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6'

base = 'Win32GUI'

tcl = "C:/Users/igrok/AppData/Local/Programs/Python/Python37-32/DLLs/tcl86t.dll"
tk = "C:/Users/igrok/AppData/Local/Programs/Python/Python37-32/DLLs/tk86t.dll"

vcruntime140 = "vcruntime140-32.dll"

packages = ["pygame", "random", "math", "sys", "time"]
include_files = ["img/earth.png", "img/jupiter.png", "img/mars.png", "img/mercury.png",
"img/neptune.png", "img/saturn.png", "img/sun.png", "img/uranus.png", "img/venus.png",
"img/meteor.png", tcl, tk, vcruntime140, "python37-32.dll",
"music/music.mp3", "img/question.png","img/settings_ico.png",
"text/all_text_eng.txt", "text/all_text_ru.txt", "text/hint_hole_eng.txt",
"text/hint_hole_ru.txt", "text/hint_solar_eng.txt", "text/hint_solar_ru.txt",
"text/text_planets_eng.txt", "text/text_planets_ru.txt", "font/font.ttf"]
includes = ["dots", "dot_hole", "functions", "planets", "settings"]


# executables = []

cx_Freeze.setup(
    name = "Black Hole",
    options = {"build_exe": {"packages": packages,
                            "include_files": include_files,
                            "includes" : includes,
                            'include_msvcr': True
                            }},
    executables = [cx_Freeze.Executable("main.py",
                                        base = base,
                                        icon = "ico.ico",
                                        targetName = "Space.exe")],
    version='1.5.0'
)
