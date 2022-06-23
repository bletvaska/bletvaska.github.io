---
title: First Run
courseid: django101
order: 105
layout: lecture
---

## First Run

Ak sme vsetko urobili dobre, tak mozeme napisat:

```bash
./manage.py runserver
```

V konzole sa nam zobrazi text:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 22, 2022 - 17:53:44
Django version 4.0.4, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


## Opening Web Browser

a mozeme otvorit webovy prehliadac na adrese http://127.0.0.1:8000, kde sa nam zobrazi stranka Django aplikacie.

