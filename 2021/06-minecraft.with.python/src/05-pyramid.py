#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Postavíme pyramídu.')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()
height = 9

# kusok od hraca vyrastie stena
for floor in range(height, 0, -2):
    x += 1
    z += 1
    for row in range(floor):
        for col in range(floor):
            mc.setBlock(x + col, y, z + row, block.BRICK_BLOCK.id)
            sleep(0.2)
    y += 1