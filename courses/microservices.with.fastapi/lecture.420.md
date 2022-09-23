---
title: Templating with Jinja
courseid: fastapi
order: 420
layout: lecture
description: |
    o tvorbe obsahu pomocou sablon
---

## Introduction


## Installation

```bash
$ poetry add jinja2
```


## Configuration

pripojime priecinok k endpointu `/static`. budeme ho pouzivat na staticke subory, ako JavaScript-ove skripty, kaskadne styly, obrazky a podobne:

```python
app.mount('/static',
          StaticFiles(directory='fishare/static'),
          name='static')
```

vyskusat to mozeme napriklad tak, ze si v prehliadaci alebo z prikazoveho riadku nechame zobrazit css subor, ktory sa v tom priecinku nachadza:

```bash
$ http http://localhost:8000/static/images/mountains.jpg
```


## Hlavna stranka

Vytvorime novy balik s nazvom `views`. Do tohto balika budeme ukladat pohlady, ktore budu vracat HTML stranky. vytvorime v nom novy subor s nazvom `homepage.py`. Ten zobrazi hlavnu stranku nasej aplikacie, ak k nej pristupime priamo z prehliadaca.

```python
import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates(directory='fishare/templates/')


@router.get('/')
def homepage(request: Request):
    data = {
        'request': request,
        'title': 'fishare - File Sharing for Free'
    }
    return templates.TemplateResponse('home.html', data)
```

ked otvorime prehliadac na adrese http://localhost:8000/ zobrazi sa nam hlavna stranka spolu s formularom na nahratie suboru.


## Dependency

V module `helpers.py` vytvorime funkciu, ktora nam vrati objekt typu `Jinja2Templates` a budeme ju pouzivat ako zavislost pre kazdy pohlad.

```python
@lru_cache
def get_jinja() -> Jinja2Templates:
    return Jinja2Templates(directory='fishare/templates/')
```

nasledne mozeme aktualizovat pohlad pre zobrazenie hlavnej stranky:

```python
@router.get('/')
def homepage(request: Request,
             jinja: Jinja2Templates = Depends(get_jinja)):
    data = {
        'request': request,
        'title': 'fishare - File Sharing for Free'
    }

    return jinja.TemplateResponse('home.html', data)
```


## Admin stránka

podobne zobrazime aj admin stranku, ktoru ulozime do modulu `admin.py`. ta vsak zobrazuje aj zoznam suborov v databaze, takze najprv potrebujeme subory vytiahnut z databazy (tentokrat naozaj vsetky) a potom ich posleme do sablony, aby boli "vyrenderovane".

```python
@router.get('/')
def list_of_files(request: Request,
                  jinja: Jinja2Templates = Depends(get_jinja),
                  session: Session = Depends(get_session)):
    # get data
    # SELECT * FROM files
    statement = select(FileDetails)
    files = session.exec(statement).all()

    # prepare data
    data = {
        'request': request,
        'title': 'fishare - List of Files',
        'files': files
    }

    # render
    return jinja.TemplateResponse('admin.html', data)
```
