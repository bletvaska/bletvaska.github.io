---
title: REST API Skeleton
courseid: fastapi
order: 110
layout: lecture
description: |
    čo je to REST API, paralela s jazykom SQL, vytvorenie prvého REST API
---

## Čo je to REST API?

## Vytvorenie API pre zdroj `files`

```python
import fastapi

router = fastapi.APIRouter()


  # select * from files
@router.get('/files/', summary="Get list of files.")
def list_of_files():
    return [
        'file1',
        'file2',
        'file3'
    ]


# select * from files where filename={slug}
@router.get('/files/{slug}', summary="Get file identified by the {slug}.")
def get_file(slug: str):
    return {
        'filename': 'file4',
        'slug': slug
    }


# delete from files where filename={filename}
@router.delete('/files/{slug}',
               summary='Deletes the file identified by {slug}.')
def delete_file(slug: str):
    return "deleted"


# update files where filename={slug} set ...  # full update
@router.put('/files/{slug}',
            summary='Updates the file identified by {slug}. Any parameters not '
            'provided are reset to defaults.')
def full_update_file(slug: str):
    return "full update"


# update files where filename={filename} set ... # partial update
@router.patch('/files/{slug}',
              summary='Updates the file identified by {slug}. For any '
              'parameters not provided in request, existing values are '
              'retained.')
def partial_file_update(filename: str):
    return "partial update"


# insert into files values ()
@router.post('/files/', summary='Uploads file and creates file details.')
def create_file():
    return "file was created"
```



## Organizacia projektu
