---
title: Settings
courseid: fastapi
order: 220
layout: lecture
description: |
    nastavenia
---

## Introduction

Twelve factor app hovori, ze ten spravny sposob, ako drzat konfiguraciu aplikacie, ktora sa meni medzi jednotlivymi deploymentmi, su premenne prostredia.

```bash
$ poetry add "pydantic[dotenv]"
```

pre podporu env suborov v pycharm-e je potrebne nainstalovat rozsirujuci plugin cez dialog `File` > `Settings` > `Plugins`. je ich niekolko, takze vyber je volny. dolezita je podpora pre zvyraznovanie syntaxe.


## Model pre nastavenia

```python
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    environment = 'development'
    slug_length = 5
    port = 8000
    base_url: AnyHttpUrl = 'http://localhost:8000'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'fishare_'
```


## Getting the Settings

na ziskanie nastaveni vytvorime samostatnu funkciu v rovnakom module, v ktorom je zadefinovaná trieda. bude vyzerať takto:

```python
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.environment}")
    return settings
```


## Caching

Problém však je, že objekt s nastaveniami bude vytvorený zakaždým, keď sa funkcia zavolá, pričom by stačilo vytvoriť tento objekt len raz (konfigurácia sa za behu nebude meniť). To sa dá vyriešiť napr. implementovaním návrhového vzoru **jedináčik** (z angl. **singleton**) alebo implementovať tzv. [LRU cache strategy](https://realpython.com/lru-cache-python/) pomocou modulu `lru_cache`:


```python
from functools import lru_cache


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.environment}")
    return settings
```

Teraz sa budú nastavenia inicializovať len raz.


## Links

* [Build a URL Shortener With FastAPI and Python](https://realpython.com/build-a-python-url-shortener-with-fastapi/)
* [Caching in Python Using the LRU Cache Strategy](https://realpython.com/lru-cache-python/)

