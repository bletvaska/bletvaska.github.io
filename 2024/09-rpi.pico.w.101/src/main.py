import json
import requests
import time
import machine

from umqtt.simple import MQTTClient


def do_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print(f'>> Connecting to network "{ssid}"...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('>> Network config:', wlan.ifconfig())


def extract_data(query: str, units: str, appid: str) -> dict:
    print('>> extract data')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={appid}&units={units}'
    response = requests.get(url)
    data = response.json()
    response.close()

    return data


def to_iso8601(ts: int) -> str:
    dt = time.gmtime(ts)
    return f'{dt[0]:04}-{dt[1]:02}-{dt[2]:02}T{dt[3]:02}:{dt[4]:02}:{dt[5]:02}Z'


def transform_data(data: dict) -> dict:
    print('>> transform data')

    return {
        'dt': to_iso8601(data['dt']),
        'lat': data['coord']['lat'],
        'lon': data['coord']['lon'],
        'metrics': {
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure']
        }
    }


def load_data_http(user: str, key: str, group: str, data: dict):
    print('>> load data over http')

    headers = {
        'X-AIO-Key': key
    }

    for feed in data['metrics']:
        url = f'https://io.adafruit.com/api/v2/{user}/feeds/{group}.{feed}/data'

        payload = {
            "lat": data['lat'],
            "lon": data['lon'],
            "value": data['metrics'][feed],
            "created_at": data['dt']
        }

        response = requests.post(url, headers=headers, json=payload)
        response.close()


def load_data_mqtt(user: str, key: str, group: str, data: dict):
    print('>> load data over mqtt')

    topic = f'{user}/groups/{group}'

    payload = {
        'feeds': {
            'temp': data['metrics']['temp'],
            'humidity': data['metrics']['humidity'],
            'pressure': data['metrics']['pressure']
        },
        'location': {
            "lat": data['lat'],
            "lon": data['lon'],
        }
    }

    client = MQTTClient('mirek.on.pico', 'io.adafruit.com', 1883, user, key)
    client.connect()
    client.publish(topic, json.dumps(payload))
    client.disconnect()


def main():
    do_connect(WIFI_SSID, WIFI_PASSWORD)
    raw_data = extract_data(OPENWEATHERMAP_QUERY, OPENWEATHERMAP_UNITS, OPENWEATHERMAP_APPID)
    data = transform_data(raw_data)
    #load_data_http(AIO_USER, AIO_KEY, AIO_GROUP, data)
    load_data_mqtt(AIO_USER, AIO_KEY, AIO_GROUP, data)

    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.disconnect()


if __name__ == '__main__':
    main()

    print(f'>> going to sleep for {INTERVAL} minutes')
    machine.deepsleep(INTERVAL * 60 * 1000)

