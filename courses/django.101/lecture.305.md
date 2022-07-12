---
title: Django REST Framework
courseid: django101
order: 305
layout: lecture
---

## Installation

podla domovskej stranky projektu:

```bash
$ pip install djangorestframework
$ pip install markdown       # Markdown support for the browsable API.
$ pip install django-filter  # Filtering support
```

po nainstalovani je potrebne pridat `rest_framework` do zoznamu vasich nainstalovanych aplikacii do suboru `config/settings`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

aby sme mohli pouzivat aj "browsable API", je potrebne pridat aj pohlady pre login a logout do suboru `config/urls.py`:

```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```


## Additional Clients

pre testovanie z prikazoveho riadku mozeme pouzivat nastroj `curl`, ktory je vsak dostupny v linuxovych operacnych systemoch. pre python mozeme pouzit alternativu s nazvom [`httpie`](https://httpie.io/)

```bash
$ pip install httpie
```

vyskusat ho mozeme napriklad pomcou REST API na ziskanie casu:

```bash
$ http http://worldtimeapi.org/api/timezone/Europe/Bratislava
```



## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 14

* [Django REST Framework](https://www.django-rest-framework.org/) - domovska stranka projektu

* [httpie](https://httpie.io/) - domovska stranka projektu `httpie`

* [httpie cheatsheet](https://devhints.io/httpie) - tahak na pouzivanie nastroja `httpie`
