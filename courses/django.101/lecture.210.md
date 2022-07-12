---
title: Uploading a File
courseid: django101
order: 210
layout: lecture
---

## Making the Storage

urobime to jednoducho - vyrobime priecinok `storage/`, kde budeme nahravat subory:

```bash
$ mkdir storage/
```

okrem toho do nastaveni pridame nove nastavenie, ktore bude toto miesto opisovat. nazveme ho `MEDIA_ROOT`:

```python
MEDIA_ROOT='storage/'
```


## Making the File Uploadable

do modelu pridame novu polozku, ktora bude typu `FileField`. pomocou jej parametra `upload_to` povieme, kde sa ma subor nahrat. na tento ucel pouzijeme prave vytvorene nastavenie:

```python
from django.conf import settings

...

file = models.FileField(upload_to=settings.STORAGE, null=False)
```

Ak teraz cez admin rozhranie skusime vytvorit polozku, uz tu mame subor, ktory vieme nahrat. Po jeho nahrati mozeme skontrolovat, ze sa naozaj nachadza v priecinku `storage/`.


## Refactoring

je mozne, ze bude potrebne odstranit obsah tabulky s existujucimi polozkami, nakolko subor je povinny a neda sa nahradit len tak `NULL` hodnotou. takze odstranit napriklad pomcou `TRUNCATE`:

```sql
DELETE FROM files_file;
```


## Updating Fields based on File Object

su veci, ktore uz odteraz nemusime zadavat ohladom suboru, pretoze tie klucove veci sa budu nachadzat v nahravanom subore. to sa tyka

* nazvu suboru
* velkosti suboru
* mime typu suboru

preto vsetky tieto polozky mozeme oznacit priznakom `editable=False`.

vysledna podoba modelu bude potom vyzerat takto:

```python
class File(models.Model):
    filename = models.CharField(max_length=128, editable=False)
    downloads = models.IntegerField(default=0, editable=False)
    max_downloads = models.IntegerField(default=1)
    size = models.IntegerField('File Size', editable=False)
    mime_type = models.CharField(max_length=64, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=False)
```


## Overriding Save

potrebujeme prepisat spravanie metody `.save()`, ktora sluzi na ulozenie udajov do databazy a na nahratie suboru na disk:


```python
    def save(self, *args, **kwargs):
        self.filename = self.file.name
        self.size = self.file.size
        self.mime_type = self.file.file.content_type

        super().save(args, kwargs)
```


## Overriding Delete

pri zmazani nedojde k zmazaniu aj suboru. preto prepiseme aj metodu `.delete()`, kde sa o to zmazanie postarame sami:

```python
def delete(self, *args, **kwargs):
    # delete from filesystem first
    path = settings.MEDIA_ROOT / self.filename
    path.unlink(missing_ok=True)

    # delete from db
    super().delete(args, kwargs)
```