---
title: Motorové obvody
layout: page
order: 4
outline:
- Riadenie motorov
- Servá
- Jednosmerné motory
- Krokové motory a ich riadenie
---


## H-mostík

* názov vznikol podľa toho, že zapojenie je v tvare písmena _H_

* Pozostáva zo štyroch prepínačov, kde sa na motor privedie napätie na základe kombinácie zapojenia dvoch z nich. Tým sa raz motor otáča vľavo alebo vpravo. Ukážka:

  ![H-mostík](images/h-bridge.gif)

* Ako prepínače sú použité tranzistory.

## Pulse-Width Modulation

### Introduction

* PWM môže byť použité na vytvorenie ilúzie, že LED dióda môže mať niekoľko úrovní jasu. Túto ilúziu získame tým, že budeme LED diódu neustále rozsvecovať a zhasínať v priebehu približne _500_ cyklov za sekundu. Jas, ktorý dosiahneme, je stanovený z množstva času, v ktorom je LED dióda zapnutá voči času, v ktorom je LED dióda vypnutá. Čím bude dlhší pracovný cyklus (dlhší čas bude PIN nastavený na hodnotu _1_ než na hodnotu _0_), tým vyšší jas bude LED dióda mať.

* V tomto prípade sa jedná o akýsi podvod pre naše oko. To totiž nie je schopné zaznamenať blikanie rýchlejšie ako _50_ cyklov za sekundu. Ak je totiž vyššie, dióda sa bude javiť ako svietiaca.

* Pozrime sa teda na to, ako taký pracovný cyklus vyzerá.
  ![Duty Cycle](images/duty.cycle.gif)

* A pozrime sa tiež na niekoľko rozličných pracovných cyklov. Čím je teda šírka pulzu nižšia, tým je aj nižší celkový výsledný výkon, resp. v našom prípade to bude úroveň jasu. Čím je naopak šírka pulzu vyššia, tým bude vyšší aj výsledný výkon, resp. úroveň jasu.
  ![Various Duty Cycles](images/duty.cycle-various.gif)

* Na _Arduino UNO_ je ako PWM piny možné využiť digitálne PIN-y _3_, _5_, _6_, _9_, _10_ a _11_. Pre úplnosť je potrebné dodať, že pre svoju činnosť PWM používa časovače mikrokontroléra _ATmega_.

* Na _ESP32_ je možné ako PWM piny využiť všetky výstupné digitálne piny. Ukážka použitia:

  ```python
  from machine import Pin, PWM

  pwm0 = PWM(Pin(0))      # create PWM object from a pin
  pwm0.freq()             # get current frequency
  pwm0.freq(1000)         # set frequency
  pwm0.duty()             # get current duty cycle
  pwm0.duty(200)          # set duty cycle
  pwm0.deinit()           # turn off PWM on the pin

  pwm2 = PWM(Pin(2), freq=20000, duty=512) # create and configure in one go
  ```


## Links

* [PWM (pulse width modulation)](https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation) - na ESP32