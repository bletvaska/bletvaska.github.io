class OpenWeatherMap:
    query = 'kosice'
    units = 'metric'
    appid = '08f5d8fd385c443eeff6608c643e0bc5'


class Wifi:
    networks = {
        'IoTLab': 'hello.world',
        'oliver.at.home': 'Indiana.Jones',
        'chalupka': 'u.nas.doma'
    }


class AdafruitIO:
    username = "bletvaska"
    key = "9e2d7e22555b4b1482f652a2d8113006"
    group = 'weather'
    feeds = ['temp', 'humidity', 'pressure']
    mqtt_broker = 'io.adafruit.com'
