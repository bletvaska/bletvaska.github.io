---
title: Downloading File
courseid: django101
order: 212
layout: lecture
---

## Creating a View for Downloading File

```python
def download_file(request, slug: str):
    print(f'>> downloading file {slug}')
    # file = get_object_or_404(File, slug=slug)
    # TODO rozsirit podmienku na kontrolu vyrazu downloads < max_downloads
    file = File.objects.get(slug=slug)

    if file.downloads >= file.max_downloads:
        return HttpResponse('Max downloads reached!', status=404)

    # update downloads
    file.downloads += 1
    file.save()

    # prepare response
    response = HttpResponse(file.file, content_type=file.mime_type)
    response['Content-Disposition'] = f'attachment; filename={file.filename}'

    return response
```


## Updating Routes

najprv vytvorime subor `urls.py` pre aplikaciu `Files`

```python
from fishare.files import views

app_name = 'files'

urlpatterns = [
    path(
        '<str:slug>',
        views.download_file,
        name='download_file'
    )
]
```

no a potom aktualizujeme subor `urls.py` v priecinku `config/` o zaznam:

```python
path('', include('fishare.files.urls')),
```

tym budeme vediet stiahnut rovno subor z adresy http://localhost:8000/\<slug>

