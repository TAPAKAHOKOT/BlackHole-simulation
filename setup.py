import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\igrok\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\igrok\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6'

base = 'Win32GUI'

tcl = "C:/Users/igrok/AppData/Local/Programs/Python/Python38-32/DLLs/tcl86t.dll"
tk = "C:/Users/igrok/AppData/Local/Programs/Python/Python38-32/DLLs/tk86t.dll"

# vcruntime140 = "C:/Windows/WinSxS/x86_avg.vc140.crt_f92d94485545da78_14.0.27012.0_none_b7a28364e4fdb0e3/vcruntime140.dll"

packages = ["pygame", "random", "math", "sys", "time"]
include_files = [tcl, tk,
                 "music/music.mp3", "font/font.ttf"]

images = ["img/" + k for k in os.listdir("img")]
text = ["text/" + k for k in os.listdir("text")]

include_files += images + text

includes = ["dots", "dot_hole", "functions", "planets", "settings"]


executables = []

cx_Freeze.setup(
    name="Black Hole",
    options={"build_exe": {"packages": packages,
                           "include_files": include_files,
                           "includes": includes,
                           'include_msvcr': True
                           }},
    executables=[cx_Freeze.Executable("main.py",
                                      base=base,
                                      icon="ico.ico",
                                      targetName="Space.exe")],
    version='1.5.0'
)
