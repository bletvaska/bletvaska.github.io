---
title: FastAPI
description: rámec FastAPI, vlastnosti, inštalácia, prvé použitie
courseid: fastapi
order: 103
layout: lecture
---

* [porovnanie s inými rámcami a technológiami](https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=query&l=v2p4an-db&a=2)

## Inštalácia

Ramec FastAPI nainstalujeme pomocou nastroja `poetry`. Okrem neho vsak budeme potrebovat aj ASGI server `uvicorn`. Oba baliky nainstalujeme prikazom:

```bash
$ poetry add fastapi uvicorn[standard]
```


## Hello World!

aby sme sa zbytocne nezdrziavali, pouzijeme rovno kostru aplikacie so vsetkym potrebnym. do svojho modulu `main.py` vlozte tento kod:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello, World!"


def main():
    uvicorn.run('fishare.main:app', reload=True,
                host='127.0.0.1', port=8000)

if __name__ == '__main__':
    main()
```


## Running the App from CLI

a nasledne mozeme aplikaciu spustit prikazom z korenoveho priecinku projektu


```bash
$ uvicorn fishare.main:app --reload
```


## Python Project Interpreter Update

Aktualne sa bude PyCharm stazovat na to, ze nepozna jednotlive moduly, ktore pouzivame a vela veci v nasom kode bude podciarknutych cervenou farbou. to je preto, ze o virtualne prostredie sa momentalne stara `poetry` a _PyCharm_ o tom nevie. aktualizujeme teda nastavenia interpretra:

1. otvorime `File` > `Settings`
2. v dialogovom okne nasledne `Project: fishare` > `Python Interpreter`
3. pri polozke interpretera klikneme na zubate koliesko a klikneme na polozku `Add...`
4. zo zoznamu vlavo najprv vyberieme `Poetry Environment` a zo zoznamu `Existing environment` vyberieme interpreter nasho projektu


## Nastavenie spustania projektu v Pycharm-e

mame v podstate dva sposoby:

1. staci pravym tlacidlom mysi kliknut na modul `main.py` a spustit ho. tym sa vytvori spustac sam. toto je pouzitelne v pripade jednomodulovych projektov. nas bude komplexnejsi, takze toto robit nebudeme.

2. vytvorit samostatnu konfiguraciu pre spustenie projektu cez polozku `Edit Configuration`:

    * module name - `fishare.main`
    * interpereter - poetry set
    * nastavit workdir na korenovy priecinok projektu


## Refactoring with module `__main__.py`


## API Docs

http://127.0.0.1:8000/docs
