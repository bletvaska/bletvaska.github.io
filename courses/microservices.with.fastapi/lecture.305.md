---
title: Dependency Injection
courseid: fastapi
order: 305
layout: lecture
description: |
    ako pouzivat dependency injection vo FastAPI
---

## Introduction

* predstavte si funkciu na prevod penazi z uctu na ucet, ktora by vyzerala takto:

    ```python
    transfer_funds()
    ```

* hned sa vam vyroja otazky typu:

    * z akeho uctu peniaze odchadzaju?
    * na aky ucet peniaze posielam?
    * kolko penazi posielam?
    * v akej mene sa prevod uskutocni?

* odpovede na otazky sa dozvieme az pri pohlade do kodu tejto funkcie, kde sa moze nachadzat pouzitie rozlicne "spinavych" veci:

    * globalne premenne
    * jedinacik
    * staticke metody
    * subor
    * priamo od pouzivatela

* problem pri navrhovani a pisani kodu - vsetko, co funkcia potrebuje pre svoj beh, jej dodajte v podobe parametrov!

    * toto pravidlo vedie k zrozumitelnemu a jednoducho testovatelnemu kodu
    * minimalizuje skryte vazby (ako v pripade funkcie `transfer_funds()`)
    * miesto parametrov funkcie mozete vyuzit aj konstruktor triedy


## What is "Dependency Injection"

**Dependency Injection** means, in programming, that there is a way for your code (in this case, your path operation functions) to declare things that it requires to work and use: **dependencies**.

And then, that system (in this case FastAPI) will take care of doing whatever is needed to provide your code with those needed dependencies (**inject** the dependencies).

This is very useful when you need to:

* Have shared logic (the same code logic again and again).
* Share database connections.
* Enforce security, authentication, role requirements, etc.
* And many other things...

All these, while minimizing code repetition.


## Pouzitie DI

v nasom pripade (a keby len v nasom) mozeme na DI vyuzit pripojenie k databaze. budeme ho totiz pouzivat vo vacsine nasich _path operation functions_. pripravime sa na to a urobime niekolko uprav:

* vytvorime samostatny modul s nazvom `database.py`
* do tohto modulu umiestnime funkciu `get_session()`, ktora nam vrati objekt sedenia s databazou


## Modul `database.py`

metoda `get_session()` bude vlastne generatorom vo vnutri kontext manazera:

  * kontext manazer zabezpeci vytvorenie a uzatvorenie spojenia s databazou
  * generator zabezpeci, ze nebudeme musiet zakazdym vytvarat objekt `engine`

```python
def get_session():
    engine = create_engine(get_settings().db_uri)

    with Session(engine) as session:
        yield session
```


## DI in path operation function

pouzitie DI v _path operation function_ bude vyzerat nasledovne:

```python
def get_list_of_files(session: Session = Depends(get_session)):
    # ...
```

rovnako tak mozeme v pripade potreby pouzivat aj nastavenia.



## Dalsie odkazy

* Nette: [Co je Dependency Injection?](https://doc.nette.org/cs/dependency-injection/introduction)
* FastAPI: [Dependencies - First Steps](https://fastapi.tiangolo.com/tutorial/dependencies/?h=)
* SQLModel: [ Session with FastAPI Dependency ](https://sqlmodel.tiangolo.com/tutorial/fastapi/session-with-dependency/?h=#create-a-fastapi-dependency)
