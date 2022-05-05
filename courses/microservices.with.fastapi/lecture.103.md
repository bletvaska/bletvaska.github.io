---
title: FastAPI
description: rámec FastAPI, vlastnosti, inštalácia, prvé použitie
courseid: fastapi
order: 103
layout: lecture
---

* [porovnanie s inými rámcami a technológiami](https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=query&l=v2p4an-db&a=2)

## Inštalácia

```bash
$ poetry add fastapi
```


## Hello World!

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello, World!"
```


spustit:


```bash
$ uvicorn fishare.main:app --reload
```

alebo

```python
uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
```

## API Docs

http://127.0.0.1:8000/docs


## Refaktoring

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello, World!"


def main():
    uvicorn.run('fishare.main:app', port=8000, host='127.0.0.1', reload=True)

if __name__ == '__main__':
    main()
```

spustit z korenoveho priecinku projektu (nad balikom `fishare`):

```bash
$ python -m fishare.main
```