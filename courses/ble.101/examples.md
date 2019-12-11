---
title: BLE Examples
layout: page
---

## Installation

Budeme používať knižnicu [pybleno](https://github.com/Adam-Langley/pybleno), ktorá je inšpirovaná _JavaScript_-ovou knižnicou [bleno](https://github.com/noble/bleno).

```bash
pip3 install pybleno
```


## Getting Started

* úvod spravím v programe `ipython`

* začneme importovaním
    ```python
    >>> import pybleno
    ```

* vytvoríme inštanciu triedy `Bleno`
    ```python
    >>> bleno = pybleno.Bleno()
    ```

* objekt `bleno` má stav. ten môžeme skontrolovať zobrazením obsahu členskej premennej `.state`
    ```python
    >>> bleno.state
    unknown
    ```

* stav sa zmení, akonáhle sa bleno štartne zavolaním funkcie `start()`
    ```python
    >>> bleno.start()
    >>> bleno.state
    poweredOn
    ```

* v tomto momente ešte náš program nič nevysiela. advertising začneme zavolaním metódy `startAdvertising()`. tá však môže byť zavolaná až vtedy, keď je bleno v stave `poweredOn`.
    ```python
    >>> bleno.startAdvertising('BLE Device')
    ```

* stav je možné skontrolovať napr. pomocou aplikácie _nRF Connect_ alebo z príkazového riadku nástrojom `bluetoothctl`
    ```bash
    $ bluetoothctl
    scan on
    devices
    ```

