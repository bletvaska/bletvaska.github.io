---
title: Pagination
courseid: fastapi
order: 320
layout: lecture
description: |
    stránkovanie výsledkov
---

## V čom je problém

* nemôžeme vracať všetky záznamy
  * príliš veľa
  * s pribúdajúcim počtom bude aj ich spracovanie a vrátenie trvať dlhší a dlhší čas
  * množstvo získaných dát bude rásť s pribúdajúcim počtom položiek
  * veľmi jednoducho by sme vedeli zabezpečiť DOS útok


## Ukážky

### Django

```python
{
    "count": 4321,
    "next": "http://app.com/users/?page=2",
    "previous": null,
    "results": [
        ...
    ]
}
```


## Podpora strankovania

zacneme tym, ze pridame podporu strankovania do pohladu pre ziskanie zoznamu suborov. vyuzijeme na to query parametre. implementacia bude vyzerat nasledovne:

```python
@router.get('/', summary='Get list of files.', response_model=list[FileDetailsOut])
def get_list_of_files(offset: int = 0, page_size: int = 50, session: Session = Depends(get_session)):
    # SELECT * FROM files LIMIT (offset - 1) * page_size, page_size
    statement = select(FileDetails).offset((offset - 1) * page_size).limit(page_size)
    files = session.exec(statement).all()
    return files
```



## Pager Model

vytvorime si samostatny model:

```python
class Pager(BaseModel):
    results: List[FileOut] = []
    next: AnyHttpUrl = None
    first: AnyHttpUrl = None
    last: AnyHttpUrl = None
    previous: AnyHttpUrl = None
```


## Updating View

no a pripravime pohlad:

```python
@router.get("/", response_model=list[FileDetailsOut],
            summary="Get list of files.")
def get_list_of_files(offset: int = 0, page_size: int = 50,
                      session: Session = Depends(get_session)):
    """
    Returns the Pager, which contains the list of files.

    :param offset: page offset
    :param page_size: size of the page
    :return: Pager object
    """

    try:
        # count nr of files
        files_count = session.query(File).count()

        # get data
        start = offset * page_size
        statement = select(File).offset(start).limit(page_size)
        files = session.exec(statement).all()

        # prepare next link
        if start + page_size >= files_count:
            next_page = None
        else:
            next_page = f'{settings.base_url}/api/v1/files/?offset={offset + 1}&page_size={page_size}'

        # prepare previous link
        if start - page_size <= 0:
            prev_page = None
        else:
            prev_page = f'{settings.base_url}/api/v1/files/?offset={offset - 1}&page_size={page_size}'

        # get result
        return Pager(
            first=f'{settings.base_url}/api/v1/files/?page_size={page_size}',
            last=f'{settings.base_url}/api/v1/files/?page_size={page_size}&offset={(files_count // page_size) - 1}',
            next=next_page,
            previous=prev_page,
            results=files
        )

    except Exception as ex:

        content = ProblemDetails(
            type='/errors/server',
            title="Some error occured.",
            status=500,
            detail=str(ex),
            instance=f"/files/?page_size={page_size}&offset={offset}"
        )

    return JSONResponse(
        status_code=content.status,
        content=content.dict(exclude_unset=True)
    )
```



## FastAPI Pagination

* vo fastapi netreba nic riesit, pretoze na to mame samostatny modul. homepage https://uriyyo-fastapi-pagination.netlify.app/

* installation:
	```bash
    # with pip
    $ pip3 install fastapi-pagination

    # with poetry
    $ poetry add fastapi-pagination
	```
