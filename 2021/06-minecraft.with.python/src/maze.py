#!/usr/bin/env python3

from time import sleep
from datetime import datetime
import random

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Čo tak bludisko?')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# zadefinujeme číslice (pixel art ;)
maze = (
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X   X           X       X   X       X",
    "X   X   XXXXX   X   X   X   X   X   X",
    "X       X       X   X   X   X   X   X",
    "XXXXXXXXX   XXXXX   X   X   X   X   X",
    "X       X       X   X   X       X   X",
    "X   X   XXXXX   X   X   XXXXXXXXX   X",
    "X   X       X       X               X",
    "X   XXXXXXXXXXXXXXXXX   XXXXXXXXXXXXX",
    "X                   X       X       X",
    "X   XXXXXXXXXXXXX   XXXXX   X   X   X",
    "X       X       X           X   X   X",
    "XXXXX   X   XXXXXXXXXXXXXXXXXXXXX   X",
    "X       X               X           X",
    "X   XXXXXXXXXXXXX   X   XXXXX   X   X",
    "X               X   X   X       X   X",
    "XXXXXXXXXXXXX   X   X   X   XXXXX   X",
    "X                   X       X       X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
)


# draw maze
dz = 0
for row in maze:
    dx = 0
    for ch in row:
        block_id = block.AIR.id
        if ch != ' ':
            block_id = block.BEDROCK.id
            
        mc.setBlocks(x + dx + 1, y, z + dz, x + dx + 1, y + 3, z + dz, block_id)
        dx += 1
    dz += 1