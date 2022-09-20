---
title: Output Model
courseid: fastapi
order: 210
layout: lecture
description: |
    expose critical/sensitive data
---

## Problem

* vystavovanie citlivych udajov


## FileOut Model

lenze nechceme, aby koncovi pouzivatelia videli vsetky polozky. urobime si preto model, ktory budeme pouzivat na prezentovanie vysledkov:

```python
class FileOut(BaseModel):
    slug: str
    filename: str
    downloads: int
    max_downloads: int
    size: int
    mime_type: str
    url: HttpUrl = None

    @validator('url', always=True)
    def set_file_url(cls, value, values):
        return f'http://localhost:9000/{values["slug"]}'
```


## Aktualizovanie REST API

no a potom mozeme vratit jeden subor:

```python
@router.head('/files/{slug}')
@router.get('/files/{slug}', response_model=FileOut)
def get_file(slug: str):
    for file in files:
        if file.slug == slug:
            return file

    return {}
```

podobne mozeme upravit aj zoznam suborov:

```python
@router.get("/files/", response_model=List[FileOut])
def get_list_of_files():
    return files
```
