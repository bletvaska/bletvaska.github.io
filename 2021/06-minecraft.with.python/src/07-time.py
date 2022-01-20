#!/usr/bin/env python3

from time import sleep
from datetime import datetime
import random

from mcpi.minecraft import Minecraft
from mcpi import block

# pripojenie
mc = Minecraft.create()
mc.postToChat('Zobrazíme aktuálny čas ;)')

# ziskanie hracovej pozicie
x, y, z = mc.player.getTilePos()

# zadefinujeme číslice (pixel art ;)
digits = (
    (
        " XXXXX  ",
        "XXX XXX ",
        "XX   XX ",
        "XX   XX ",
        "XX   XX ",
        "XXX XXX ",
        " XXXXX  ",
        "        "
    ),
    (
        "   XX   ",
        "  XXX   ",
        "  XXX   ",
        "   XX   ",
        "   XX   ",
        "  XXXXX ",
        " XXXXX  ",
        "        "
    ),
    (
        " XXXXX  ",
        "XX  XXX ",
        "X  XXX  ",
        "  XXX   ",
        " XXX    ",
        "XXX  XX ",
        "XXXXXXX ",
        "        "
    ),
    (
        " XXXXXX ",
        "XX  XX  ",
        "X  XX   ",
        "  XXXX  ",
        "    XXX ",
        "XX  XXX ",
        " XXXXX  ",
        "        "
    ),
    (
        " XX     ",
        "XX  X   ",
        "XX XX   ",
        " XXXXXX ",
        "   XX   ",
        "   XX   ",
        "   X    ",
        "        "
    ),
    (
        "XXXXXX  ",
        " XX  XX ",
        " XX     ",
        " XXXXX  ",
        "    XXX ",
        "XX  XXX ",
        " XXXXX  ",
        "        "
    ),
    (
        "  XXXX  ",
        " XX     ",
        "XX XXX  ",
        "XXXX XX ",
        "XX    X ",
        "XXX  XX ",
        " XXXXX  ",
        "        "
    ),
    (
        " XXXXXX ",
        "XXX  XX ",
        "    XXX ",
        "   XXX  ",
        "  XXX   ",
        "  XX    ",
        "  XX    ",
        "        "
    ),
    (
        " XXXXX  ",
        "XXX XXX ",
        "XX   XX ",
        " XXXXX  ",
        "XX   XX ",
        "XXX XXX ",
        " XXXXX  ",
        "        "
    ),
    (
        " XXXXX  ",
        "XX  XXX ",
        "X    XX ",
        "XX XXXX ",
        " XXX XX ",
        "    XX  ",
        " XXXX   ",
        "        "
    ),
    (
        "        ",
        "        ",
        "   XX   ",
        "   XX   ",
        "        ",
        "   XX   ",
        "   XX   ",
        "        "
    ),
)

def draw_letter(char, x, y):
    offset = 10
    if char.isdigit():
        offset = int(char)

    dy = 0
    for row in digits[offset][::-1]:
        dx = 0
        for ch in row:
            block_id = block.AIR.id
            if ch == 'X':
                block_id = block.DIAMOND_BLOCK.id

            mc.setBlock(x + dx, y + dy, z, block_id)
            dx += 1
        dy += 1
            
        
        

while True:
    # aktualny cas
    now = datetime.now()
    text = now.strftime("%H:%M:%S")

    # vykresli!
    dx = 0
    for char in text:
        draw_letter(char, x + dx + 1, y + 1)
        dx += 8
        
    # schrupni
    sleep(1)
