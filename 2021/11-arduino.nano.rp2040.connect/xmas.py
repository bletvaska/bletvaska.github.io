import time
from neopixel import NeoPixel
from machine import Pin


def clear(pixels):
    print('>> running clear')
    for i in range(pixels.n):
        pixels[i] = (0, 0, 0)
    pixels.write()
    
    
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def rainbow_cycle(pixels, wait, once=False):
    print('>> running rainbow_cycle')
    clear(pixels)

    while True:
        for j in range(255):
            for i in range(pixels.n):
                rc_index = (i * 256 // pixels.n) + j
                pixels[i] = wheel(rc_index & 255)
            pixels.write()
            time.sleep_ms(wait)
            yield

        if once == True:
            break
        
if __name__ == '__main__':
    np = NeoPixel(Pin(4, Pin.OUT), 50)
    scenario = rainbow_cycle(np, 100)
    
    while True:
        next(scenario)