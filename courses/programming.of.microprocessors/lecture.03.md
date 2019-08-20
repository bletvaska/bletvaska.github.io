---
title: Analógové vstupy a výstupy
layout: layout
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

* Na prevod analógového signálu na digitálny potrebujeme mať k dispozícii analógovo-digitálny prevodník (označovaný aj ako A/D prevodník). Jeho úlohou je odmerať veľkosť vstupného napätia (alebo prúdu) a previesť ho na číslo zodpovedajúce jeho veľkosti.

* A/D prevodníky sa veľmi často používajú v zariadeniach, ktoré merajú napätie alebo prúd. Rovnako sa používa v zariadeniach, ktoré merajú inú fyzikálnu veličinu a tú prevádzajú na elektrickú (senzory), ako napr. teplota, tlak, svetlo a pod.

* Prevodník je charakteristický svojim **rozlíšením**. Rozlíšenie prevodníku je číslo, ktoré je dané počtom rozlíšiteľných úrovní analógového signálu. Udáva sa v bitoch. Ak by bol prevodník napr. 3 bitový, vedel by dokopy rozlíšiť 8 úrovní vstupného analógového signálu (pretože _2^3 = 8_)

* Proces prevodu analógového signálu na digitálny sa volá **vzorkovanie** (sampling). V pravidelných intervaloch daných vzorkovacou frekvenciou dochádza k odčítaniu hodnoty vstupnej veličiny.

### Mikrokontrolér Arduino

* Mikrokontrolér _Arduino_ obsahuje 10 bitový prevodník (môže nadobúdať hodnoty v rozsahu od _0_ po _1023_). Jeden “dielik” teda zodpovedá úrovni približne _4.88mV_ (_5V/1024_). Ak teda odčítame z analógového vstupu hodotu _567_, tak je napätie na vstupe približne _2.77V_.

* Tento prevodník obsahuje _6_ kanálov, čomu zodpovedajú vstupy _A0_ až _A5_, nazývané tiež ako **analógové vstupy** (iné verzie dosiek Arduino môžu mať iný počet kanálov). Analógové vstupy však je možné rovnako použiť ako štandardné digitálne vstupy alebo výstupy.

* Na odčítanie analógovej hodnoty pomocou mikrokontroléra Arduino používame funkciu `analogRead()`, ktorá vráti celé číslo v rozsahu _0_ - _1023_. Jej parametrom je číslo analógového portu, ktorý chceme odčítať. Je možné priamo využiť konštanty, takže miesto písania samotného čísla je možné písať A0 až A5. Teda použiť identické označenie, aké je priamo na doske.


### Mikrokontrolér ESP32

* Mikrokontrolér _ESP32_ obsahuje _2_ _12_ bitové prevodníky (môže nadobúdať hodnoty v rozsrahu od _0_ po _4095_). Jeden “dielik” teda zodpovedá úrovni približne _0.81mV_ (_3.3V/4096_). Ak teda odčítame z analógového vstupu hodotu _567_, tak je napätie na vstupe približne _0.46V_.

* Jeden z týchto prevodníkov je možné používať za veľmi špecifických podmienok. Preto je prakticky možné použiť len piny _32_ až _39_.

* Ukážka:
    ```python
    from machine import ADC

    adc = ADC(Pin(32))          # create ADC object on ADC pin
    adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v
    ```

* Pri práci je však potrebné zvážiť nastavenie dvoch hodnôt - **útlm** a **šírku**.


## Labáky


### Foto rezistor

* do série s fotorezistorom pridať ešte _10k_ odpor
* merať medzi oboma odpormi

```python
from time import sleep
from machine import ADC, Pin

sensor = ADC(Pin(32))
sensor.atten(ADC.ATTN_11DB)
while True:
    print(sensor.read())
    sleep(1)
```


### Meranie výšky hladiny s klincami

* vymeniť fotorezistor za dva klince
* pre zvýšenie citlivosti pridať ešte jeden _10k_ odpor do série


### Meranie vlhkosti zeminy v kvetináči s klincami

* rovnaký spôsob sa dá využiť aj na meranie vlhkosti v kvetináči
    * odpor sa znižuje zvyšovaním vlhkosti
* klince sú jednoduchou náhradou za podobné senzory
    * water sensor
    * moisture sensor


### Meranie baterky

* pre potreby merania monočlánkov o veľkosti _1.5V_ je treba upraviť útlm na hodnotu `ADC.ATTN_6DB` (max. _2V_)
* baterku stačí zapojiť priamo medzi zem a analógový pin

```python
from time import sleep
from machine import ADC, Pin, I2C
from esp8266_i2c_lcd import I2cLcd

# nastaveine AD prevodnika
sensor = ADC(Pin(32))
sensor.atten(ADC.ATTN_6DB)

# nastavenie I2C zbernice
i2c = I2C(scl=Pin(22), sda=Pin(21))
lcd = I2cLcd(i2c, 39, 2, 16)

lcd.putstr('Merac bateriek')
sleep(3)

while True:
    lcd.clear()
    value = sensor.read() / 4096 * 2
    lcd.putstr('{:.3f}V'.format(value))
    sleep(1)
```

### Sound Sensor

* má 4 piny:
    * `GND` - zem
    * `+` - napájanie
    * `A0` - pripojenie na analógový pin, tu je možné odčítať hodnotu hluku/zvuku
    * `D0` - pripojenie na digitálny pin, bude na ňom možné odčítať logickú 1, ak je hodnota hluku vyššia ako maximum (treshold), ináč vráti logickú 0, hodnotu treshold-u je možné nastaviť pomocou potenciometra
