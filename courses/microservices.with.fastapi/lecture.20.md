---
title: File Update
courseid: fastapi
order: 20
layout: lecture
description: |
    aktualzácia existujúcich záznamov, plná aktualizácia pomocou metódy `PUT`, čiastočná aktualizácia pomocou metódy `PATCH`
---

## HTTP Status Code and Response

* stavovy kod v oboch pripadoch moze zalezat od toho, ci odpoved obsahuje telo alebo nie:
    * v pripade, ze telo obsahuje, tak sa odporuca pouzitie stavoveho kodu `200`
    * ak sa vsak v odpovedi telo nenachadza, odporuca sa pouzitie stavoveho kodu `204`


## `PUT` - Full Update

* vsetky parametre su povinne

    * subor
    * nazov suboru
    * pocet stiahnuti


### Ukazka implementacie

```python
@router.put('/files/{slug}')
def full_update_file(slug: str,
                     payload: UploadFile = fastapi.File(...),
                     filename: str = Form(...),
                     max_downloads: int = Form(...)):
    try:
        # get existing file from db
        with Session(engine) as session:
            statement = select(File).where(File.slug == slug)
            file = session.exec(statement).one()

            # upload new file and update/overwrite existing file/attributes
            path = settings.storage / slug
            with open(path, 'wb') as dest:
                shutil.copyfileobj(payload.file, dest)

            # update the file object
            file.size = path.stat().st_size
            file.filename = filename
            file.max_downloads = max_downloads
            file.content_type = payload.content_type
            file.updated_at = datetime.now()

            session.add(file)
            session.commit()
            session.refresh(file)

            return file

    except NoResultFound:
        content = ProblemDetails(
            title='File not found.',
            detail=f"No file with slug '{slug}'",
            status=404,
            instance=f'/files/{slug}'
        )

        return ProblemJSONResponse(
            status_code=404,
            content=content.dict(exclude_unset=True)
        )
```


## `PATCH` - Partial Update

* jednotlive parametre su volitelne

    * subor
    * nazov suboru
    * max pocet stiahnuti


### Ukazka implementacie

```python
@router.patch('/files/{slug}')
def partial_file_update(slug: str,
                        payload: Optional[UploadFile] = fastapi.File(None),
                        filename: Optional[str] = Form(None),
                        max_downloads: Optional[int] = Form(None)):
    try:
        # get existing file from db
        with Session(engine) as session:
            statement = select(File).where(File.slug == slug)
            file = session.exec(statement).one()

            # upload/override new file if provided
            if payload is not None:
                path = settings.storage / slug
                with open(path, 'wb') as dest:
                    shutil.copyfileobj(payload.file, dest)

                # update the file object
                file.size = path.stat().st_size
                file.content_type = payload.content_type
                file.updated_at = datetime.now()

            # update filename if provided
            if filename is not None:
                file.filename = filename
                file.updated_at = datetime.now()

            # update max downloads if provided
            if max_downloads is not None:
                file.max_downloads = max_downloads
                file.updated_at = datetime.now()

            # commit changes to db
            session.add(file)
            session.commit()
            session.refresh(file)

            return file

    except NoResultFound:
        content = ProblemDetails(
            title='File not found.',
            detail=f"No file with slug '{slug}'",
            status=404,
            instance=f'/files/{slug}'
        )

        return ProblemJSONResponse(
            status_code=404,
            content=content.dict(exclude_unset=True)
        )
```


## Additional Links

* MDN: [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)
* MDN: [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)
