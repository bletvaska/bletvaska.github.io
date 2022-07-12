---
title: DRF - Hyperlinked View
courseid: django101
order: 325
layout: lecture
---


## Hyperlinked View

obsahuje polozku `url` s adresou na detail prvku


## Hyperlinked Serializer

```python
class FileHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'size', 'downloads', 'url']
        extra_kwargs = {
            'url': {'view_name': 'files:file-detail', 'lookup_field': 'slug'}
        }
```

bude treba samozrejme aktualizovat pohlad `FileListAPIView`, kde upravime clensku premennu `serializer`:

```python
class FileListAPIView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileHyperlinkedSerializer
    lookup_field = 'slug'
```


## Detail View

```python
class FileDetailAPIView(RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileHyperlinkedSerializer
    lookup_field = 'slug'
```


## Aktualizacia smerovaca

```python
path('api/<str:slug>', FileDetailAPIView.as_view(), name='file-detail'),
```

## Testovanie

otvorit adresu so zoznamom http://localhost:8000/api/files/ a nasledne kliknut na konkretnu polozku

alebo z prikazoveho riadku

```bash
$ http http://localhost:8000/api/files/
```


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 17

* [Django REST Framework](https://www.django-rest-framework.org/) - domovska stranka projektu

* [Classy Django REST Framework.](https://www.cdrf.co/)
