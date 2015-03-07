import sys

from PIL import Image


img = Image.open(sys.argv[1])
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b, a = pixels[i,j]
        if r == g == b:
            pixels[i,j] = (255, 255, 255, a)
img.save(sys.argv[1])
