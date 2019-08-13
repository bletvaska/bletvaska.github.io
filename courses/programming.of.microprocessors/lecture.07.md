---
title: Komunikačné rozhrania
layout: page
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
ssid = 'IoTkurz'
password = 'pivopivo'

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
```

## MQTT


## Links

* [Micropython: Networking](https://docs.micropython.org/en/latest/esp32/quickref.html#networking)
