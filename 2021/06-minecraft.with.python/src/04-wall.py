#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Postavíme stenu.')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# kusok od hraca vyrastie stena
for row in range(5):
    for col in range(10):
        mc.setBlock(x + 1 + col, y + row, z, block.BRICK_BLOCK.id)
        sleep(0.2)
        
# pomocou jedného príkazu
mc.setBlocks(x + 1, y, z + 5, x + 1 + 10, y + 5, z + 5, block.BRICK_BLOCK.id)