---
title: Installation
description: inštalácia, nástroj Poetry, vytvorenie projektu
courseid: fastapi
order: 02
layout: lecture
---

* problem: niekolko nastrojov a procesov na spravu a manazment projektov


## What is Poetry

* Python packaging and dependency management made easy 

* Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.


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


## Vytvorenie projektu

First, let’s create our new project, let’s call it `fishare`:

```bash
$ poetry new fishare
```

ten vytvori strukturu projektu. nas kod  budeme davat do priecinku `fishare/`, popripade, ak ste zvyknuty, ho mozeme premenovat na `app/`.


## Pridanie/nainstalovanie zavislosti

```bash
$ poetry add ipython
```

zobrazenie nainstalovanych balickov:

```bash
$ poetry show
```


## Doinstalovat Poetry do Pycharm-u

treba pridat plugin Poetry do pluginov
