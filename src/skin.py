import sys

import yaml
import numpy as np
import colorspacious as col


config_yaml = '''
- General:
    Name: Cyanogenoid 0.3
    Author: Cyanogenoid
    Version: 2.5

    CursorRotate: 0
    CursorExpand: 0
    CursorCentre: 1

    AllowSliderBallTint: 1

- Colours:
    SliderTrackOverride: 0, 0, 0
    SliderBorder: 91, 91, 91

    SongSelectActiveText: 255, 255, 255
    SongSelectInactiveText: 192, 192, 192

    MenuGlow: 255, 255, 255
    InputOverlayText: 0, 127, 57


- Fonts:
    HitCirclePrefix: score
    HitCircleOverlap: 0

    ComboPrefix: combo
    ComboOverlap: 0

    ScorePrefix: score
    ScoreOverlap: 0
'''

config = yaml.load(config_yaml)


def generate_combo_colours():
    n_colors = 3
    colorfulness = 20
    brightness = 60

    for i in range(n_colors):
        hue = i * (2 * np.pi) / n_colors
        Jab = [brightness, colorfulness * np.cos(hue), colorfulness * np.sin(hue)]
        sRGB255 = col.cspace_convert(Jab, "CAM02-LCD", 'sRGB255')
        sRGB255 = np.clip(np.round(sRGB255), 0, 255)
        yield sRGB255


def generate_mania(keys):
    c = {}
    c['Keys'] = keys
    return c


for keys in range(4, 9):
    mania = generate_mania(keys)
    config.append({'Mania': mania})

for entry in config:
    key_name, key_content = next(iter(entry.items()))
    if key_name == 'Colours':
        for i, color in enumerate(generate_combo_colours(), start=1):
            key_content['Combo{}'.format(i)] = ', '.join(map('{:.0f}'.format, color))
        break

with open(sys.argv[1], 'w') as fd:
    for key in config:
        key_name, key_content = next(iter(key.items()))
        fd.write('[{}]\n'.format(key_name))
        for option, value in key_content.items():
            fd.write('{}: {}\n'.format(option, value))
