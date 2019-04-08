---
title: Micropython s ESP 32 101
layout: page 
description: 
    Základy práce s micropython-om na platforme ESP32.
---

## Príprava prostredia

Ak používate _OS Windows_, tak odporúčam do systému nainštalovať balíčkovací systém [Chocolatey](https://chocolatey.org/) a pomocou neho nainštalovať _Python_ v poslednej verzii, ako aj príkazový riadok _Cmder_:

```bash
choco install -y python cmder
```

Pre vývoj budeme používať editor [Mu](https://codewith.mu/) minimálne vo verzii _1.1_. Ku _3.apr.2019_ je táto verzia dostupná len vo verzii _alpha_. Stiahnite si teda túto verziu.

## ESP32

### Vlastnosti ESP32

### Micropython na ESP32

### navod
http://docs.micropython.org/en/latest/esp32/tutorial/intro.html

#### instalacia balikov
```bash
sudo dnf install picocom ampy esptool
```

### download
http://micropython.org/download#esp32
• standard firmware
• idu sice vsetky, ale stahovat druhy v zozname (prvy je night build)
• nachadzaju sa tam aj prikazy, ktore treba zadat na vymazanie flash pamate, ako aj vypecenie firmware-u

### vymazat flash
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```



### vypecenie firmwaru
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
```



### po instalacii treba vypnut wifi, pretoze esp-cko sa by default zapne do rezimu access point
```bash
sudo dnf install magic-wormhole
wormhole receive 8-unicorn-repay
ampy -p /dev/ttyUSB0 run upy-nowifi.py
```






