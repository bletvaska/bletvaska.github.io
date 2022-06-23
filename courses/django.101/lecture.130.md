---
title: Uploading a File
courseid: django101
order: 125
layout: lecture
---

## Making the Storage

urobime to jednoducho - vyrobime priecinok `storage/`, kde budeme nahravat subory:

```bash
$ mkdir storage/
```

okrem toho do nastaveni pridame nove nastavenie, ktore bude toto miesto opisovat. nazveme ho `STORAGE`:

```python
STORAGE='storage/'
```


## Making the File Uploadable

do modelu pridame novu polozku, ktora bude typu `FileField`. pomocou jej parametra `upload_to` povieme, kde sa ma subor nahrat. na tento ucel pouzijeme prave vytvorene nastavenie:

```python
from django.conf import settings

...

file = models.FileField(upload_to=settings.STORAGE)
```

Ak teraz cez admin rozhranie skusime vytvorit polozku, uz tu mame subor, ktory vieme nahrat. Po jeho nahrati mozeme skontrolovat, ze sa naozaj nachadza v priecinku `storage/`.
