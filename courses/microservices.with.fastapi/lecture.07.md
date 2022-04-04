---
title: Post New File
courseid: fastapi
order: 15
layout: lecture
description: |
    ako vytvoriť novú položku pomocou metódy POST, voliteľné parametre
---

## HTTP Status Code and Response

* po vytvoreni sa nevracia kod `200 - OK`, ale vracia sa kod `201 - Created` .

* vo výsledku sa zvykne vracať novovytvorený objekt

    * odfiltrovať položky/kľúče, ktoré by nemal klient vidieť
    * pridať kľúč `url`/`link`, kde sa dá ku položke pristúpiť/stiahnuť


## Parametre funkcie

* parametrom bude urcite subor, ktory sa bude nahravat

* volitelne mozeme pridat dalsie parametre, ako:

	* nazov suboru
	* maximalny pocet stiahnuti

* aby boli parametre voliteľné, treba miesto `...` pridat `None`

* parametrom vsak nemoze byt model/json, pretoze formularove data sa nemozu miesat s JSON-om. to nie je vlastnost FastAPI, ale HTTP protokolu

	> Warning: You can declare multiple File and Form parameters in a path operation, but you can't also declare Body fields that you expect to receive as JSON, as the request will have the body encoded using multipart/form-data instead of application/json. This is not a limitation of FastAPI, it's part of the HTTP protocol. ([FastAPI](https://fastapi.tiangolo.com/tutorial/request-files/#what-is-form-data))


## Implementacia

```python
@router.post('/files/', response_model=File)
def create_file(request: Request,
                payload: UploadFile = fastapi.File(...),
                filename: Optional[str] = Form(None),
                max_downloads: Optional[int] = Form(None)):
    # prepare the file entry
    file = File(
        filename=payload.filename if filename is None else filename,
        content_type=payload.content_type,
    )

    # set max downloads, if provided
    if max_downloads is not None:
        file.max_downloads = max_downloads

    # get ready
    path = settings.storage / file.slug

    # check if storage directory exists
    if not settings.storage.is_dir():
        settings.storage.mkdir(parents=True, exist_ok=True)

    # save uploaded file
    with open(path, 'wb') as dest:
        shutil.copyfileobj(payload.file, dest)

    # get file size
    file.size = path.stat().st_size

    # insert file in to db
    with Session(engine) as session:
        session.add(file)
        session.commit()
        session.refresh(file)

    # return RedirectResponse(f'/uploaded/?slug={file.slug}', 
    #                         status_code=302)

    # return newly created file
    return JSONResponse(
        status_code=201,
        content=jsonable_encoder(file)
    )
```


## Testovanie cez httpie

```bash
$ http -f post http://localhost:8080/api/v1/files/ \
    payload@slides.html \
    filename=prezentacia.html
```

```http
HTTP/1.1 201 Created
content-length: 212
content-type: application/json
date: Tue, 07 Dec 2021 16:36:46 GMT
server: uvicorn

{
    "content_type": "text/html",
    "created_at": "2021-12-07T17:36:46.454462",
    "downloads": 0,
    "filename": "prezentacia.html",
    "id": 40,
    "max_downloads": 1,
    "size": 6652,
    "slug": "V-PEEAKZ",
    "updated_at": "2021-12-07T17:36:46.454470"
}
```


## Additional Links

* MDN: [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
