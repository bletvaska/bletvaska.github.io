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

* pulzne šírková modulácia

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

## Labák: Diaľkové robotické autíčko

Autíčko bude ovládané pomocou príkazov posielaných cez MQTT na diaľku.

Zoznam materiálu:

* 2x DC motor
* 2x kolieska
* dvojkanálový h-mostík L298N
* batérie (4x1.5V alebo 1x9V) s battery box-om
* analógový joystick
* 2x ESP32
* buď originálny podvozok pre autíčko alebo kus kartónu
* lepiaca pištoľ
* lepiace pásky

### Autíčko

![Rozloženie pinov na L298N](images/l298n-pinout.png)

![Zapojenie jedného motora](images/esp32-with.l298n.png)

```python
from machine import Pin, PWM
from umqtt.robust import MQTTClient


class DCMotor:
    # the min_duty and max_duty are defined for 15000Hz frequency
    # you can pass as arguments
    def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

    # speed value can be between 0 and 100
    def forward(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)

    def stop(self):
        self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(
                self.min_duty
                + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1))
            )

        return duty_cycle

motor1 = DCMotor(pin1=Pin(12), pin2=Pin(14), enable_pin=PWM(Pin(13)))
motor2 = DCMotor(pin1=Pin(15), pin2=Pin(16), enable_pin=PWM(Pin(17)))

def on_message(topic, message):
    topic = topic.decode("utf-8")
    message = message.decode("utf-8")

    print('Message "{}" received in topic "{}"'.format(topic, message))

    if message == 'dopredu':
        motor1.forward(50)
        motor2.forward(50)
    elif message == 'stop':
        motor1.stop()
        motor2.stop()
    elif message == 'dolava':
        motor1.forward(50)
        motor2.stop()
    elif message == 'doprava':
        motor1.stop()
        motor2.forward(50)


client = MQTTClient("mirek-car", "mqtt.kpi.fei.tuke.sk", 80)
client.set_callback(on_message)

client.connect()
client.subscribe("iotlab/car/mirek")
print("Waiting for message...")

while True:
    client.wait_msg()  # blocking call

client.disconnect()
```

### Diaľkový ovládač

![Rozloženie pinov na joysticku](images/joystick-pinout.png)

```python
from machine import Pin, ADC
from time import sleep
from umqtt.robust import MQTTClient

TOPIC = 'iotlab/car/mirek'
client = MQTTClient('mirek-joystick', 'mqtt.kpi.fei.tuke.sk', 80)

dx = ADC(Pin(32))
dx.atten(ADC.ATTN_11DB)

dy = ADC(Pin(33))
dy.atten(ADC.ATTN_11DB)

button = Pin(25, Pin.IN, Pin.PULL_UP)

while True:
    if dy.read() == 0:
        client.connect()
        client.publish(TOPIC, 'dopredu')
        client.disconnect()
    elif dy.read() == 4095:
        client.connect()
        client.publish(TOPIC, 'stop')
        client.disconnect()

    if dx.read() == 0:
        client.connect()
        client.publish(TOPIC, 'dolava')
        client.disconnect()
    elif dx.read() == 4095:
        client.connect()
        client.publish(TOPIC, 'doprava')
        client.disconnect()

    print("dy: {} dx: {} button: {}".format(dy.read(), dx.read(), button.value()))
    sleep(0.5)
```

## Links

* [PWM (pulse width modulation)](https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation) - na ESP32
* [ESP32 with DC Motor and L298N Motor Driver – Control Speed and Direction](https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/)
* [Interface L298N DC Motor Driver Module with Arduino](https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/)
* [How 2-Axis Joystick Works & Interface with Arduino + Processing](https://lastminuteengineers.com/joystick-interfacing-arduino-processing/)