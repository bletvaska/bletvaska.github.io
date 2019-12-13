---
title: BLE Examples
layout: page
---

## nRF Connect

* nainštalovať do svojho mobilného telefónu aplikáciu _nRF Connect_.

## Micro:bit and BLE


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

## iBeacon Example

```python
from time import sleep
from pybleno import Bleno

UUID = 'e2c56db5dffb48d2b060d0f5a71096e0'
MAJOR = 1   # 0x0000 - 0xffff
MINOR = 2   # 0x0000 - 0xffff
TX_POWER = -59 # -128 - 127

bleno = Bleno()
bleno.start()
sleep(3)
bleno.startAdvertisingIBeacon(UUID, MINOR, MAJOR, TX_POWER)
```


## Start advertising with EIR data 


```python
from time import sleep
from array import array
from pybleno import Bleno

scanData = array('B', [1, 2, 3])  # maximum 31 bytes
advertisementData = array('B', [10, 11, 12])    # maximum 31 bytes

bleno = Bleno()
bleno.start()
sleep(3)
bleno.startAdvertisingWithEIRData(advertisementData, scanData)
```


## Links

* [USING BLE DEVICES WITH A RASPBERRY PI](https://www.argenox.com/library/bluetooth-low-energy/using-raspberry-pi-ble/)
