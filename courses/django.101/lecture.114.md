---
title: Third Party Apps
courseid: django101
order: 114
layout: lecture
---

## Third Party Apps

Aplikacie sa daju aj doinstalovat a tym padom rozsirit funkcionalitu djanga ako takeho.


## Django Extensions

Django Extensions is a collection of custom extensions for the Django Framework.


### Installing

```bash
$ pip install django-extensions
```

treba aktualizovat zoznam nainstalovanych aplikacii v subore `config/settings.py`:

```python
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```


### The Usage

pribudli nam nove prikazy pre nastroj `manage.py`:

* Produce a tab-separated list of (url_pattern, view_function, name) tuples for a project:

  ```bash
  $ ./manage.py show_urls
  ```

* Run the enhanced django shell:

  ```bash
  $ ./manage.py shell_plus
  ```


## Django Debug Toolbar

The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel's content.

### Install

```bash
$ pip install django-debug-toolbar
```

pridat do zoznamu aplikacii `config/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
]
```

pridat adresu do smerovaca `config/urls.py`:

```python
urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```

pridat middleware do `config/settings.py`:

```python
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
```

potrebne je pridat aj zoznam povolenych IP adries do suboru `config/settings.py`:

```python
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```


## Awesome Django

[Awesome Django](https://github.com/wsvincent/awesome-django) is A curated list of awesome things related to Django.