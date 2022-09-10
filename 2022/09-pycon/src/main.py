from dht import DHT11 as DHT
from machine import Pin, unique_id
from umqtt.robust import MQTTClient
import ubinascii
import time

import settings


def do_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('>> Connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('>> Network config:', wlan.ifconfig())
    
    
if __name__ == '__main__':
    # connecting to wifi and MQTT
    do_connect(settings.WIFI_SSID, settings.WIFI_PASSWORD)
    client = MQTTClient(ubinascii.hexlify(unique_id()), settings.MQTT_BROKER)
    client.connect()
    
    # setting up DHT sensor
    pin = Pin(settings.PIN_DHT,
              Pin.IN)
    sensor = DHT(pin)

    # setting up LED
    led = Pin(settings.PIN_LED,
              Pin.OUT,
              Pin.PULL_DOWN)
    led.off()
    
    while True:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(temp, hum)
        
        # send data to mqtt
        client.publish(f'{settings.MQTT_TOPIC}/temp', str(temp) )
        client.publish(f'{settings.MQTT_TOPIC}/hum', str(hum) )
        
        # check if it is over 32
        if temp > 32:
            led.on()
        else:
            led.off()
            
        # sleep
        time.sleep(2)
        