---
layout: default
title: Installation
duration: 120
---


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


## Editor Mu

* editor stiahnite z [domovskej stránky](https://codewith.mu/) z časti [Downloads](https://codewith.mu/en/download)

* stiahnite si **nie stabilnú** verziu, ale **alfa verziu** !!!
    * podpora pre ESP32
    * slovenčina
    * iné mocné veci

* Linuxáci - uistite sa, že ste v skupine `dialout`


### Windowsaci

* používatelia windowsu si musia stiahnuť ovládač pre _CP210x USB to UART Bridge_
  * [download drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)


## Links

* [ESP32 DevKit ESP32-WROOM GPIO Pinout](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)
* [ESP32 Datasheet](files/esp32-wroom-32_datasheet_en.pdf)
