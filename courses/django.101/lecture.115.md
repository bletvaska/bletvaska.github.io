---
title: Files App
courseid: django101
order: 115
layout: lecture
---


## The Files App

Inspiracia zo sluzby [file.io](https://www.file.io/) na nahravanie suborov.


## Creation

vytvorime appku:

```bash
$ ./manage.py startapp files
```

a pridame ju do zoznamu aplikacii projektu v subore `config/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "files",
    # ...
]
```



