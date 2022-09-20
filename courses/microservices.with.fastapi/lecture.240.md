---
title: Fake files
courseid: fastapi
order: 240
layout: lecture
description: |
    priprava dat v databaze
---



## Vytvorenie funkcie `populate_data()`

vytvorime funkciu pre generovanie nahodnych dat, aby ich ukladala rovno do databazy. vytvorime samostatny modul `helpers.py` a do neho vlozime tento kod:

```python
import random

from faker import Faker
from sqlmodel import create_engine, Session

from fishare.models.file_details import FileDetails
from fishare.models.settings import get_settings


def populate_data(count: int = 100):
    engine = create_engine(get_settings().db_uri)

    faker = Faker()
    categories = ('audio', 'video', 'image', 'text')

    with Session(engine) as session:
        for _ in range(count):
            category = random.choice(categories)
            file = FileDetails(
                filename=faker.file_name(category=category),
                mime_type=faker.mime_type(category=category),
                size=random.randint(100, 100000000)
            )
            session.add(file)

        session.commit()

```


## Refaktoring `GET /files/{slug}`

```python
@router.head('/files/{slug}')
@router.get('/files/{slug}', response_model=FileOut,
            summary="Get file identified by the {slug}.")
def get_file(slug: str):
    try:
        engine = create_engine(settings.db_uri)

        with Session(engine) as session:
            statement = select(File).where(File.slug == slug)
            return session.exec(statement).one()

    except NoResultFound as ex:
        content = ProblemDetails(
            type='/errors/files',
            title="File not found.",
            status=404,
            detail=f"File with slug '{slug} was not found.'",
            instance=f"/files/{slug}"
        )

        return JSONResponse(
            status_code=404,
            content=content.dict(exclude_unset=True)
        )
```