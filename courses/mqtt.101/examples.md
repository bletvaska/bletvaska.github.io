---
title: MQTT Examples
layout: default
---

# {{ page.title }}


## Paho MQTT Hello world

* vytvorenie _MQTT_ klienta, jeho pripojenie
* odoslanie (_publish_) správy _"hello world"_ do témy _"general"_

```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', port=1883)

client.publish('general', 'hello world')
```


## Paho MQTT Subscribing to Topic

```python
import paho.mqtt.client as mqtt
from time import sleep

def on_message(client, userdata, message):
    text = str(message.payload.decode("utf-8"))
    print('Received message "{}" in topic "{}"'.format(
        text, message.topic))

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect('localhost', port=1883)
    client.subscribe('general')
    client.on_message = on_message

    client.loop_start()  # non blocking call
    # or client.loop_forever() - blocking call (no need the rest of code)

    while True:
        # your job goes here
        sleep(1)

    client.loop_stop()
```
