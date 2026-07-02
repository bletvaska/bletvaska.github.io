import json
import crypto


SETTINGS_FILE = '/data/settings.py'

# content of settings
settings = {
    "ssid": "OSS Conf 2026",
    "password": crypto.encrypt("Linux.Rocks!"),
}

# write settings
with open(SETTINGS_FILE, 'w') as file:
    json.dump(settings, file)

# read settings
with open(SETTINGS_FILE, 'r') as file:
    settings = json.load(file)


print(settings)