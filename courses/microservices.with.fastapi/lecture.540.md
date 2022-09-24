---
title: Building a Docker Image
courseid: fastapi
order: 530
layout: lecture
description: |
    ako zabalit aplikaciu do obrazu
---

## Alpine Linux

```dockerfile
# UPOZORNENIE!!!
# nebal svoje python aplikacie do kontajnerov zalozenych na alpine linuxe!!!!!

FROM alpine AS builder
LABEL mainter="mirek <mirek@cnl.sk>"

RUN apk add \
    py3-pip \
    gcc \
    python3-dev \
    musl-dev \
    alpine-sdk \
    && mkdir /wheels

COPY dist/fishare-0.1.0-py3-none-any.whl /wheels/

RUN pip install wheel \
    && pip wheel --wheel-dir=/wheels/ \
       /wheels/fishare-0.1.0-py3-none-any.whl


FROM alpine AS base
LABEL mainter="mirek <mirek@cnl.sk>"

COPY --from=builder /wheels/*whl /tmp/

RUN apk add py3-pip \
    && cd /tmp/ \
    && pip install *whl \
    && pip cache purge \
    && rm -rf *whl \
    && mkdir -p /app/storage

EXPOSE 8000
VOLUME /app/storage

WORKDIR /app

CMD [ "fishare" ]
```


## Finalny obraz zalozeny na Python obraze

```dockerfile
FROM python:3.10-slim
LABEL maintainer="mirek <mirek@cnl.sk>"

RUN adduser --no-create-home --disabled-password --gecos "" appuser

COPY dist/fishare-0.9.0-py3-none-any.whl /tmp/

RUN pip install /tmp/fishare-0.9.0-py3-none-any.whl httpie \
    && pip cache purge \
    && rm /tmp/*whl \
    && mkdir -p /app/storage \
    && chown -R appuser.appuser /app \
    && apt update && apt install -y curl \
    && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
    CMD http get http://localhost:8000/health/ --check-status || exit 1

USER appuser
WORKDIR /app

EXPOSE 8000
VOLUME /app/storage/

CMD [ "fishare" ]
```

