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
