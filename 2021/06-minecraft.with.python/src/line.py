#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Vytvoríme stĺp vysoký 20 blokov.')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# kusok od hraca vyrastie stlp do vysky
for i in range(20):
    mc.setBlock(x + 1, y + i, z, block.IRON_BLOCK.id)
    sleep(1)