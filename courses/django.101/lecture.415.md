---
title: Views Testing
courseid: django101
order: 415
layout: lecture
---

## Using the `client`

```python
import pytest

from django.urls import reverse


def test_view(client):
    url = reverse('files:homepage')
    response = client.get(url)
    assert response.status_code == 200
```


## Using the `admin_client`

```python
def test_superuser_view(admin_client):
    url = reverse('files:list-files')
    response = admin_client.get(url)
    assert response.status_code == 200
```


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 24

* [Pytest Django](https://pytest-django.readthedocs.io/en/latest/)

* Namakaný webinár #39: [Základy testovania v jazyku Python s rámcom pytest (nie len) pre učiteľov](http://namakanyden.sk/webinars/2022.09-pytest.101.html)

* [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/)

* [Obey the Testing Goat!](https://www.obeythetestinggoat.com/)

