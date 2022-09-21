---
title: File Update
courseid: fastapi
order: 340
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
@router.put('/files/{slug}', response_model=FileOut,
            summary='Updates the file identified by {slug}. Any parameters not provided are reset to defaults.')
def full_file_update(slug: str,
                     payload: UploadFile,  # UploadFile = fastapi.File(...)
                     filename: str = Form(None),
                     max_downloads: int = Form(...),
                     session: Session = Depends(get_session)
                     ):
    try:
        # get the file with given slug
        statement = select(File).where(File.slug == slug)
        file = session.exec(statement).one()

        # save uploaded file
        path = settings.storage / file.slug
        with open(path, 'wb') as dest:
            shutil.copyfileobj(payload.file, dest)

        # update filename if given
        if filename is not None:
            file.filename = filename
        else:
            file.filename = payload.filename

        # update other file fields
        file.size = path.stat().st_size
        file.max_downloads = max_downloads
        file.updated_at = datetime.now()
        file.mime_type = payload.content_type

        # update db
        session.add(file)
        session.commit()
        session.refresh(file)

        return file

    except NoResultFound as ex:
        # when not found, then 404
        content = ProblemDetails(
            type='/errors/files/put',
            title="File not found.",
            status=404,
            detail=f"File with slug '{slug}' was not found.",
            instance=f"/files/{slug}"
        )

    return JSONResponse(status_code=content.status,
                        content=content.dict())
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
