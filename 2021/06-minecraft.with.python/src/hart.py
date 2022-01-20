from mcpi.minecraft import Minecraft
from mcpi import block

from time import sleep

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

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


dy = 0
for row in picture[::-1]:
    dx = 0
    for col in row:
        if col != ' ':
            mc.setBlock(x + dx, y + dy, z, block.BRICK_BLOCK.id)
            sleep(0.1)
        dx += 1
    dy += 1

