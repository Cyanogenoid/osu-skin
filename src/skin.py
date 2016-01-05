import sys

import yaml
from colormath.color_objects import sRGBColor, LCHuvColor, SpectralColor
from colormath.color_conversions import convert_color


config_yaml = '''
- General:
    Name: Cyanogenoid 0.2
    Author: Cyanogenoid
    Version: 2.5

    CursorRotate: 0
    CursorExpand: 0
    CursorCentre: 1


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
    # reference hue of cursor
    ref_spectral = SpectralColor(spec_550nm=1.0)
    ref_lch = convert_color(ref_spectral, LCHuvColor)
    # number of colors to generate
    n = 4
    # generate colors
    l = 75.0
    c = 50.0
    for i in range(n):
        # evenly spaced out hues excluding reference hue
        h = (i + 1) * 360 / (n + 1) + ref_lch.lch_h
        lch = LCHuvColor(l, c, h)
        rgb = convert_color(lch, sRGBColor, target_illuminant='d65')
        yield rgb.get_upscaled_value_tuple()


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
            key_content['Combo{}'.format(i)] = ', '.join(map(str, color))
        break

with open(sys.argv[1], 'w') as fd:
    for key in config:
        key_name, key_content = next(iter(key.items()))
        fd.write('[{}]\n'.format(key_name))
        for option, value in key_content.items():
            fd.write('{}: {}\n'.format(option, value))
