---
title: Decorators
courseid: fastapi
order: 520
layout: lecture
description: |
    co je a na co je dekorator
---

## Co je to dekorator?


## Priklad

vytvorime samostatny modul `decorators.py` a v nom tento dekorator:

```python
from functools import wraps


def log_client_ip(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):  # request=None,
        request = kwargs['request']
        print(f'>> Opened conection from {request.client.host}')
        response = await func(*args, **kwargs)
        print(f'>> Closing conection from {request.client.host}')
        return response

    return wrapper
```

pouzijeme ho pri pohlade takto:

```python
@router.head('/{slug}')
@router.get('/{slug}', status_code=200,
            summary='Download file by {slug}.')
@log_client_ip
async def download_file(request: Request, slug: str,
                        session: Session = Depends(get_session),
                        settings: Settings = Depends(get_settings)):
    # ...
```
