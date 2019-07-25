---
title: Digitálne vstupy a výstupy
layout: page
order: 2
duration: 240
outline:
- Riadenie digitálnych vstupov a výstupov
- Digitálne výstupy
- Digitálne vstupy
---

## GPIO Piny

* skratka od _General Purpose Input Output_

### ESP-WROOM-32 Pinout

[![ESP-WROOM-32 Pinout](images/esp32-pinout.jpg)](https://www.flickr.com/photos/jgustavoam/40089095211/in/photostream/)


## Digitálny výstup

```python
from machine import Pin
from time import sleep

led = Pin(32)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```


## Let's Build a Python LED Class

* odbočka - môžeme vytvárať triedy, ktoré reprezentujú príslušné senzory alebo akčné členy


## Digitálny vstup


## Lab: Indiana Jones Theme

![Indiana Jones and the Raiders of the Lost Ark](images/indiana.jones.jpg)

* kuknime si na oázu zariadení poháňaných ESP32 s kopcom digitálnych vstupov:

<iframe width="560" height="315" src="https://www.youtube.com/embed/aADExWV1bsM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* spravme zabezpečovací mechanizmus pre _Golden Idol_

* ako však zabezpečili, aby ten mechanizmus fungoval aj po tisíckach rokov?


## Linky
* [ESP32 DevKit ESP32-WROOM GPIO Pinout](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)