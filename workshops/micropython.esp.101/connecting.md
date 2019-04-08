---
title: Pripájanie k ESP32
layout: default
---
## Pripojenie ESP32 ku počítaču

* USB kábel  do ESP32 a druhý koniec do počítača

## Spustenie editora Mu

* spustíme editor _Mu_
* po spustení editor sám rozpozná, že má pripojené _ESP_ a ponúkne nám prepnúť režim editora pre mikrokontroléry _ESP_
* prepnúť do režimu _ESP_ sa môžete kedykoľvek kliknutím na ikonu _Režim_ editora (úplne vľavo)

## Spojenie z príkazového riadku

```bash
picocom -b 115200 --flow n /dev/ttyUSB0
```

pomocou ampy je mozne sa pripojit na suborovy system a nahravat tam 
subory. ak sa subor vola main.py, tak sa bude spustat automaticky po 
restartnuti esp-cka