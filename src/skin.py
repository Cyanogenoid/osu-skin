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
    HitCirclePrefix: score
    HitCircleOverlap: 0

    ComboPrefix: combo
    ComboOverlap: 0

    ScorePrefix: score
    ScoreOverlap: 0

'''

config = yaml.load(config_yaml)


with open(sys.argv[1], 'w') as fd:
    for key in config:
        key_name, key_content = next(iter(key.items()))
        fd.write('[{}]\n'.format(key_name))
        for option, value in key_content.items():
            fd.write('{}: {}\n'.format(option, value))
        fd.write('''[Mania]
Keys: 4
// Aesthetic HD
// Mania 4k config

UpsideDown: 0
JudgementLine: 0

HitPosition: 405
ScorePosition: 324
ComboPosition: 128

// Combo
ColourBreak: 255,76,76,255
ColourHold: 255,255,255,192

//Barline
ColourBarline: 255,255,255,48

// Columns
ColumnStart: 356
ColumnWidth: 32,36,36,32

// ColumnLine
ColourColumnLine: 255,255,255,12

//Colours
Colour1: 14,10,15,150
Colour2: 0,0,0,150
Colour3: 0,0,0,150
Colour4: 14,10,15,150

//Stagelight
LightFramePerSecond: 12
ColourLight1: 198,84,255,150
ColourLight2: 255,255,255,150
ColourLight3: 255,255,255,150
ColourLight4: 198,84,255,150

// Notes
NoteImage0: mania/note/purple
NoteImage0H: mania/note/purple
NoteImage0L: mania/sustain/purple
NoteImage1: mania/note/white
NoteImage1H: mania/note/white
NoteImage1L: mania/sustain/white
NoteImage2: mania/note/white
NoteImage2H: mania/note/white
NoteImage2L: mania/sustain/white
NoteImage3: mania/note/purple
NoteImage3H: mania/note/purple
NoteImage3L: mania/sustain/purple

//Keys
KeyImage0: mania/key/purple
KeyImage0D: mania/key/purple-down
KeyImage1: mania/key/white
KeyImage1D: mania/key/white-down
KeyImage2: mania/key/white
KeyImage2D: mania/key/white-down
KeyImage3: mania/key/purple
KeyImage3D: mania/key/purple-down

ColumnLineWidth: 0,0,2,0,0
[Mania]
Keys: 5
// Aesthetic HD
// Mania 5k config

UpsideDown: 0
JudgementLine: 0

HitPosition: 405
ScorePosition: 324
ComboPosition: 128

// Combo
ColourBreak: 255,76,76,255
ColourHold: 255,255,255,192

// Barline
ColourBarline: 255,255,255,48

// Columns
ColumnStart: 342
ColumnWidth: 32,36,32,36,32

// ColumnLine
ColourColumnLine: 255,255,255,12

// Colours
Colour1: 14,10,15,150
Colour2: 0,0,0,150
Colour3: 12,15,10,150
Colour4: 0,0,0,150
Colour5: 14,10,15,150

// Stagelight
LightFramePerSecond: 12
ColourLight1: 198,84,255,150
ColourLight2: 255,255,255,150
ColourLight3: 141,255,84,150
ColourLight4: 255,255,255,150
ColourLight5: 198,84,255,150

// Notes
NoteImage0: mania/note/purple
NoteImage0H: mania/note/purple
NoteImage0L: mania/sustain/purple
NoteImage1: mania/note/white
NoteImage1H: mania/note/white
NoteImage1L: mania/sustain/white
NoteImage2: mania/note/green
NoteImage2H: mania/note/green
NoteImage2L: mania/sustain/green
NoteImage3: mania/note/white
NoteImage3H: mania/note/white
NoteImage3L: mania/sustain/white
NoteImage4: mania/note/purple
NoteImage4H: mania/note/purple
NoteImage4L: mania/sustain/purple

// Keys
KeyImage0: mania/key/purple
KeyImage0D: mania/key/purple-down
KeyImage1: mania/key/white
KeyImage1D: mania/key/white-down
KeyImage2: mania/key/green
KeyImage2D: mania/key/green-down
KeyImage3: mania/key/white
KeyImage3D: mania/key/white-down
KeyImage4: mania/key/purple
KeyImage4D: mania/key/purple-down

// Daily dose

ColumnLineWidth: 0,0,0,0,0,0
[Mania]
Keys: 6
// Aesthetic HD
// Mania 6k config

UpsideDown: 0
JudgementLine: 0

HitPosition: 405
ScorePosition: 324
ComboPosition: 128

// Combo
ColourBreak: 255,76,76,255
ColourHold: 255,255,255,192

// Barline
ColourBarline: 255,255,255,48

// Columns
ColumnStart: 322
ColumnWidth: 36,32,36,36,32,36

// ColumnLine
ColourColumnLine: 255,255,255,12

// Colours
Colour1: 0,0,0,150
Colour2: 15,10,12,150
Colour3: 0,0,0,150
Colour4: 0,0,0,150
Colour5: 15,10,12,150
Colour6: 0,0,0,150

// Stagelight
LightFramePerSecond: 12
ColourLight1: 255,255,255,150
ColourLight2: 255,84,141,150
ColourLight3: 255,255,255,150
ColourLight4: 255,255,255,150
ColourLight5: 255,84,141,150
ColourLight6: 255,255,255,150

// Notes
NoteImage0: mania/note/white
NoteImage0H: mania/note/white
NoteImage0L: mania/sustain/white
NoteImage1: mania/note/pink
NoteImage1H: mania/note/pink
NoteImage1L: mania/sustain/pink
NoteImage2: mania/note/white
NoteImage2H: mania/note/white
NoteImage2L: mania/sustain/white
NoteImage3: mania/note/white
NoteImage3H: mania/note/white
NoteImage3L: mania/sustain/white
NoteImage4: mania/note/pink
NoteImage4H: mania/note/pink
NoteImage4L: mania/sustain/pink
NoteImage5: mania/note/white
NoteImage5H: mania/note/white
NoteImage5L: mania/sustain/white

// Keys
KeyImage0: mania/key/white
KeyImage0D: mania/key/white-down
KeyImage1: mania/key/pink
KeyImage1D: mania/key/pink-down
KeyImage2: mania/key/white
KeyImage2D: mania/key/white-down
KeyImage3: mania/key/white
KeyImage3D: mania/key/white-down
KeyImage4: mania/key/pink
KeyImage4D: mania/key/pink-down
KeyImage5: mania/key/white
KeyImage5D: mania/key/white-down

ColumnLineWidth: 0,0,0,2,0,0,0
[Mania]
Keys: 7
// Aesthetic HD
// Mania 7k config

UpsideDown: 0
JudgementLine: 0

HitPosition: 405
ScorePosition: 324
ComboPosition: 128

// Combo
ColourBreak: 255,76,76,255
ColourHold: 255,255,255,192

// Barline
ColourBarline: 255,255,255,48

// Columns
ColumnStart: 306
ColumnWidth: 36,32,36,32,36,32,36

// ColumnLine
ColourColumnLine: 255,255,255,12

// Colours
Colour1: 0,0,0,150
Colour2: 10,14,15,150
Colour3: 0,0,0,150
Colour4: 12,15,10,150
Colour5: 0,0,0,150
Colour6: 10,14,15,150
Colour7: 0,0,0,150

// Stagelight
LightFramePerSecond: 12
ColourLight1: 255,255,255,150
ColourLight2: 84,227,255,150
ColourLight3: 255,255,255,150
ColourLight4: 141,255,84,150
ColourLight5: 255,255,255,150
ColourLight6: 84,227,255,150
ColourLight7: 255,255,255,150

// Notes
NoteImage0: mania/note/white
NoteImage0H: mania/note/white
NoteImage0L: mania/sustain/white
NoteImage1: mania/note/blue
NoteImage1H: mania/note/blue
NoteImage1L: mania/sustain/blue
NoteImage2: mania/note/white
NoteImage2H: mania/note/white
NoteImage2L: mania/sustain/white
NoteImage3: mania/note/green
NoteImage3H: mania/note/green
NoteImage3L: mania/sustain/green
NoteImage4: mania/note/white
NoteImage4H: mania/note/white
NoteImage4L: mania/sustain/white
NoteImage5: mania/note/blue
NoteImage5H: mania/note/blue
NoteImage5L: mania/sustain/blue
NoteImage6: mania/note/white
NoteImage6H: mania/note/white
NoteImage6L: mania/sustain/white

// Keys
KeyImage0: mania/key/white
KeyImage0D: mania/key/white-down
KeyImage1: mania/key/blue
KeyImage1D: mania/key/blue-down
KeyImage2: mania/key/white
KeyImage2D: mania/key/white-down
KeyImage3: mania/key/green
KeyImage3D: mania/key/green-down
KeyImage4: mania/key/white
KeyImage4D: mania/key/white-down
KeyImage5: mania/key/blue
KeyImage5D: mania/key/blue-down
KeyImage6: mania/key/white
KeyImage6D: mania/key/white-down

ColumnLineWidth: 0,0,0,0,0,0,0,0
[Mania]
Keys: 8
// Aesthetic HD
// Mania 8k config

UpsideDown: 0
JudgementLine: 0

HitPosition: 405
ScorePosition: 324
ComboPosition: 128

// Combo
ColourBreak: 255,76,76,255
ColourHold: 255,255,255,192

// Barline
ColourBarline: 255,255,255,48

// Columns
ColumnStart: 290
ColumnWidth: 36,32,36,32,32,36,32,36

// ColumnLine
ColourColumnLine: 255,255,255,12

// Colours
Colour1: 0,0,0,150
Colour2: 10,14,15,150
Colour3: 0,0,0,150
Colour4: 15,14,10,150
Colour5: 15,14,10,150
Colour6: 0,0,0,150
Colour7: 10,14,15,150
Colour8: 0,0,0,150

// Stagelight
LightFramePerSecond: 12
ColourLight1: 255,255,255,150
ColourLight2: 84,227,255,150
ColourLight3: 255,255,255,150
ColourLight4: 255,198,84,150
ColourLight5: 255,198,84,150
ColourLight6: 255,255,255,150
ColourLight7: 84,227,255,150
ColourLight8: 255,255,255,150

// Notes
NoteImage0: mania/note/white
NoteImage0H: mania/note/white
NoteImage0L: mania/sustain/white
NoteImage1: mania/note/blue
NoteImage1H: mania/note/blue
NoteImage1L: mania/sustain/blue
NoteImage2: mania/note/white
NoteImage2H: mania/note/white
NoteImage2L: mania/sustain/white
NoteImage3: mania/note/yellow
NoteImage3H: mania/note/yellow
NoteImage3L: mania/sustain/yellow
NoteImage4: mania/note/yellow
NoteImage4H: mania/note/yellow
NoteImage4L: mania/sustain/yellow
NoteImage5: mania/note/white
NoteImage5H: mania/note/white
NoteImage5L: mania/sustain/white
NoteImage6: mania/note/blue
NoteImage6H: mania/note/blue
NoteImage6L: mania/sustain/blue
NoteImage7: mania/note/white
NoteImage7H: mania/note/white
NoteImage7L: mania/sustain/white

// Keys
KeyImage0: mania/key/white
KeyImage0D: mania/key/white-down
KeyImage1: mania/key/blue
KeyImage1D: mania/key/blue-down
KeyImage2: mania/key/white
KeyImage2D: mania/key/white-down
KeyImage3: mania/key/yellow
KeyImage3D: mania/key/yellow-down
KeyImage4: mania/key/yellow
KeyImage4D: mania/key/yellow-down
KeyImage5: mania/key/white
KeyImage5D: mania/key/white-down
KeyImage6: mania/key/blue
KeyImage6D: mania/key/blue-down
KeyImage7: mania/key/white
KeyImage7D: mania/key/white-down

ColumnLineWidth: 0,0,0,0,2,0,0,0,0

''')
