# osu! skin

This is a skin for [osu!](https://osu.ppy.sh/) that is intended to be very clean.
It is highly optimised for readability.

## Features
- Simple, white cursor. Human eyes are better at distinguishing contrast than colour hues [citation needed], so visibility is maximised by having a white cursor on a black background.
- Perceptually uniform combo colours. By using combo colours that have the same brightness and colourfulness in the sophisticated CIECAM02-LCS colourspace, no colour stands out from the others and the player can devote equal focus to every circle.
- Semi-transparent hitcircles. This makes it easier to see stacks compared to opaque circles while reducing clutter compared to fully transparent circles.
- Hidden life bar and combo counter. Looking at these during gameplay is more often than not a bad idea.


## Dependencies
- Make
- Python 3 (Might work in 2, untested)
- PyYAML / LibYAML
- Inkscape (Must be in PATH)
- Scour (for SVG optimisation)

## Build Instructions
Run `python make.py`, then `make`.
