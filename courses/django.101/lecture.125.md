---
title: Admin Interface
courseid: django101
order: 125
layout: lecture
---

## Admin Interface


## Creating the Superuser

aby sme mohli admin panel pouzivat, potrebujeme si vytvorit spravcu:

```bash
$ ./manage.py createsuperuser
Username (leave blank to use 'mirek'):
Email address: mirek@cnl.sk
Password:
Password (again):
Superuser created successfully.
```


## Accessing Admin Interface

ak teraz spustime server, mozeme sa dostat na adresu http://localhost:8000/admin, kde sa nachadza _Admin Interface_.

Po prihlaseni sa vidime modely, ktore mame k dispozicii, a ktore mozeme pomocou _Admin rozhrania_ spravovat.

Mozeme napriklad pridat dalsieho pouzivatela alebo upravit vlastnosti existujuceho.



## Making File Model available in Admin Interface

aby sme mohli spravovat pomocou admin rozhrania aj nase subory, tak do suboru `admin.py` v aplikacii `files` pridame riadok:

```python
admin.site.register(File)
```

ak aktualizujeme admin rozhranie, uvidime v nom aj nas model.


## Changing the View of Files in Admin Interface

### Providing the Name of the File

aby sme miesto nejakeho generickeho objektu videli nazov suboru v zozname suborov, tak do modelu `File` pridame metodu `__str__()`:

```python
def __str__(self):
    return f'{self.filename}'
```


### Providing more Info to Admin List View


```python
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'mime_type', 'size', 'max_downloads', 'created_at')
```


### Own Labels instead of Field Names

nie je velmi sexi vidiet nazvy clenskych premennych. miesto nich mozeme pouzit popisky z modelov.

prvy parameter v modeli je nepovinny a je opisom daneho pola. tak ak napriklad upravime `size` takto:

```python
size = models.IntegerField('file size', null=True)
```

Tak pri obnoveni pohladu v admin rozhrani uz miesto nazvu `size` uvidime `file size`.



### Own Function instead of Column

```python
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'mime_type', 'format_filesize', 'max_downloads', 'created_at')

    def format_filesize(self, file: File, suffix="B"):
        size = 0
        if file.size:
            size = file.size
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(size) < 1024.0:
                return f"{size:3.1f}{unit}{suffix}"
            size /= 1024.0
        return f"{size:.1f}Yi{suffix}"
```


### Adding Links

```python
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'mime_type', 'format_filesize', 'max_downloads', 'created_at', 'view_link')

        return format_html('<a href="https://www.google.com/search?q=file:{}">Search</a>', file.filename)

    view_link.short_description = "Search on Google"
```


## Additional Resources

* [https://realpython.com/customize-django-admin-python/](Customize the Django Admin With Python)
* [The Django admin site](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)