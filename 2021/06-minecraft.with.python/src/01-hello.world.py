#!/usr/bin/env python3


from mcpi.minecraft import Minecraft
from oliver import Config

# pripojenie
mc = Minecraft.create(Config.server, Config.port)
mc.postToChat('Ahoj Minecraft!')
