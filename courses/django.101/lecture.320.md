---
title: DRF - Pagination
courseid: django101
order: 320
layout: lecture
---


## Pagination

strankovanie je sikovne pre dlhsie zoznamy, pretoze nechceme, aby si pouzivatel stiahol vzdy vsetky polozky. je praktickejsie mu cely zoznam strankovat po castiach


na zabezpecenie strankovania nam staci len aktualizovat nastavenie v subore `config/settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```


## Testing

ak si teraz otvorime zasa REST API prehliadac na adrese http://127.0.0.1:8000/files/api/ , uvidime vystup nie vo forme zoznamu, ale objektu, ktory v sebe obsahuje zoznam vysledkov:

```python
{
    "count": 10,
    "next": "http://127.0.0.1:8000/files/api/?format=api&page=2",
    "previous": null,
    "results": [
        {
            "filename": "rpi.jpg",
            "size": 1613940,
            "downloads": 1
        },
        ...
    ]
}
```


## Additional Links

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 17

* [Django REST Framework](https://www.django-rest-framework.org/) - domovska stranka projektu

* [Classy Django REST Framework.](https://www.cdrf.co/)
