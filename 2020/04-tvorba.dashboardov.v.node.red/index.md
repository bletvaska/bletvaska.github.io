---
layout: default
title: Tvorba dashboardov v Node-Red
duration: 120
---

Prostredie IoT je charakteristické zberom obrovského množstva údajov, ktoré následne treba niekde ukladať, vizualizovať a analyzovať. V tomto webinári sa pozrieme na vizualizáciu údajov pomocou nástroja Node-Red, ktoré k nám budú v reálnom čase prichádzať ako správy cez protokol MQTT. Uvidíte, ako rýchlo a jednoducho dokážete z údajov svojich senzorov zostaviť sexi dashboard.

Pre absolvovanie webináru budete potrebovať len nainštalovaný Node-Red na vašom počítači. Inštrukcie nájdete nižšie.

## Potrebný softvér

Pre prácu budeme používať prostredie [Node-RED](https://nodered.org), ktoré je webovou aplikáciou napísanou v [Nodejs](https://nodejs.org/en/). Preto okrem samotného Node-RED budete potrebovať aj prehliadač.

Ako skúsený používateľ môžete prejsť rovno na stránku [Getting Started](https://nodered.org/docs/getting-started/), kde si nájdete spôsob inštalácie, ktorý vám vyhovuje najviac.

Ak na webinári budete pracovať na minipočítači Raspberry Pi, ste za vodou, pretože Node-RED je predinštalovaný v OS Raspbian (full) a stačí ho len spustiť.

### Inštalácia Node.js

Node-RED je aplikáciou napísanou v Node.js. Preto v rámci prvého kroku nainštalujeme do počítača práve ten. Ak ste používateľom OS Linux, na inštaláciu použite balíčkovací systém distribúcie.

Pre používateľov OS Windows existujú v príncípe dve základné možnosti:

1. stiahnite si inštalačku priamo zo stránky [nodejs.org](https://nodejs.org/) (sťahujte LTS verziu, nakoľko tá je stabilná).

2. použite na inštaláciu balíčkovací systém [Chocolatey](https://chocolatey.org), kde následne stačí v príkazovom riadku ako administrátor napísať:

    ```bash
    choco install nodejs-lts
    ```

To, či máte `nodejs` nainštalovaný správne, si overíte spustením príkazového riadku a napísaním do neho príkazu:

    ```bash
    $ node --version
    v12.10.0
    ```

Príkaz zobrazí verziu nainštalovaného `node`. Číslo verzie sa samozrejme môže líšiť od spôsobu inštalácie.

Overte tiež, či máte nainštalovaný nástroj `npm`, pomocou ktorého následne nainštalujeme Node-RED:
    ```bash
    $ npm --version
    6.14.4
    ```


### Inštalácia Node-RED

Pokiaľ máme nainštalovaný ako `node`, tak aj `npm`, inštalácia nástroja Node-RED je už veľmi jednoduchá - v príkazovom riadku napíšte:

```bash
npm install -g --unsafe-perm node-red
```


## Spustenie Node-RED

Ak používate Raspberry Pi s OS Raspbian, nájdete Node-RED priamo v menu a spustíte ho kliknutím na príslušnú položku.

Ostatní budú spúšťať Node-RED z príkazového riadku takto:

```bash
$ node-red
```

Výstup spusteného programu bude vyzerať podobne tomu môjmu:

```
14 Apr 13:11:40 - [info]

Welcome to Node-RED
===================

14 Apr 13:11:40 - [info] Node-RED version: v1.0.3
14 Apr 13:11:40 - [info] Node.js  version: v12.10.0
14 Apr 13:11:40 - [info] Linux 5.5.13-200.fc31.x86_64 x64 LE
14 Apr 13:11:40 - [info] Loading palette nodes
14 Apr 13:11:41 - [info] Dashboard version 2.7.0 started at /ui
14 Apr 13:11:41 - [info] Settings file  : /home/mirek/.node-red/settings.js
14 Apr 13:11:41 - [info] Context store  : 'default' [module=memory]
14 Apr 13:11:41 - [info] User directory : /home/mirek/.node-red
14 Apr 13:11:41 - [warn] Projects disabled : set editorTheme.projects.enabled=true to enable
14 Apr 13:11:41 - [info] Flows file     : /home/mirek/.node-red/flows_gotham.json
14 Apr 13:11:41 - [info] Server now running at http://127.0.0.1:1880/
14 Apr 13:11:41 - [warn]
```

Najpodstatnejší riadok bude tento:

```
14 Apr 13:11:41 - [info] Server now running at http://127.0.0.1:1880/
```

Ten hovorí o tom, že na uvedenej adrese a porte sa Node-RED spustil. Ak teda otvoríte prehliadač, mali by ste Node-RED vidieť.


## Links

* [Getting Started](https://nodered.org/docs/getting-started/) - This guide will help you get Node-RED installed and running in just a few minutes.

* [Running Node-RED locally](https://nodered.org/docs/getting-started/local) - Rozličné postupy pre inštaláciu Node-RED.

* [Installing Chocolatey](https://chocolatey.org/install) - Postup pre inštaláciu Chocolatey na OS Windows.


