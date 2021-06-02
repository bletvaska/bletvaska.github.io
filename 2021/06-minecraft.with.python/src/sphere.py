#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Urobíme guľu.')

# ziskanie hracovej pozicie
playerPos = mc.player.getPos()

radius = 10

for x in range(radius * -1, radius):
	for y in range(radius * -1, radius):
		for z in range(radius *- 1,radius):
			if x ** 2 + y ** 2 + z ** 2 < radius ** 2:
				mc.setBlock(playerPos.x + x, playerPos.y + y + radius, playerPos.z - z - 10, block.GOLD_BLOCK)