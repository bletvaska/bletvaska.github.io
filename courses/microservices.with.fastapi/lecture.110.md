---
title: REST API Skeleton
courseid: fastapi
order: 110
layout: lecture
description: |
    čo je to REST API, paralela s jazykom SQL, vytvorenie prvého REST API
todo:
* mozno by to chcelo zacat robit po jednom a nie cely template nahodit naraz
* alebo pracovat so statickym zoznamom suborov a naprogramovat jednotlive veci manualne
    * strata casu?
    * ukazat na tom funkcionalne programovanie
---

## Čo je to REST API?

## Vytvorenie API pre zdroj `files`

### Architektura projektu

pre REST API urobime samostatny balik a v nom modul `files.py`, ktory bude obsahovat vsetky HTTP metody pre pracu so subormi. struktura projektu bude nasledne vyzerat takto:

```
fishare_project
├── fishare
│   ├── api
│   │   ├── files.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
└── readme.md
```


### Ziskanie zoznamu suborov

zacneme tym, ze vytvorime funkciu `get_list_of_files()`, ktora vrati zoznam suborov:

```python
import fastapi

router = fastapi.APIRouter()


  # select * from files
@router.get('/api/v1/files/', summary="Get list of files.")
def list_of_files():
    return [
        'file1',
        'file2',
        'file3'
    ]
```

aby vsetko pracovalo ako malo, v module `main.py` musime pridat tento router do objektu aplikacie `app`:

```python
# application init
app = FastAPI()
app.include_router(files.router)
```


### Ziskanie informacii o jednom subore

```python
# select * from files where filename={slug}
@router.get('/api/v1/files/{slug}', summary="Get file identified by the {slug}.")
def get_file(slug: str):
    return {
        'filename': 'file4',
        'slug': slug
    }
```


### Odstranenie suboru

```python
# delete from files where filename={filename}
@router.delete('/api/v1/files/{slug}',
               summary='Deletes the file identified by {slug}.')
def delete_file(slug: str):
    return "deleted"
```


### Uplna aktualizacia informacii o subore

```python
# update files where filename={slug} set ...  # full update
@router.put('/api/v1/files/{slug}',
            summary='Updates the file identified by {slug}. Any parameters not '
            'provided are reset to defaults.')
def full_update_file(slug: str):
    return "full update"
```


### Ciastocna aktualizacia informacii o subore

```python
# update files where filename={filename} set ... # partial update
@router.patch('/api/v1/files/{slug}',
              summary='Updates the file identified by {slug}. For any '
              'parameters not provided in request, existing values are '
              'retained.')
def partial_file_update(filename: str):
    return "partial update"
```


### Vytvorenie noveho suboru

```python
# insert into files values ()
@router.post('/api/v1/files/', summary='Uploads file and creates file details.')
def create_file():
    return "file was created"
```


## Refaktoring: Spolocny prefix pre zdroj `/files`

ak si vsimneme, tak vsetky metody maju spolocny prefix, ktorym je `/api/v1/files`. aby sme sa neopakovali a aj v pripade moznej zmeny/aktualizacie cesty pre tento zdroj, vytiahneme spolocny prefix do modulu `main.py`:

```python
# application init
app = FastAPI()
app.include_router(files.router, prefix='/api/v1/files')
```

nasledne aktualizujeme vsetky dektoratory v module `files.py` a upravime cestu odstranenim uvedeneho prefix-u na `/` a `/{slug}`.
