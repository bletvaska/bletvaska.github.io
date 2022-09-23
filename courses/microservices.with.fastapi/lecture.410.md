---
title: Cron Endpoint
courseid: fastapi
order: 410
layout: lecture
description: |
    spustanie na pozadi
---

## Introduction

http protokol je synchronny. aby sa veci vykonali, klient potrebuje urobit dopyt.

obcas je potrebne ale spustit sluzby na pozadi. napr. indexovanie, cistenie, priprava dat a pod. na toto sa s oblubou pouziva v linuxovych systemoch cron. casto maju webove aplikacie priamo pripraveny endpoint, ktorym sa tieto sluzby spustia, ale casto maju aj nastroj z prikazoveho riadku, ktorym je mozne tieto operacie spustit priamo z prikazoveho riadku.

my si urobime endpoint


## Endpoint `/cron`

```python
@router.get('/', summary="Run background jobs.")
def cleanup(session: Session = Depends(get_session),
            settings: Settings = Depends(get_settings)):
    start = datetime.now()

    # SELECT * FROM filedetails WHERE downloads >= max_downloads OR now() > expires;
    statement = select(FileDetails).where(or_(
        FileDetails.downloads >= FileDetails.max_downloads,
        datetime.now() > FileDetails.expires
    ))
    files = session.exec(statement).all()

    # delete files
    for file in files:
        # delete file from storage
        path = settings.storage / file.slug
        path.unlink(missing_ok=True)

        # delete file from database
        session.delete(file)
        session.commit()

    # count duration
    end = datetime.now()
    duration = end - start

    return {
        'startedAt': start,
        'finishedAt': end,
        'duration': duration.total_seconds(),
        'removedFiles': len(files)
    }
```