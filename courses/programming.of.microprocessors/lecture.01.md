---
title: Programovateľné mikroprocesorové stavebnice
layout: layout
order: 1
duration: 240
---

## Goals

- Základy práce s programovateľnými mikroprocesorovými stavebnicami
- Mikroprocesorové stavebnice (prehľad, porovnanie, elektronické prvky)
- Softvérové vybavenie (vývojové prostredie, simulátor, základná štruktúra programu)


## Základná terminológia

* čo je to mikroprocesor? čo je to mikrokontrolér? aký je medzi nimi rozdiel?
    * vytvoriť aktivitu na tabuli, zapojiť do nich všetkých účastníkov a pýtať sa
    * zapisovať vlastnosti jedného aj druhého

    | mikroprocesor | mikrokontrolér |
    |---------------|----------------|
    | je zariadenie na všeobecné použitie | špecializované zariadenie |
    | | označuje sa ako jednočipový počítač |
    | neobsahuje I/O porty, pamäť, časovače a pod. | obsahuje RAM, ROM, sériové a pralelné rozhranie, časovače, ... všetko na jednom čipe |
    | používajú sa ako CPU v mikropočítačoch | používajú sa v jednoduchých/jednoúčelových zariadeniach |
    | jeho dizajn/návrh je komplexný | jeho dizajn/návrh je jednoduchý |
    | je drahý (desiatky/stovky Eur) | je lacný (jednotky Eur) |
    | energeticky náročný (desiatky watov) | energeticky nenáročný (jednotky Watov) |
    | majú [Von Neumannovskú architektúru](https://en.wikipedia.org/wiki/Von_Neumann_architecture) | majú [Harvardskú architektúru](https://en.wikipedia.org/wiki/Harvard_architecture) |
    | vysoká rýchlosť (GHz) | malá rýchlosť (MHz) |
    | Raspberry Pi | Arduino, ESP32, micro:bit |


## Prehľad populárnych riešení

* Arduino UNO / ATmega 328P
* ESP32
* Raspberry Pi / Raspberry Pi Zero WH

### Porovnanie riešení

| RPi Zero W | Arduino Uno | ESP32 |
|------|------|--------|
| ARM BCM 2835 | AVR ATmega328P | Tensilica Xtensa LX6 |
| 32b | 8b | 32b |
| 1 core | 1 core | 2 cores |
| 1 GHz | 20 MHz | 240 MHz |
| 512 MB RAM | 2kB RAM | 520 kB RAM |
| MicroSD | 32kB Flash | 16 MB Flash |


## ESP32 Introduction

### Inštalácia firmvéru

* pre napálenie firmvéru je treba mať nainštalovaný nástroj `esptool.py`, pomocou `pip3`:
  ```bash
  pip3 install esptool
  ```

* najprv treba stiahnuť firmvér zo stránky [micropython.org](http://micropython.org/) 
    * časť [Download](http://micropython.org/download)
    * doska [ESP32](http://micropython.org/download)
    * z časti _Standard firmware_ stiahnuť druhý v poradí (prvý je nočné zostavenie)

* pustite terminál a presuňte sa do priečinku, do ktorého ste stiahli firmvér

* vymažte obsah flash pamäte pomocou
  ```bash
  esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
  ```

* vypečte firmvér pomocou
  ```bash
  esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
  ```

* reštartnite dosku _ESP32_


### Editor Mu

#### Spustenie a zapojenie

* po spustení a zístení, že je ESP32 pripojené, sa Mu opýta, či nechete prepnúť režim do ESP32
    * prepnúť manuálne, ak sa neopýta sám

* pripojte LED diódu s _220 Ohm_-ovým odporom
    * najprv priamo na _3.3V_ a _GND_, aby ste si otestovali správnosť zapojenia
    * potom odpojiť _3.3V_ pin a pripojiť ho na _GPIO23_

#### REPL

* zapnúť REPL a ukázať, že sa veci vykonávajú priamo - postupne písať tieto riadky, na konci ktorých bude blikať
  ```python
  from machine import Pin

  led = Pin(23, Pin.OUT)

  led.on()
  led.off()
  ```

#### Blink

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


#### Súborový systém

* po kliknutí na _Súbory_ sa zobrazí obsah súborového systému na _ESP32_
    * súbor `boot.py` slúži ako nastavenie systému, prečíta sa po štarte ako prvý a to, čo sa v ňom vykoná, bude dostupné celý čas
    * ak sa tam nahrá súbor `main.py`, automaticky sa spustí po načítaní súboru `boot.py` a vykoná sa jeho obsah

* z _blink_-u spravte súbor `main.py` a pošlite ho do _ESP32_

### Windowsaci

* používatelia windowsu si musia stiahnuť ovládač pre _CP210x USB to UART Bridge_
  * https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers


## Links

* [ESP32 DevKit ESP32-WROOM GPIO Pinout](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)
* [What is the difference between a microprocessor and microcontroller?](https://www.quora.com/What-is-the-difference-between-a-microprocessor-and-microcontroller)
* [datasheet](files/esp32-wroom-32_datasheet_en.pdf)
