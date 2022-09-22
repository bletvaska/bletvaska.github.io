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
$ http http://localhost:8000/static/css/style.css
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
