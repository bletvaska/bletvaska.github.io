---
title: HTTP DELETE
courseid: fastapi
order: 310
layout: lecture
description: |
    odstránenie existujúcej položky
---

* navratovy kod `204` - No Content

* vo výsledku sa nesmie nachádzať žiadny obsah
    * pretože No Content

## HTTP Request Example

```bash
$ http DELETE http://app.com/files/WjaGsbI
```

```http
HTTP/1.1 204 No Content
date: Tue, 16 Nov 2021 23:07:18 GMT
server: uvicorn
```


## Delete in FastAPI

```python
@router.delete('/files/{file_id}')
def delete_file(file_id: str):
    try:
        with Session(engine) as session:
            statement = select(File).where(File.key == file_id)
            file = session.exec(statement).one()
            session.delete(file)
            session.commit()
            return Response(status_code=204)
    except NoResultFound:
        return JSONResponse(status_code=404, content={
            "message": "File not found.",
            "detail": {
                "key": f"No file with key '{file_id}'"
            }
        }
                            )
```


## Additional Links

* MDN: [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)
