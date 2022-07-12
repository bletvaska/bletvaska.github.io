---
title: Code Coverage
courseid: django101
order: 450
layout: lecture
---


## Code Coverage

## Pytest and Code Coverage

```bash
$ pip install pytest-cov
```


## Running the Coverage

```bash
$ pytest --cov
```


## Coverage with HTML Report

treba doinstalovat balik `pytest-html`:


```bash
$ pip install pytest-html
```

a upravit podobu `pytest.ini`:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
# -- recommended but optional:
python_files =
    tests.py
    test_*.py
    *_tests.py
addopts =
    --cov=fishare
    --cov-report=html
    --cov-report=term
    --html=report.html
    --self-contained-html
```

aktualne sa bude spustat coverage automagicky vzdy pri spusteni pytest-u. report pre coverage sa bude nachadzat v priecinku `htmlcov/` a report testov sa bude nachadzat v subore `report.html`


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 24

* [Pytest Django](https://pytest-django.readthedocs.io/en/latest/)

* Namakaný webinár #39: [Základy testovania v jazyku Python s rámcom pytest (nie len) pre učiteľov](http://namakanyden.sk/webinars/2022.09-pytest.101.html)

* [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/)

* [Obey the Testing Goat!](https://www.obeythetestinggoat.com/)

