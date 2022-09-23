---
title: SQL Admin
courseid: fastapi
order: 208
layout: lecture
description: |
    jednoduche admin rozhranie
---

## Instalacia

```bash
$ poetry add sqladmin
```


## Admin Model

najprv v module `file_details.py` vytvorime admin model. tento model bude opisovat, co bude zobrazene v admin pohlade.

```python
class FileDetailsAdmin(ModelView, model=FileDetails):
    column_list = [
        FileDetails.filename,
        FileDetails.slug,
        FileDetails.mime_type,
        FileDetails.size,
        FileDetails.downloads,
        FileDetails.max_downloads
    ]
```


## Admin rozhranie

```python
# admin
engine = create_engine(get_settings().db_uri)
admin = Admin(app, engine)

admin.add_view(FileDetailsAdmin)
```


## Linky

* [SQLAlchemy Admin](https://github.com/aminalaee/sqladmin) - projekt na Github-e
* [SQLAlchemy Admin Documentation](https://aminalaee.dev/sqladmin/) - dokumentacia modulu
