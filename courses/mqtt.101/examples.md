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
