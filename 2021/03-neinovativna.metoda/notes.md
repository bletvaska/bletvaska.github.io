---
title: Space Invaders Talk
layout: page
---

## Introduction

* Programovať budem v jedoduchom editore jazyka _Python_ s názvom [Mu](), ktoré má osobitný režim pre tvorbu aplikácií s knižnicou _Pygame Zero_

## Application Window

* Začnem tým, že vytvorím prázdny súbor, ktorý uložím pod názvom `invaders.py` a spustím ho.

* Aj napriek tomu, že je súbor prázdny, tak sa okno vytvorilo s predvolenými vlastnosťami, a to:

  * šírka: _800 px_ 
  * výška: _600 px_
  * titulok okna: _Pygame Zero Game_

* Okno aplikácie vytvorené pomocou rámca _Pygame Zero_ je možné kedykoľvek zatvoriť stlačením ikony na zavretie okna v titulku okna, stlačením klávesovej skratky `ALT+F4` alebo `CTRL+Q`.

* Každú z týchto troch vlastností okna viem nastaviť zvlášť pomocou príslušných globálnych premenných. Pomocou premennej `TITLE` viem nastaviť titulok okna:

  ```python
  TITLE = 'Space Invaders'
  ```

  Pomocou premenej `HEIGHT` viem nastaviť výšku okna a pomocou premennej `WIDTH` viem zasa nastaviť šírku okna:

  ```python
  WIDTH = 640
  HEIGHT = 480
  ```

* Po spustení takto upraveného kódu sa zobrazí okno s rozmerom `640x480` a titulkom `Space Invaders`.

## Herná slučka

Vo všeobecnosti vyzerá herná slučka takto:

![Herná slučka](http://gameprogrammingpatterns.com/images/game-loop-simple.png)

_Process Input_ bude zodpovedný za načítanie vstupu od používateľa, resp. hráča. Napr. aké klávesy boli stlačené na klávesnici alebo na hernom ovládači, poprípade kde klikol používateľ myšou.

Časť _Update Game_ je zodpovedná za aktualizáciu stavu hry vzhľadom na stlačené klávesy. Rovnako tak dôjde k aktualizácii všetkých aktérov, ktorí sa v hre nachádzajú a potrebujú byť aktualizovaní. Napr. pohyb nepriateľov smerom k hráčovi, resp. aktualizácia hráčovej polohy v hre.

Časť _Render_ zasa zabezpečí vykreslenie všetkých aktérov, pozadia a popredia na obrazovku. 

V knižnici _PyGame Zero_ je táto herná slučka zastúpená dvoma funkciami:

* `update()`
* `draw()`

Nemáme však funkciu, ktorá by zodpovedala obdĺžniku `INPUT`. Vyhodnotenie používateľského vstupu sa totiž zvykne ošetrovať priamo v metóde `update()`. Tento prístup zvolíme aj my.

Táto slučka sa vykonáva neustále, pokiaľ sa hra hrá. Aby sme túto skutočnosť demonštrovali, upravím kód programu tak, že v telách funkcií `update()` a `draw()` nechám na obrazovku vypisovať len jednoduchý text, pomocou ktorého budem vedieť identifikovať, ktorá funkcia bola spustená:

```python
TITLE = 'Space Invaders'
HEIGHT = 480
WIDTH = 640

def update():
	print('update')

def draw():
	print('draw')
```

Po spustení sa zobrazí okno a v konzole budeme vidieť striedavo vypisovať dva riadky: `update` a `render`.

## Actor

* čo je to
* kvíz - koľko aktérov vidíš na obrazovke?
* základné vlastnosti
  * obrázok
  * pozícia x a y (pre fajnšmekrov .pos)
* umiestnenie na pozíciu 0, 0
* rozmer invadera - 103x84

## Moving Actor

* preletieť invaderom zľava doprava
  * vyčistenie obrazovky cez `screen.clear()`
* kde zmizol?
* otočiť ho naspäť
  * najprv odpočítam  a bude pendlovať na okraji
  * objavíme deltu v x-ovej osi, ktorá bude hovoriť, ktorým smerom alien pôjde
* aby invader prešiel celou obrazovkou
  * posunieme ho o polovicu dolu, keď narazí na okraj obrazovky
  * keď dorazí na spodok, ukončíme hru s _Game Over_

## The Invaders

* jeden invader je nuda. ako spravíme viac invaderov?
  * začneme ich číslovať podľa počtu a vytvoríme X invaderov
    * somarina. ak ich bude 100, tak 100x copy'n'pastujem?
* použijeme zoznam
  * z matematiky - množina viacerých objektov
* vytvoríme zoznam s piatimi invadermi
  * o koľko budem vykreslovať invadera vedľa invadera?
  * aktualizujeme najprv len vykreslenie (bez `update()`-u)
  * potom aktualizujeme aj funkciu `update()`
  * hra sa ukončí, keď prvý invader vyletí z obrazovky, resp. dosiahne spodok obrazovky
* čo tak dva rady invaderov?
  * pridáme len riadok navyše - cyklus v cykle


## Additinal Links

* [Welcome to Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) - domovská stránka knižnice
* [Welcome to Pygame Zero SK](https://pgzero-slovak.readthedocs.io/sk/latest/) - slovenský preklad knižnice
* [Mu]() - domovská stránka editora _Mu_