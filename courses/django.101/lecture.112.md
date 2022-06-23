---
title: Hello World App
courseid: django101
order: 112
layout: lecture
---

## Creating The Hello World App

Urobime len taku jednoduchu aplikaciu, aby sme videli, ze to naozaj funguje.

Zacneme teda jej vytvorenim:

```bash
$ ./manage.py startapp hello
```


## Structure of the App

V projekte sa nam teda vytvori priecinok `hello/` s nasledujucou strukturou:

```bash
$ tree hello
hello
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

vyznam jednotlivych suborov a priecinkov je nasledovny:


* The two `__init__.py` files are there, as usual, just to define their containing folders as packages.

* The `migrations/` subfolder will hold information about changes to your future database.

* The `models.py` file will define the data model for your app.

* The `views.py` file will handle the logic controlling the app display.


## First View

Do suboru `views.py` vlozime tento kod:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

Tym sme vytvorili nas prvy pohlad.


## Aktualizacia suboru `urls.py`

V priecinku aplikacie vytvorime subor `urls.py`:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```


## Aktualizacia smerovaca projektu

Nakoniec uz len upravime subor `urls.py` v konfiguracii celeho projektu. Upravime teda subor `config/urls.py` takto:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
]
```


## Testing the result

Ak sme postupovali spravne a nedopustili sme sa ziadnej chyby, otvorenim prehliadaca na adrese http://localhost:8000 sa nam zobrazi nasa textova sprava.


## Autoreload on Change

mozeme teraz skusit spravu zmenit na inu, cim aktualizujeme subor s pohladmi pre aplikaciu `hello`.

po zmene nie je nutne nic restartovat. staci len obnovit vytvorenu stranku a zmena sa prejavi okamzite.

samozrejme, ak sa dopustite chyby, tak v terminalovom okne, kde je spusteny server, sa chyba zobrazi a v pripade velkej zavaznosti sa server skonci. ak ale chybu opravite, opat sa automagicky server aktualizuje a vam staci len aktualizovat stranku v prehliadaci.
