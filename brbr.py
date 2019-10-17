names_of_files = ['main.py', 'asteroids.py', 'dots.py', 'dot_hole.py',
    'functions.py', 'planets.py', 'settings.py']

with open('text.txt', 'w') as txt:
    for name in names_of_files:
        with open(name, 'r', encoding='utf-8') as file:
            for line in file:
                txt.write(line)
