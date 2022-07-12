---
title: DRF - Organization of API in Project Structure
courseid: django101
order: 315
layout: lecture
---


## Project Structure

teraz sa nam miesaju normalne pohlady s tymi, ktore reprezentuju REST API. podla odporucania Two Scoops of Django je dobre pre REST API urobit samostatny balik, ktory bude sucastou nasej aplikacie. je to dobre z dovodu prilisnej komplexnosti REST API, ktorym sa moze stat.

iny pristup by mohol predstavovat urobit z modulu `views.py` balik s nazvom `views` a do neho jednotlive pohlady vytvorit vo forme samostatnych modulov.


vytvorime teda samostatny balik s nazvom `api` v nasej aplikacii s touto strukturou:

```
api
├── __init__.py
├── serializers.py
└── views.py
```

pre nase potreby zatial potrebujeme modul pre serializery a pre pohlady. samozrejme s rastucimi potrebami budu aj moduly v tomto baliku rast, napriklad:

    * `authentication.py`
    * `parsers.py`
    * `permissions.py`
    * `renderers.py`
    * `validators.py`
    * `viewsets.py`


## Refactoring

do uvedenych modulov presunieme kody, ktore mame uz napisane


### Modul `serializers.py`

```python
from rest_framework import serializers

from ..models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'size', 'downloads']
```


### Modul `views.py`

```python
from rest_framework.generics import ListAPIView

from ..models import File
from .serializers import FileSerializer


class FileListAPIView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
```


### Modul `urls.py`

potrebujeme aktualizovat aj adresy

```python
from .api.views import FileListAPIView

urlpatterns = [
    path('api/', FileListAPIView.as_view(), name='rest-api'),
]
```



## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 17

* [Django REST Framework](https://www.django-rest-framework.org/) - domovska stranka projektu

* [Classy Django REST Framework.](https://www.cdrf.co/)
