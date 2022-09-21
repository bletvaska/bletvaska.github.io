---
title: SQLModel
courseid: fastapi
order: 230
layout: lecture
description: |
    praca s databazou, ORM, SQLModel, SQL Alchemy
---

## Introduction

* co je to ORM
* balik SQL Alchemy - najznamejsi ORM balik pre pracu s SQL databazami v jazyku Python
* problem - FastAPI pouziva na reprezentaciu modelov Pydantic, SQL Alchemy ma vlastnu definiciu modelov, takze je potrebne spravit prepojenie medzi nimi
* riesenie - SQL Model - jeho modely su sucasne modelmi Pydanticu aj SQL Alchemy


## Installation

```bash
$ poetry add sqlmodel
```


## Model Refaktoring

upravime signaturu triedy a pridame primarny kluc:

```python
from sqlmodel import SQLModel, Field

class File(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    ...
```


## Settings Refaktoring

pridame polozku do nastaveni pre pripojenie k databaze:

```python
class Settings(BaseSettings):
    db_uri: str = 'sqlite:///database.db'

    ...
```

tym mozeme pridat lubovolnu databazu a nakonfigurovat jej pripojenie len pomocou tohto retazca


## Table Initialization

za zaciatok funkcie `main()` pridame:

* vytvorenie db enginu
* vytvorenie tabuliek podla modelov

```python
def main():
    # init db
    engine = create_engine(settings.db_uri)
    SQLModel.metadata.create_all(engine)

    ...
```


## Klient litecli

ak pouzivate Linux, mate k dispozicii priamo z prikazoveho riadku nastroj `sqlite3`, ktory reprezentuje SQLite klienta. ak ale Linux nemate, mate smolu.

ako SQLite klienta ale mozeme pouzit nastroj `litecli`, ktory je napisany v jazyku Python, takze ho vieme nainstalovat priamo z Pypi:

```bash
$ poetry add litecli
```

v korenovom priecinku, kde vznikol subor `database.db` ho mozeme spustit prikazom:

```bash
$ litecli database.db
```

zoznam tabuliek si vypiseme:

```
.tables
```


schemu tabulky `filedetails` si vypiseme:

```
.schema filedetails
```
