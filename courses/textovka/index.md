---
layout: default
title: Python Textovka
courseid: pytx
---
{% assign lectures = site.pages | where: "courseid", page.courseid | where: 'layout', 'lecture' | sort: "order" %}

## TOC

{% for lecture in lectures %}

1. **[{{ lecture.title }}]({{ lecture.url }})**

   {{ lecture.description }}

{% endfor %}

## Todo

* pridat linku na indiana jonesa rovno, aby sa mohli zahrat aj oni sami: https://spectrumcomputing.co.uk/playonline.php?eml=2&downid=140892

* po vytvoreni batohu miesto prikazu vezmi, spravit prikaz poloz
  * netreba v nom testovat, ci je batoh plny ani to, ci sa da predmet vziat
