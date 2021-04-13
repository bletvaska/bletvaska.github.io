---
title: Node-RED
layout: default
---

# {{ page.title }}

## Inštalácia

* na RPi je Node-RED predinštalovaný, ale je v starej verzii, takže ho treba aktualizovať:

  ```bash
  $ sudo apt update
  $ sudo apt install nodered
  ```

* ak používate Raspberry Pi Desktop, tak Node-RED nainštalujete nasledovne:

  ```bash
  $ sudo apt update
  $ sudo apt install npm
  $ sudo npm install -g --unsafe-perm node-red
  ```

* ak chcete Node-RED dostať do Windows-ov, tak postupujte napríklad podľa [tohto návodu](http://www.namakanyden.sk/webinare/2020/05/21/tvorba-webovych-aplikacii-v-node-red.html)


## FRED

Ak nemáte možnosť nainštalovať si Node-RED lokálne, môžete využiť službu [FRED](https://fred.sensetecnic.com). Je potrebné sa len zaregistrovať a využiť Free Plan.


## Predstavenie prostredia

* uzly - nodes
* flow
* vlastnosti


## Prvý flow

1. pridať do flow-u uzly `inject` a `debug`

2. prepojiť ich

3. nasadiť ich


## Pocasie aka IT Akademia pocasie

1. pridať nový uzol [node-red-contrib-web-worldmap](https://flows.nodered.org/node/node-red-contrib-web-worldmap)

    * hamburgerové menu > `Manage palette`
    * záložka `Install`
    * vyhľadať `worldmap`
    * nainštalovať

2. stiahnuť počasie z 

    [http://api.openweathermap.org/data/2.5/weather?units=metric&q=kosice,sk&appid=08f5d8fd385c443eeff6608c643e0bc5](http://api.openweathermap.org/data/2.5/weather?units=metric&q=kosice,sk&appid=08f5d8fd385c443eeff6608c643e0bc5)
