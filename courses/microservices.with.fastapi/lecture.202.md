---
title: Settings
courseid: fastapi
order: 202
layout: lecture
description: |
    nastavenia
---

## Introduction

```bash
$ poetry add pydantic-dotenv
```


## Model

```python
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    slug_length = 5
    port = 8000
    base_url: AnyHttpUrl = 'http://localhost:8000'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'fishare_'
```
