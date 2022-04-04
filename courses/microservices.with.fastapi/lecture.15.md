---
title: URL
courseid: fastapi
order: 15
layout: lecture
---


* path
* query params
* url


![URL Format Explained](images/url.format.explained.png)


## REST API

| path | method | meaning |
| `/`    | `GET` | show homepage |
| `/{key}` | `GET` | download file with given `key` |
| `/files/{key}` | `GET` | get file info as JSON document |
| `/files/{key}` | `DELETE` | delete file with given `key` |
| `/files/` | `POST` | create/upload new file |
| `/files/` | `GET` | return list of files |
| `/cron/` | `GET` | starts maintainance |
| `/users/` | `GET` | retrieve list of users |
| `/users/{user_id}` | `GET` | retrieve info about given user |
| `/users/` | `POST` | create new user |
| `/users/{user_id}` | `DELETE` | delete existing user |
| `/users/me` | `GET` | shows my profile |
