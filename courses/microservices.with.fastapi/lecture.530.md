---
title: Building a Package
courseid: fastapi
order: 530
layout: lecture
description: |
    ako zostavit instalacny balik vyslednej aplikacie
---


## Vytvorenia balicka

Zadanim prikazu `poetry build` dojde k vytvoreniu priecinku `dist/`, do ktoreho sa ulozi vysledny balicek s nasou aplikaciu:

```bash
$ poetry build
```

## Nainstalovanie balicka z prikazoveho riadku

```bash
$ mkvirtualenv fishare
$ pip install ./fishare-0.2.0-py3-none-any.whl
```


## Spustenie naninstalovanej aplikacie

musime ju spustit tak, ako v IDE:


```bash
$ python -m fishare.main
```


## Vytvorenie suboru `requirements.txt`

```bash
$ poetry export
```

popripade

```bash
$ poetry export --without-hashes
```


## Vytvorenie skriptov

ak chceme spustit aplikaciu, musime v prikazovom riadku napisat:

```bash
$ python -m fishare.main:app
```

mame ale moznost vytvorit spustitelny skript, ktory to urobi za nas. upravime konfiguracny subor `pyproject.toml`:

```toml
[tool.poetry.scripts]
fishare = "fishare.main:main"
fishare_init = "fishare.helpers:populate_data"
```

a ked ho teraz nainstalujeme, budeme ho mat k dispozicii.
