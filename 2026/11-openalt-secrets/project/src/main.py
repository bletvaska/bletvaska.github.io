import json
from crypto import encrypt, decrypt

SETTINGS_FILE = '/data/settings.json'

# content of settings
settings = {
    "ssid": "OpenAlt 2026",
    "password": encrypt("Linux.Rocks!"),
}

# write settings
with open(SETTINGS_FILE, 'w') as file:
    json.dump(settings, file)

# read settings and decrypt password
with open(SETTINGS_FILE, 'r') as file:
    settings = json.load(file)

print(decrypt(settings['password']))