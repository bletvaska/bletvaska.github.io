#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Nakreslíme obrázok.')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# zadefinujeme obrázok (pixel art ;)
picture = [
    "  XX XX  ",
    " X  X  X ",
    "X       X",
    "X       X",
    "X       X",
    " X     X ",
    "  X   X  ",
    "   X X   ",
    "    X    "
]


# vykresli!
picture.reverse()
dy = 0
for row in picture:
    dx = 0
    for col in row:
        if col != ' ':
            mc.setBlock(x + dx, y + dy, z, block.BRICK_BLOCK.id)
#         sleep(0.2)
        dx += 1
    dy += 1