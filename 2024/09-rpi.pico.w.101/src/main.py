from time import sleep, gmtime
from machine import Timer, unique_id, ADC, reset
import json
import urequests as requests

from umqtt.simple import MQTTClient

from settings import OpenWeatherMap, Wifi, AdafruitIO


def do_connect(networks: dict):
    try:
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        
        # connect to network
        if not wlan.isconnected():
            filtered_networks = filter(lambda net: net[0].decode('utf-8') in networks, wlan.scan())
            net = list(filtered_networks)[0]
            ssid = net[0].decode('utf-8')
            print(f'>> Connecting to network {ssid}...')
            wlan.connect(ssid, networks[ssid])
            while not wlan.isconnected():
                pass
            
        print('>> Network config:', wlan.ifconfig())
    except Exception as ex:
        print('>> No network to connect. Will reboot in 30 seconds and try again.')
        sleep(30)
        reset()
    

def enlight(func):
    def wrapper(*args, **kwargs):
        led = machine.Pin('LED', machine.Pin.OUT)
        led.on()
        func(*args, **kwargs)
        led.off()
    return wrapper


@enlight
def publish_data_over_http(timer: Timer = None):
    data = download_data()
    print('>> Publishing data over HTTP')
    
    headers = {
        'X-AIO-Key': AdafruitIO.key
    }

    for feed in AdafruitIO.feeds:
        url = f'https://io.adafruit.com/api/v2/{AdafruitIO.username}/feeds/{AdafruitIO.group}.{feed}/data'
        dt = gmtime(data['dt'])
        payload = {
            'value': data['main'][feed],
            'lat': data['coord']['lat'],
            'lon': data['coord']['lon'],
            'created_at': f'{dt[0]}-{dt[1]}-{dt[2]}T{dt[3]}:{dt[4]}:{dt[5]}Z'
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.close()


@enlight
def publish_data_over_mqtt(timer: Timer = None):
    data = download_data()
    print('>> Publishing data over MQTT')
    
    # connect to broker
    client = MQTTClient(client_id=unique_id(),
                        server=AdafruitIO.mqtt_broker,
                        user=AdafruitIO.username,
                        password=AdafruitIO.key)
    client.connect()
    
    # prepare data
    # https://io.adafruit.com/api/docs/mqtt.html#group-topics
    # mosquitto_pub -u "bletvaska" -P "9e2d7e22555b4b1482f652a2d8113006"  -h "io.adafruit.com" -t "bletvaska/feeds/weather.temperature" -m "30"
    topic = f'{AdafruitIO.username}/groups/{AdafruitIO.group}'
    
    payload = {
        "feeds": { # { key : data['main'][key] for key in AdafruitIO.feeds }
            "temp": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
        },
        "location": {
            'lat': data['coord']['lat'],
            'lon': data['coord']['lon'],
        }
    }
    
    # publish data
    client.publish(topic, json.dumps(payload))
    client.disconnect()
    
    
def download_data() -> dict:
    # download data
    print(f'>> Downloading weather forecast for {OpenWeatherMap.query}.')
    url = f'https://api.openweathermap.org/data/2.5/weather?' + \
          f'q={OpenWeatherMap.query}&units={OpenWeatherMap.units}' + \
          f'&appid={OpenWeatherMap.appid}'
    response = requests.get(url)
    
    data = response.json()
    response.close()
    
    return data


@enlight
def publish_pico_temperature(timer: Timer = None):
    print('>> Publishing Pico temperature over MQTT')
    
    # read the temperature
    sensor = ADC(4)
    conversion_factor = 3.3 / (65535)

    reading = sensor.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    
    # connect to broker
    client = MQTTClient(client_id=unique_id(),
                        server=AdafruitIO.mqtt_broker,
                        user=AdafruitIO.username,
                        password=AdafruitIO.key)
    client.connect()
    
    # prepare data
    # https://io.adafruit.com/api/docs/mqtt.html#sending-json
    # mosquitto_pub -u "bletvaska" -P "9e2d7e22555b4b1482f652a2d8113006"  -h "io.adafruit.com" -t "bletvaska/feeds/weather.temperature" -m "30"
    topic = f'{AdafruitIO.username}/feeds/pico_temp/json'
    
    payload = {
        'value': temperature
    }
    
    # publish data
    client.publish(topic, json.dumps(payload))
    client.disconnect()
    

if __name__ == '__main__':
    # connect to wifi
    do_connect(Wifi.networks)
    
    # make first publishing after startup
    publish_pico_temperature()
    publish_data_over_http()
    
    # set timers
    timer1 = Timer(period=1 * 60 * 1000, mode=Timer.PERIODIC, callback=publish_pico_temperature)
    #timer2 = Timer(period=10 * 60 * 1000, mode=Timer.PERIODIC, callback=publish_data_over_mqtt)
    timer3 = Timer(period=10 * 60 * 1000, mode=Timer.PERIODIC, callback=publish_data_over_http)

    
#     counter = 0
#     while True:
#         if counter == 0:
#             counter = 10
#             data = download_data()
#     
# #             publish_data_over_http(data)
#             publish_data_over_mqtt(data)
#         else:
#             counter -= 1
#             
#         publish_pico_temperature()
#         
#         print('>> Going to sleep...')
#         time.sleep(1 * 60)
