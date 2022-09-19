---
title: Model
courseid: fastapi
order: 201
layout: lecture
description: |
    co je to model, pydantic, response model
---

## Co je to model?


## Pydantic

* treba nainstalovat plugin pre pycharm, aby isiel pydantic pekne cez `File` > `Settings` > `Plugins`


## Model pre subor

Modely budeme ukladat do balika s nazvom `models`, ktory vytvorime v korenovom priecinku projektu. nasledne model pre subor vytvorime v module `file.py`. jeho kod bude vyzerat nasledovne:


```python
from datetime import datetime

from pydantic import BaseModel


class File(BaseModel):
    # id: int
    slug: str = None
    filename: str
    downloads = 0
    max_downloads = 1
    size: int
    mime_type: str
    created_at: datetime = None
    updated_at: datetime = None
    # expires: datetime # od uploadu +24 hodin
```

skusit vytvorit subor

```python
from fishare.models.file import File

file = File(filename='fishare.exe', size=1024, mime_type='text/plain')
```


## Validator

* `always` - validator sa bude volat aj vtedy, ak nie je poskytnuta hodnota pri vytvarani objektu (`value`)
* `pre` - validator sa bude volat pred inymi validatormi

```python
@validator('created_at', pre=True, always=True)
def set_created_now(cls, value):
    return datetime.now()
```

vyskusat:

```python
>>> from fishare.models.file import File

>>> file = File(filename='fishare.exe', size=1024, mime_type='text/plain')

>>> file
File(slug=None, filename='fishare.exe', size=1024, mime_type='text/plain', created_at=datetime.datetime(2022, 4, 6, 10, 19, 56, 644201), updated_at=None, downloads=0, max_downloads=1)
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


## FileOut Model

lenze nechceme, aby koncovi pouzivatelia videli vsetky polozky. urobime si preto model, ktory budeme pouzivat na prezentovanie vysledkov:

```python
class FileOut(BaseModel):
    slug: str
    filename: str
    downloads: int
    max_downloads: int
    size: int
    mime_type: str
    url: HttpUrl = None

    @validator('url', always=True)
    def set_file_url(cls, value, values):
        return f'http://localhost:9000/{values["slug"]}'
```

no a potom mozeme vratit jeden subor:

```python
@router.head('/files/{slug}')
@router.get('/files/{slug}', response_model=FileOut)
def get_file(slug: str):
    for file in files:
        if file.slug == slug:
            return file

    return {}
```

podobne mozeme upravit aj zoznam suborov:

```python
@router.get("/files/", response_model=List[FileOut])
def get_list_of_files():
    return files
```
