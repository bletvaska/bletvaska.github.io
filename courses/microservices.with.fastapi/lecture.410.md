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
@router.get("/", summary="Run background jobs.")
def run_cron_job(session: Session = Depends(get_session)):
    start = datetime.now()

    # query
    statement = select(File).where(or_(datetime.now() > File.expires, File.downloads >= File.max_downloads))
    files = session.exec(statement).all()

    # delete files
    for file in files:
        # prepare path
        path = settings.storage / file.slug

        # delete file
        session.delete(file)
        session.commit()

        # delete file from storage
        path.unlink(missing_ok=True)

    # count duration
    end = datetime.now()
    duration = end - start

    return {
        'startedAt': start,
        'finishedAt': end,
        'removedFiles': len(files),
        'duration': duration.total_seconds()
    }
```