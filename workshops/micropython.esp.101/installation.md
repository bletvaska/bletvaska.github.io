---
layout: default
title: Installation
duration: 120
---

## Potrebný softvér

Na workshope budeme pracovať v editore [Mu](https://codewith.mu). Samozrejme môžete použiť akýkoľvek iný editor, ktorý vie s mikrokontrolérom _ESP32_ pracovať.

Editor stiahnite z [domovskej stránky](https://codewith.mu/) z časti [Downloads](https://codewith.mu/en/download)

Tu však pozor! Stiahnite si **nie stabilnú** verziu, ale **alfa verziu**, pretože:
    * podporuje _ESP32_ (stabilná verzia ju nepodporuje), a teda nebudete môcť pracovať
    * hovorí po slovensky
    * obsahuje aj iné mocné veci

Ak ste používatelia _OS Linux_, tak stabilnú verziu potrebujete stiahnuť ručne zo stránky porjektu na [GitHub](https://github.com/mu-editor/mu)-e. Okrem toho sa uistite, že ste v skupine `dialout`


### Windowsaci

* používatelia windowsu si musia stiahnuť ovládač pre _CP210x USB to UART Bridge_
  * [download drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)


## Inštalácia firmvéru

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




## Links

* [ESP32 DevKit ESP32-WROOM GPIO Pinout](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)
* [ESP32 Datasheet](files/esp32-wroom-32_datasheet_en.pdf)
