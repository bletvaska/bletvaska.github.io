---
title: Database Testing
courseid: django101
order: 415
layout: lecture
---

## The `django_db` mark


```python
import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1
```



## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 24

* [Pytest Django](https://pytest-django.readthedocs.io/en/latest/)

* Namakaný webinár #39: [Základy testovania v jazyku Python s rámcom pytest (nie len) pre učiteľov](http://namakanyden.sk/webinars/2022.09-pytest.101.html)

* [Testing Your Django App With Pytest](https://djangostars.com/blog/django-pytest-testing/)

* [Obey the Testing Goat!](https://www.obeythetestinggoat.com/)

