---
title: Templates
courseid: django101
order: 215
layout: lecture
---

## About Templates

* v priecinku `templates/` pre vsetky appky

    * netreba sa potom tolko vnarat, ako v pripade samostatnych priecinkov pre jednotlive appky


## Configuration

v nastaveniach treba upravit zoznam v premennej `TEMPLATES`:

```python
'DIRS': [
    BASE_DIR / 'templates'
],
```

tym vsetky sablony v aplikaciach sa budu nachadzat priamo v priecinku `templates/` projektu.


## Making Homepage

v priecinku `templates/`


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 14
