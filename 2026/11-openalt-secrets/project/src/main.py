import json
from crypto import encrypt

SETTINGS_FILE = '/data/settings.json'

# content of settings
settings = {
    "ssid": "OpenAlt 2026",
    "password": encrypt("Linux.Rocks!"),
}

# write settings
with open(SETTINGS_FILE, 'w') as file:
    json.dump(settings, file)