---
title: Node-RED
layout: default
---

# {{ page.title }}

## Inštalácia

* na RPi je predinštalovaný
* ináč:

  ```bash
  $ apt install npm
  $ npm install node-red
  ```

## FRED

Ak nemáte možnosť nainštalovať si Node-RED lokálne, môžete využiť službu [FRED](https://fred.sensetecnic.com).


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

    [http://api.openweathermap.org/data/2.5/weather?units=metric&q=kosice,skY&appid=08f5d8fd385c443eeff6608c643e0bc5](http://api.openweathermap.org/data/2.5/weather?units=metric&q=kosice,skY&appid=08f5d8fd385c443eeff6608c643e0bc5)
