---
layout: default
title: Django 101
description: |
    Simple introduction to Django
courseid: django101
github: https://github.com
---
{% assign lectures = site.pages | where: "courseid", page.courseid | where: 'layout', 'lecture' | sort: "order" %}

{% assign slides = site.pages | where: "courseid", page.courseid | where: 'layout', 'slide' | sort: "order" %}

# {{ page.title }}

{{ page.description }}

[slides]({{ slides[0].url }})

Project Github: [{{ page.github }}]({{ page.github }})

## TOC

{% for lecture in lectures %}

1. **[{{ lecture.title }}]({{ lecture.url }})**

   {{ lecture.description }}

{% endfor %}


## Additional Sources

* [Django Project Homepage](https://www.djangoproject.com/)
* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
* [Awesome Django](https://github.com/wsvincent/awesome-django) - A curated list of awesome things related to Django.


