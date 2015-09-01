import sys

import yaml


config_yaml = '''
- General:
    Name: Cyanogenoid 0.1
    Author: Cyanogenoid
    Version: 2.5

    CursorRotate: 0
    CursorExpand: 0
    CursorCentre: 1


- Colours:
    Combo1: 0, 162, 255
    Combo2: 255, 187, 0
    Combo3: 255, 61, 0

    SliderTrackOverride: 0, 0, 0
    SliderBorder: 91, 91, 91

    SongSelectActiveText: 255, 255, 255
    SongSelectInactiveText: 192, 192, 192

    MenuGlow: 255, 255, 255
    InputOverlayText: 0, 127, 57


- Fonts:
    HitCirclePrefix: default
    HitCircleOverlap: 159

    ComboPrefix: combo
    ComboOverlap: 0

    ScorePrefix: score
    ScoreOverlap: 0
'''

config = yaml.load(config_yaml)


def generate_mania(keys):
    c = {}
    c['Keys'] = keys
    return c


for keys in range(4, 9):
    mania = generate_mania(keys)
    config.append({'Mania': mania})

with open(sys.argv[1], 'w') as fd:
    for key in config:
        key_name, key_content = next(iter(key.items()))
        fd.write('[{}]\n'.format(key_name))
        for option, value in key_content.items():
            fd.write('{}: {}\n'.format(option, value))
