---
title: REST API
courseid: fastapi
order: 05
layout: lecture
description: |
    čo je to REST API, paralela s jazykom SQL vytvorenie prvého REST API
---


## Čo je to REST API?


## Vytvorenie API pre zdroj `files`

```python
import fastapi

router = fastapi.APIRouter()


@router.get('/files/')  # select * from files
def list_of_files():
    return [
        'file1',
        'file2',
        'file3'
    ]


@router.get('/files/{filename}')  # select * from files where filename={filename}
def get_file(filename: str):
    return {
        'filename': filename
    }


@router.delete('/files/{filename}')  # delete from files where filename={filename}
def delete_file(filename: str):
    return "deleted"


@router.put('/files/{filename}')  # update files where filename={filename} set ...  # full update
def full_update_file(filename: str):
    return "full update"


@router.patch('/files/{filename}')  # update files where filename={filename} set ... # partial update
def partial_file_update(filename: str):
    return "partial update"


@router.post('/files/')  # insert into files values ()
def create_file():
    return "file was created"
```


