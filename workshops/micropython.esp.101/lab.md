---
layout: default
title: ESP32 Lab
duration: 120
---

## Editor Mu

## Spustenie a zapojenie

* po spustení a zístení, že je ESP32 pripojené, sa Mu opýta, či nechete prepnúť režim do ESP32
    * prepnúť manuálne, ak sa neopýta sám

* pripojte LED diódu s _220 Ohm_-ovým odporom
    * najprv priamo na _3.3V_ a _GND_, aby ste si otestovali správnosť zapojenia
    * potom odpojiť _3.3V_ pin a pripojiť ho na _GPIO23_

## REPL

* zapnúť REPL a ukázať, že sa veci vykonávajú priamo - postupne písať tieto riadky, na konci ktorých bude blikať
  ```python
  from machine import Pin

  led = Pin(23, Pin.OUT)

  led.on()
  led.off()
  ```

## Blink

* vytvorte _Blink_ ako program
  ```python
  from machine import Pin
  from time import sleep

  led = Pin(23, Pin.OUT)

  while True:
    led.on()
    sleep(1)
    led.off()
    sleep(0.5)
  ```

* spustite program
    * ledka začne blikať
    * program sa nenahral na ESP32, ale akoby sa nakopíroval priamo do REPL-u zariadenia
    * po reštartovaní zariadenia blikanie prestane


## Links

* [ESP32 DevKit ESP32-WROOM GPIO Pinout](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)
* [ESP32 Pinout](images/esp32-pinout.png)
* [datasheet](files/esp32-wroom-32_datasheet_en.pdf)
