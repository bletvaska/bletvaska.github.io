---
title: File Download
courseid: fastapi
order: 360
layout: lecture
description: |
    stiahnutie suboru
---

## Introduction

pri stahovani netreba zabudnut, ze chceme dovolit stiahnut len subory, ktore:

* existuju ;)
* maju pocet stiahnuti mensi ako maximalny dovoleny pocet na stiahnutie
* neuplynula im expiracia


## Endpoint

vytvorime novy modul s baliku `api` s nazvom `download.py` a do neho vlozime nasledujuci obsah:

```python
import fastapi
from fastapi import Depends
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from starlette.requests import Request
from starlette.responses import JSONResponse, FileResponse

from fishare.database import get_session
from fishare.models.file_details import FileDetails
from fishare.models.problem_details import ProblemDetails
from fishare.models.settings import get_settings, Settings

router = fastapi.APIRouter()


@router.head('/{slug}')
@router.get('/{slug}', status_code=200,
            summary='Download file by {slug}.')
def download_file(request: Request, slug: str,
                  session: Session = Depends(get_session),
                  settings: Settings = Depends(get_settings)):
    try:
        # get file by slug
        # SELECT * FROM filedetails WHERE slug={slug} AND downloads < max_downloads
        statement = select(FileDetails) \
            .where(FileDetails.slug == slug) \
            .where(FileDetails.downloads < FileDetails.max_downloads)
        file = session.exec(statement).one()

        # update the number of downloads
        if request.method == 'GET':
            file.downloads += 1
            session.commit()
            session.refresh(file)

        # return file
        return FileResponse(
            settings.storage / file.slug,  # path
            media_type=file.mime_type,  # content-type
            filename=file.filename  # filename
        )

    except NoResultFound as ex:
        problem = ProblemDetails(
            status=404,
            title='File not found',
            detail=f"File with slug '{slug}' does not exist.",
            instance=f'{request.url.path}'
        )

        return JSONResponse(
            status_code=problem.status,
            content=problem.dict(),
            media_type='application/problem+json'
        )
```
