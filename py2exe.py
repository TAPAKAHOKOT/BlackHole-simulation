import os
import shutil
import sys

main_dir = 'D:/git/BlackHole-simulation'
v_arr = ['32']

for k in range(len(v_arr)):
    v = v_arr[k]

    dir_here = main_dir
    os.chdir(dir_here)

    try:
        shutil.rmtree('Black Hole x' + v)
    except:
        pass

    if v == '32':
        python_name = 'python'
        python_v = '32'
    else:
        python_name = 'python'
        python_v = '-amd64'

    if v == '64':
        os.system(python_name + ' setup.py build')
    else:
        os.system(python_name + ' setup.py build')

    os.chdir(dir_here + '/build')

    os.rename(main_dir + "/build/exe.win" + python_v + "-3.8",
              main_dir + "/Black Hole x" + v)

    os.chdir(dir_here)
    shutil.rmtree('build')

    dir_build = main_dir + "/Black Hole x" + v
    os.chdir(dir_build)

    arr = os.listdir()

    try:
        os.makedirs('img')
        os.makedirs('music')
        os.makedirs('text')
        os.makedirs('font')
    except:
        pass

    for k in arr:
        if "." in k:
            if k[-3:] == "png" or k[-3:] == "jpg" or k[-3:] == "gif":
                print("renaming {} to {}".format(k, 'img/' + k))
                os.rename(k, 'img/' + k)
            elif k[-3:] == "txt":
                print("renaming {} to {}".format(k, 'img/' + k))
                os.rename(k, 'text/' + k)
            elif k[-3:] == "mp3":
                print("renaming {} to {}".format(k, 'img/' + k))
                os.rename(k, 'music/' + k)
            elif k[-3:] == "ttf":
                print("renaming {} to {}".format(k, 'img/' + k))
                os.rename(k, 'font/' + k)


sys.exit()
