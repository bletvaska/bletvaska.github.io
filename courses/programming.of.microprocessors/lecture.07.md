---
title: Komunikačné rozhrania
layout: default
order: 4
duration: 240
outline:
- Komunikácia s okolím
- Komunikácia s počítačom a ďalšími jednotkami (sériová linka, Bluetooth, wifi, IR a iné)
- Komunikácia na internete, Internet vecí

---


## Networking

* podpora Wifi

```python
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect('essid', 'password') # connect to an AP
wlan.config('mac')      # get the interface's MAC adddress
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='ESP-AP') # set the ESSID of the access point
ap.active(True)         # activate the interface
```

* odporúčanie priamo z Micropython-u

```python
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('essid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
```

* konfigurácia do `boot.py` spolu s funkciou, resp. s inicializáciou siete

```python
_ssid = 'IoTkurz'
_password = 'pivopivo'

def do_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect(_ssid, _password)
```

## MQTT

* Micropython pre ESP32 obsahuje priamu podporu pre MQTT - balík `umqtt`

* [prezentácia o MQTT](http://bit.ly/2wKbheb)


### Publikovanie správ do MQTT

```python
from umqtt.robust import MQTTClient

# connecting to broker
client = MQTTClient('client-id', 'broker-ip', port)

# publishing message
client.connect()
client.publish('messages', 'hello world')
client.disconnect()
```


### Prihlásenie sa na odber správ z MQTT

```python
from umqtt.robust import MQTTClient

def on_message(topic, message):
    print('Message "{}" received in topic "{}"'.format(topic, message))

# connecting to broker
client = MQTTClient('client-id', 'broker-ip', port)
client.set_callback(on_message)

client.connect()
client.subscribe('topic')
print('Waiting for message...')
client.wait_msg()  # blocking call
client.disconnect()
```


## IBM Watson IoT

* komplexná platforma pre IoT riešenia od IBM
* my si ukážeme jednoduchosť použitia v režime [Quickstart](https://quickstart.internetofthings.ibmcloud.com/)
    * do formuláru na stránke zadáme len identifikátor nášho zariadenia (_Device ID_)
* podpora pre _IBM Watson IoT_ nie je na _ESP32_ natívna - je potrebné ju doinštalovať
    * balík sa volá `micropython-watson-iot`)
        * balíky pre _Micropython_ je možné vyhľadať cez [pypi](https://pypi.org/)
        * majú prefix `micropython-*`
    * doinštalovať niečo v Python-e je možné pomocou nástroja `pip`
    * v _Micropython_-e je možné ďalšie balíky doinštalovať tiež pomocou nástroja `pip`, ale vo forme príkazov samotného jazyka:
      ```python
      import upip
      upip.install('micropython-watson-iot')
      ```
    * balíky sa inštalujú do priečinku `lib/` priamo na _ESP32_
        * po nainštalovaní sú dostupné aj po reštarte _ESP32_
    * výhoda - je možné pripraviť kód tak, aby v prípade, že potrebné balíky neexistujú, tak sa najprv nainštalujú
* po nainštalovaní je použitie podobné, ako v prípade `MQTT`:
  ```python
  from watson_iot import Device

  device = Device(device_id='esp32-dht22',
                  device_type='my-device-type',
                  token='my-device-token')

  device.connect()
  device.publishEvent('temperature', {'degrees': 30.7, 'unit': 'C'})
  device.disconnect()
  ```


### Zoznam verejných MQTT brokerov, resp. IoT paltforiem

|---------------------------------------------+----------+------+------|
|                                             | **REST API** | **MQTT** | **pypi** |
|=============================================+==========+======+======|
| [io.adafruit.com](https://io.adafruit.com/) | [áno](https://io.adafruit.com/api/docs/#adafruit-io-http-api) | [áno](https://io.adafruit.com/api/docs/mqtt.html#adafruit-io-mqtt-api) | [`adafruit-io`](https://pypi.org/project/adafruit-io/) |
|---------------------------------------------+----------+------+------|
| [Ubidots](https://ubidots.com/)             | [áno](https://ubidots.com/docs/sw/#tag/Datasources) | [áno](https://ubidots.com/docs/hw/#mqtt-authentication) |      |
|---------------------------------------------+----------+------+------|
| [IBM Watson IoT]()                          |          |      | [`micropython-watson-iot`](https://pypi.org/project/micropython-watson-iot/) |
|---------------------------------------------+----------+------+--------------------------|
| [ThingSpeak](https://thingspeak.com/)       | [áno](https://uk.mathworks.com/help/thingspeak/rest-api.html?s_tid=CRUX_lftnav) | [áno](https://uk.mathworks.com/help/thingspeak/mqtt-api.html) |      |
|---------------------------------------------+----------+------+------|


#### io.adafruit.com

* je potrebné sa zaregistrovať, čím je možné získať username a AIO Key

* buď používať autententifikovaný prístup cez MQTT alebo ich knižnicu:
    ```bash
    pip3 install adafruit-io
    ```
    * [dokumentácia](https://adafruit-io-python-client.readthedocs.io/en/latest/index.html)

* táto knižnica má vlastné API pre prístup, ale taktiež aj vlastného MQTT klienta, čím je možné zabezpečiť aj odchytávanie udalostí z dashboard-u

* príklad použitia vlastného API [`adafruit-io`](https://adafruit-io-python-client.readthedocs.io/en/latest/quickstart.html):

    ```python
    from Adafruit_IO import Client
    aio = Client('YOUR ADAFRUIT USER', 'YOUR ADAFRUIT IO KEY')

    # Send the value 100 to a feed called 'Foo'.
    aio.send('Foo', 100)

    # Retrieve the most recent value from the feed 'Foo'.
    data = aio.receive('Foo')
    print('Received value: {0}'.format(data.value))
    ```

* príklad použitia MQTT klienta:

    ```python
    from time import sleep
    from Adafruit_IO import MQTTClient

    def on_message(client, feed_id, payload): 
        print(f'Feed {feed_id} received new value: {payload}')

    client = MQTTClient('username', 'AIO Key')
    client.on_message = on_message
    client.connect()

    client.subscribe('light')
    client.loop_background() # client.loop_blocking()

    while True:
        print('>> turning ON')
        client.publish('light', 'ON')
        sleep(5)
        print('>> turning OFF')
        client.publish('light', 'OFF')
        sleep(5)
    ```


## Links

* [Micropython: Networking](https://docs.micropython.org/en/latest/esp32/quickref.html#networking)
* [IoT Made Easy: ESP-MicroPython-MQTT-ThingSpeak](https://towardsdatascience.com/iot-made-easy-esp-micropython-mqtt-thingspeak-ce05eea27814)
* [Connect your ESP32 to Ubidots over MQTT using MicroPython](https://help.ubidots.com/en/articles/1956065-connect-your-esp32-to-ubidots-over-mqtt-using-micropython)
