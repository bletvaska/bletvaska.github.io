---
title: Model
courseid: fastapi
order: 205
layout: lecture
description: |
    co je to model, pydantic, response model
---

## Co je to model?


## Balik Pydantic

balik `pydantic` najprv nainstalujeme:

```bash
$ poetry add pydantic
```

a pre lepsiu pracu si nainstalujeme aj plugin pre pycharm, aby isiel pydantic. otvorime nastavenia cez `File` > `Settings` > `Plugins` a nechame vyhladat a nainstalovat plugin s nazvom `Pydantic`


## Model pre subor

pre inspiraciu toho, ako bude vyzerat model pre subor, sa mozeme pozriet na sluzbu [file.io](https://www.file.io/developers).

Modely budeme ukladat do balika s nazvom `models`, ktory vytvorime v korenovom priecinku projektu. nasledne model pre subor vytvorime v module `file_details.py`. jeho kod bude vyzerat nasledovne:


```python
from datetime import datetime

from pydantic import BaseModel


class FileDetails(BaseModel):
    # id: int
    slug: str = None
    filename: str
    downloads = 0
    max_downloads = 1
    size: int
    mime_type: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    # expires: datetime # od uploadu +24 hodin
```


## Otestovanie vytvoreneho modelu

skusit vytvorit subor

```python
from fishare.models.file_details import FileDetails

file = FileDetails(filename='fishare.exe', size=1024, mime_type='text/plain')
```


## Validator

### Validatacia clenskej premennej `mime_type`

mozeme overit, ci mime type obsahuje znak `'/'`:

```python
@validator('mime_type')
def mime_type_must_contain_slash(cls, v):
    if '/' not in v:
        raise ValueError('must contain "/"')
    else:
        return v.lower()
```

vyskusat:

```python
>>> from fishare.models.file import File

>>> file = File(filename='fishare.exe', size=1024, mime_type='textPLAIN')
```


### Validatacia clenskej premennej `created_at`

validatory ale vieme pouzit aj na post inicializaciu clenskych premennych. v nasom pripade je to clenska premenna `created_at`, ktoru chceme nastavit v dobe vytvorenia na datum a cas vytvorenia objektu. takze vytvorime nasledovny validator:

```python
@validator('created_at')
def set_created_now(cls, v):
    print('>> validating created_at')
    return datetime.now()
```

ked sa ale pokusime vytvorit subor, clenska premenna `created_at` bude mat stale hodnotu `None` a nevypise sa ani pomocna hlaska. to znamena, ze tento validator nebol vobec zavolany.

to je sposobene tym, ze validator sa vola len vtedy, ak je potrebne overit zadanu hodnotu - nesmie byt prazdny (`None`). aby sme zabezpecili toto spravanie a teda spustanie validatora vzdy aj v pripade, ze je hodnota premennej prazdna, pridame validatoru parameter `always`. ten zabezpeci, ze sa bude validator spustat aj vtedy, ak nie je poskytnuta hodnota pri vytvarani objektu.

upravime teda kod validatora takto:

```python
@validator('created_at', always=True)
def set_created_now(cls, v):
    print('>> validating created_at')
    return datetime.now()
```

vyskusat:

```python
>>> from fishare.models.file import File

>>> file = File(filename='fishare.exe', size=1024, mime_type='text/plain')

>>> file
File(slug=None, filename='fishare.exe', size=1024, mime_type='text/plain',
    created_at=datetime.datetime(2022, 4, 6, 10, 19, 56, 644201),
    updated_at=None, downloads=0, max_downloads=1)
```

Okrem volby `always` je mozne pouzit aj dalsie volby, napr.:

* `pre` - validator sa bude volat pred inymi validatormi


## Validator pre `slug`

```python
@validator('slug', always=True)
def set_secret_slug(cls, v):
    return secrets.token_urlsafe(5)
```


## Vytvorit jednoduchu implementaciu pre `/files/`

najprv si pripravime zoznam niekolkych suborov:

```python
files = [
    File(filename='jano.jpg', size=1234, mime_type='image/jpeg'),
    File(filename='juro.jpg', size=21234, mime_type='image/jpeg'),
    File(filename='main.py', size=234, mime_type='plain/text'),
    File(filename='pesnicka.mp3', size=12000000, mime_type='audio/mp3'),
]
```

vratit ho cely nie je problem:

```python
@router.get("/files/")
def get_list_of_files():
    return files
```
