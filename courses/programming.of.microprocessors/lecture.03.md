---
title: Analógové vstupy a výstupy
layout: page
order: 3
duration: 240
outline:
- Riadenie analógových vstupov a výstupov
- Analógové vstupy a výstupy
---


## Analógové piny na ESP32

* analógové piny _32_ až _39_
* má _12_ bitový A/D prevodník, ale je možné pracovať s rolišovacou schopnosťou _9_, _10_, _11_ a _12_ bitov


## Analógový vstup

```python
from machine import Pin, ADC
from time import sleep

sensor = ADC(Pin(32)

while True:)
    print(sensor.read())
    sleep(1)
```


## Sound Sensor

* má 4 piny:
    * `GND` - zem
    * `+` - napájanie
    * `A0` - pripojenie na analógový pin, tu je možné odčítať hodnotu hluku/zvuku
    * `D0` - pripojenie na digitálny pin, bude na ňom možné odčítať logickú 1, ak je hodnota hluku vyššia ako maximum (treshold), ináč vráti logickú 0, hodnotu treshold-u je možné nastaviť pomocou potenciometra
