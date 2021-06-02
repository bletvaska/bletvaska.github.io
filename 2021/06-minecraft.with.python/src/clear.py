#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Vyčistíme oblasť.')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# kusok od hraca sa urobi fuga
mc.setBlocks(x + 1, y, z, x + 50, y + 50, z + 50, block.AIR.id)
