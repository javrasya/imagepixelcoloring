from PIL import Image
import math

__author__ = 'ahmetdal'

im = Image.open('/home/ahmetdal/Pictures/mesut.jpg')
pix = im.load()
rgb_im = im.convert('RGB')

bordeaux = (145, 23, 38)
blue = (70, 160, 255)

for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):
        r, g, b = rgb_im.getpixel((i, j))
        if 70 < r < 200 and 30 < g < 130 and 70 < b < 170:
            pix[i, j] = bordeaux
        elif 70 < r < 200 and 140 < g < 230 and 180 < b < 300:
            pix[i, j] = blue

    #for j in range(0, im.size[1]):
    #    r, g, b = rgb_im.getpixel((i, j))
    #    if 100 < r < 140 and 90 < g < 140 and 120 < b < 190:
    #        if (math.ceil((i + 1) / 11.0) + math.ceil((j + 1) / 11.0)) % 2 == 0:
    #            pix[i, j] = bordeaux
    #            v1 = i - (i % 11)
    #            v2 = j - (j % 11)
    #            for k in range(v1, v1 + 11):
    #                if k < im.size[0] and pix[k, j] == blue:
    #                    pix[k, j] = bordeaux
    #            for l in range(v2, v2 + 11):
    #                if l < im.size[1] and pix[i, l] == blue:
    #                    pix[i, l] = bordeaux
    #
    #        else:
    #            pix[i, j] = blue
    #            v1 = i - (i % 11)
    #            v2 = j - (j % 11)
    #            for k in range(v1, v1 + 11):
    #                if k < im.size[0] and pix[k, j] == bordeaux:
    #                    pix[k, j] = blue
    #            for l in range(v2, v2 + 11):
    #                if l < im.size[1] and pix[i, l] == bordeaux:
    #                    pix[i, l] = blue

im.save('/home/ahmetdal/Pictures/edited2.png', 'PNG')
