---
title: DRF - Quick Start
courseid: django101
order: 310
layout: lecture
---


## Quick Start

vytvorime rychlo REST API pre zoznam suborov. DRF podporuje tiez Class Based Views


## Serializer

* potrebujeme pripravit serializer, ktory z modelu vyberie len prvky, ktore chceme
    * nechceme totiz vsetkym vzdy ukazovat vsetko


```python
# Serializers define the API representation.
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'size', 'downloads']
```


## List View

* teraz uz mozeme vyrobit rovno pohlad, pomocou ktoreho vratime cely zoznam


```python
class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
```


## Router Update

na zaver uz len aktualizujeme smerovac/linky v subore `urls.py` aplikacie `files`

```python
path('api/', views.FileListView.as_view(), name='asdf'),
```


## Browsable API

ak pojdeme s prehliadacom na adresu http://127.0.0.1:8000/files/api/ tak uvidime paradnu vec - prehliadac rest api, resp. jeho klient priamo ako sucast Djanga


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 17

* [Django REST Framework](https://www.django-rest-framework.org/) - domovska stranka projektu

* [Classy Django REST Framework.](https://www.cdrf.co/)
