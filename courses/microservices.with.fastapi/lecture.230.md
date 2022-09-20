---
title: SQLModel
courseid: fastapi
order: 230
layout: lecture
description: |
    praca s databazou, SQLModel, SQL Alchemy
---

## Installation

```bash
$ poetry add sqlmodel
```


## Model Refaktoring

upravime signaturu triedy a pridame primarny kluc:

```python
from sqlmodel import SQLModel, Field

class File(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    ...
```


## Settings Refaktoring

pridame polozku do nastaveni pre pripojenie k databaze:

```python
class Settings(BaseSettings):
    db_uri: str = 'sqlite:///database.db'

    ...
```

tym mozeme pridat lubovolnu databazu a nakonfigurovat jej pripojenie len pomocou tohto retazca


## Table Initialization

za zaciatok funkcie `main()` pridame:

* vytvorenie db enginu
* vytvorenie tabuliek podla modelov

```python
def main():
    # init db
    engine = create_engine(settings.db_uri)
    SQLModel.metadata.create_all(engine)

    ...
```


## Aktualizacia funkcie `populate_data()`

upravime funkciu pre generovanie nahodnych dat, aby ich ukladala rovno do databazy:

```python
def populate_data(count: int = 10):
    engine = create_engine(settings.db_uri)

    faker = Faker()
    categories = ('audio', 'video', 'image', 'text')

    with Session(engine) as session:
        for _ in range(count):
            category = random.choice(categories)
            file = File(
                id=_,
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