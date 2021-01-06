from neopixel import NeoPixel
from machine import Pin
from random import randint
from time import sleep_ms
from umqtt.robust import MQTTClient
from settings import WIFI_NETWORKS
from helper import do_connect

def clear(pixels):
    #while True:
        for i in range(pixels.n):
            pixels[i] = (0, 0, 0)
        pixels.write()
        #yield
    
def set_color(pixels, r, g, b):
    while True:
        for i in range(pixels.n):
            pixels[i] = (g, r, b)
        pixels.write()
        yield

def set_random_colors(pixels):
    while True:
        for i in range(pixels.n):
            pixels[i] = (randint(0, 255), randint(0, 255), randint(0, 255))
        pixels.write()
        sleep_ms(50)
        yield
    
def cycle(pixels, r, g, b, wait):
    clear(pixels)
    
    while True:
        for i in range(pixels.n):
            pixels[i] = (g, r, b)
            pixels.write()
            sleep_ms(wait)
            yield
            pixels[i] = (0, 0, 0)
        else:
            pixels.write()

def bounce(pixels, r, g, b, wait):
    set_color(pixels, r, g, b)
    
    while True:        
        for i in range(pixels.n):
            pixels[i] = (0, 0, 0)
            pixels.write()
            sleep_ms(wait)
            yield
            pixels[i] = (g, r, b)
        else:
            pixels.write()
            
        for i in range(pixels.n - 1, 0, -1):
            pixels[i] = (0, 0, 0)
            pixels.write()
            sleep_ms(wait)
            yield
            pixels[i] = (g, r, b)
        else:
            pixels.write()

    
np = NeoPixel(Pin(12), 50)



def on_message(topic, message):
    global animation
    
    topic = topic.decode('utf-8')
    message = message.decode('utf-8')
    print('>> Message received: {}: {}'.format(topic, message))
    
    if message == 'bounce':
        animation = bounce(np, 255, 0, 0, 50)
        
    elif message == 'clear':
        animation = clear(np)
        
    elif message == 'cycle':
        animation = cycle(np, 0, 255, 0, 75)
        
    elif message == 'set color':
        animation = set_color(np, 0, 0, 255)
        
    elif message == 'random':
        animation = set_random_colors(np)
        
    else:
        print('>> Error: unknown effect {}!'.format(message))


# connect to WiFi
do_connect(WIFI_NETWORKS)

# connect to MQTT broker
client = MQTTClient('mirekove-esp32', 'broker.hivemq.com', 1883)
client.set_callback(on_message)
client.connect()
client.subscribe('iotlab/things/stromcek')

global animation
animation = cycle(np, 255, 0, 0, 50)

print('>> waiting for message...')
while True:
    client.check_msg()
    next(animation)

