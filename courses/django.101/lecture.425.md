---
title: Testing REST API
courseid: django101
order: 425
layout: lecture
---

da sa samozrejme pouzit univerzalny modul `requests`, ale _Django REST Framework_ ma vlstneho klienta pre tvorbu REST API.

Najprv vytvorime *fixture*:

```python
import pytest


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()
```


a potom vytvorime test

```python
@pytest.mark.django_db
def test_files_list(api_client):
    url = reverse('files:api-collection')
    response = api_client.get(url)
    assert response.status_code == 200
```


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 24

* [Pytest Django](https://pytest-django.readthedocs.io/en/latest/)

* Namakaný webinár #39: [Základy testovania v jazyku Python s rámcom pytest (nie len) pre učiteľov](http://namakanyden.sk/webinars/2022.09-pytest.101.html)

* [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/)

* [Obey the Testing Goat!](https://www.obeythetestinggoat.com/)

