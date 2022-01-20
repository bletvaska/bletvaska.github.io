#!/usr/bin/env python3

from time import sleep

from mcpi.minecraft import Minecraft
from mcpi import block

# from oliver import Config

# pripojenie
mc = Minecraft.create() #Config.server)
mc.postToChat('Vytvoríme nad hlavou jeden blok.')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# nad hlavou spravím blok
mc.setBlock(x, y + 2, z, block.FLOWER_CYAN.id)