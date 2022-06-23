---
title: File Model
courseid: django101
order: 120
layout: lecture
---

## Co je to model?


## Django and Databases


Django officially supports the following databases:

* PostgreSQL
* MariaDB
* MySQL
* Oracle
* SQLite

ale podporuje aj dalsie databazy prostrednictvom rozsireni tretich stran


konfiguracia v `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


## The File Model

```python
class File(models.Model):
    filename = models.CharField(max_length=100)
    downloads = models.IntegerField(default=0)
    max_downloads = models.IntegerField(default=1)
    size = models.IntegerField(null=True)
    mime_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
```


## Activating models

na zaklade modelu Django bude vediet vytvorit potrebne tabulky v db.

Aby sa to mohlo udiat, potrebujeme aplikovat migracie:

```bash
$ ./manage.py makemigrations files
```

ak chceme vidiet, ze ako migracia vyzera, mozeme sa pozriet pomocou prikazu:

```bash
$ ./manage.py sqlmigrate files 0001
```

nakoniec uz len nechame vsetky migracie vykonat:

```bash
$ ./manage.py migrate
```


## Testing/Playing

mozeme si pustit shell/konzolu a hrat sa s vytvorenym modelom:

```bash
$ ./manage.py shell_plus
```

a potom uz v standardnom python-e:

```python
# create object
file = File(filename='obrazok.jpg')
file.mime_type = 'image/jpg'
file.max_downloads = 5

# save it to db
file.save()


# check it values
file.id
file.created_at
file.updated_at

# make change and update
file.downloads = 2
file.save()

# check the timestamps
file.created_at
file.updated.at
```
