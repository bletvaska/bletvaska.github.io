---
title: Installation
description: inštalácia, nástroj Poetry, vytvorenie projektu
courseid: fastapi
order: 102
layout: lecture
---

* problem: niekolko nastrojov a procesov na spravu a manazment projektov


## What is Poetry

* Python packaging and dependency management made easy

* Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.



## Vytvorenie projektu

Vytvorime prazdny projekt v IDE PyCharm, ktory bude typu _Pure Python_. Nastavime:

* nazov projektu na `fishare_project`
* cestu k projektu
* z moznosti interpreterov vyberieme volbu _Virtual Environment_
* nezaklikneme vytvorenie suboru `main.py`

Projekt sa vytvori automaticky a bude prazdny. To je pre nas odrazovy mostik na vytvorenie vlastnej kostry projektu.

**Poznamka:** Projekt sme nevytvarali pomocou nastroja `poetry` kvoli tomu, ze rozlicni ludia maju rozlicne prostredia, resp. rozlicne nakonfigurovane prostredie. Preto vytvorime prazdny projekt, nasledne nainstalujeme `poetry` a upravime nastavenia projektu, aby ho pouzival.


## Poetry Installation

najprv do nasho prostredia nainstalujeme balik `poetry`. to mozeme spravit cez `File` > `Settings` > `Project: fishare` > `Python Interpreter`


## Inicializacia projektu pomocou `poetry`

v domovskom priecinku projektu inicializujeme projekt pomocou `poetry` prikazom

```bash
$ poetry init
```

nasledne sa spusti sprievodca, pomocou ktoreho nastavime metaudaje projektu.

nasledne vytvorime zakladnu kostru projektu, ktora bude vyzerat takto:

```
fishare_project
├── fishare
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
└── readme.md
```

**Poznamka:** priecinok `fishare/` bude obsahovat kod nasho projektu. mozete sa stretnut ale aj s nazvami `src/` alebo `app/` v zavislosti od zvyklosti vyvojarov.


## Pridanie/nainstalovanie zavislosti

zatial v projekte nemame nainstalovany ziadny balicek. o tom sa mozeme presvedcit prikazom

```bash
$ poetry show
```

ten zobrazi zoznam nainstalovanych balickov pomocou poetry.

pre nainstalovanie balicka pouzijeme prikaz `add`. takze ak chcem nainstalovat balicek `ipython`, tak napisem prikaz

```bash
$ poetry add ipython
```

overit instalaciu mozeme opat prikazov `show`:

```bash
$ poetry show
```

ked sa pozrieme do suboru `pyproject.toml`, tak sa balik `ipython` bude nachadzat v hlavnych zavislostiach. tento balik vsak patri do vyvojarskych zavislosti, takze ho bud rucne presunieme alebo ho najprv zmazeme pomocou prikazu `remove`:

```bash
$ poetry remove ipython
```

a nasledne ho nainstalujeme s prepinacom `--dev`, ktory prave zabezpeci, aby sa balik dostal do vyvojarskych zavislosti:

```bash
$ poetry add --dev ipython
```




## Installation

ak nemate systemovy balickovaci system, tak balik nainstalujete prikazom `pip`:

```bash
$ pip install --user poetry
```

je mozne pridat aj podporu pre automaticke doplnanie prikazov vo vasom interpretri prikazoveho riadku

```bash
# Bash
$ poetry completions bash > /etc/bash_completion.d/poetry.bash-completion
```


### Windowsaci a proxy

treba nastavit proxy:

```bash
$ set HTTP_PROXY=http://127.0.0.1:3128
$ set HTTPS_PROXY=%HTTP_PROXY%
```

a potom pofici aj `pip3`

