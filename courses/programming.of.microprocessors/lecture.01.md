---
title: Programovateľné mikroprocesorové stavebnice
layout: page
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

* [datasheet](files/esp32-wroom-32_datasheet_en.pdf)

* používatelia windowsu si musia stiahnuť ovládač pre _CP210x USB to UART Bridge_
  * https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers


## Links

* [ESP32 DevKit ESP32-WROOM GPIO Pinout](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)
* [What is the difference between a microprocessor and microcontroller?](https://www.quora.com/What-is-the-difference-between-a-microprocessor-and-microcontroller)