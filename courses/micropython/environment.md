---
title: Prepare Your Environment
layout: page
---

## Technology Overview

* webrepl - https://micropython.org/webrepl/
* rshell - pip3 install rshell

## Príprava prostredia

Ak používate _OS Windows_, tak odporúčam do systému nainštalovať balíčkovací systém [Chocolatey](https://chocolatey.org/) a pomocou neho nainštalovať _Python_ v poslednej verzii, ako aj príkazový riadok _Cmder_:

```bash
choco install -y python cmder
```

Pre vývoj budeme používať editor [Mu](https://codewith.mu/) minimálne vo verzii _1.1_. Ku _3.apr.2019_ je táto verzia dostupná len vo verzii _alpha_. Stiahnite si teda túto verziu.

## ESP32

### Vlastnosti ESP32

### Micropython na ESP32

### Inštalácia Micropython-u na ESP32

http://docs.micropython.org/en/latest/esp32/tutorial/intro.html

#### Instalacia balikov

```bash
sudo dnf install picocom ampy esptool
```

* `picocom` -
* `ampy` -
* `esptool` -

### Stiahnutie obrazu

* zo stránky projektu Micropython-u je potrebné stiahnuť obraz pre ESP32. to je možné stiahnuť zo stránky [downloads](http://micropython.org/download#esp32)
* zo stránky stiahnuť _Standard firmware_
  * idu sice vsetky obrazy, ale stahovat druhý v zozname, resp. ten, ktorý má najdlhší názov a má dnešný dátum (night build)
* poznámka: nachadzaju sa tam aj prikazy, ktore treba zadat na vymazanie flash pamate, ako aj vypecenie firmware-u

### Vymazať flash pamäť

* pred vypečením firmvéru je potrebné zmazať flash pamäť:

    ```bash
    esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
    ```

### Vypecenie firmwaru

* následne vypečieme firmvér

    ```bash
    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
    ```

### Tip po inštalácii

* po instalacii treba vypnut wifi, pretoze esp-cko sa by default zapne do rezimu access point

    ```bash
    sudo dnf install magic-wormhole
    wormhole receive 8-unicorn-repay
    ampy -p /dev/ttyUSB0 run upy-nowifi.py
    ```

## RSHELL

* rshell je

* pripojiť sa je možné pomocou

  ```bash
  rshell -p /dev/ttyUSB0
  ```

* otázkou je voľba `--buffer-size=30`

## Additional Links

* [Code with Mu](https://codewith.mu/)
