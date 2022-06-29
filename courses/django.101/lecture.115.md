---
title: Files App
courseid: django101
order: 115
layout: lecture
---


## The Files App

Inspiracia zo sluzby [file.io](https://www.file.io/) na nahravanie suborov.


## Creation

vytvorime novu appku v priečinku `fishare/`:

```bash
$ cd fishare/
$ python3 ../manage.py startapp files
```

a pridame ju do zoznamu aplikacii projektu v subore `config/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "files",
    # ...
]
```



