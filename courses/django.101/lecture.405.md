---
title: Django Testing Intro
courseid: django101
order: 405
layout: lecture
---

## Intro to Testing


## How to Structure Tests

po vytvoreni aplikacie sa v nej nachdza subor `tests.py`, kde sa maju nachadzat testy. ten je ale hodne zbytocny, pretoze:

* testovat budeme pohlady, REST API, formulare, modely a ine a to vsetko nie je prakticke pchat do jedneho suboru
* navigacia v jednom subore bude otrasna

preto miesto suboru `tests.py` je lepsie spravit balik `tests` a do neho vytvorit subory, ktore bude reprezentovat jednotlive typy testov, napriklad:

* `test_models.py` - testy tykajuce sa modelov
* `test_views.py` - testy tykajuce sa pohladov
* `test_api.py` - testy tykajuce sa REST API
* a pod

kazdy model, ktory obsahuje testy, bude mat prefix `test_`. takze takymto sposobom upravime architekturu projektu


## Testing Library

standardne sa pouziva kniznica `unittest`, ale my budeme pouzivat rozsirenie Djanga o moznost testovat pomocou kniznice [`pytest`](https://pytest-django.readthedocs.io/en/latest/)

nainstalujeme ju teda najprv:

```bash
$ pip install pytest-django
```

V korenovom priecinku vytvorime subor `pytests.ini` a vlozime do neho konfiguraciu pre `pytest`:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py
```


## First (Empty) Run

teraz mozeme vyskusat spustit testy v korenovom priecinku Django projektu:

```bash
$ pytest
```

**Pozor:** Ak by sme testy pisali standardne pomocou modulu `unittest`, tak by sme ich spustali prikazom

```bash
$ python3 manage.py test
```

tym, ze sa ale chystame pouzivat na testovanie `pytest`, budeme testy spustat priamo s nim (aplikovanim konfiguracie zo suboru `pytest.ini`).


## Why would I use this instead of Django’s `manage.py` test command?

Running the test suite with pytest offers some features that are not present in Django’s standard test mechanism:

* Less boilerplate: no need to import `unittest`, create a subclass with methods. Just write tests as regular functions.
* Manage test dependencies with fixtures.
* Run tests in multiple processes for increased speed.
* There are a lot of other nice plugins available for pytest.
* Easy switching: Existing unittest-style tests will still work without any modifications.


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 24

* [Pytest Django](https://pytest-django.readthedocs.io/en/latest/)

* [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/)

* [Obey the Testing Goat!](https://www.obeythetestinggoat.com/)

