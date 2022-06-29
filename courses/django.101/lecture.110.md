---
title: Creating Apps
courseid: django101
order: 110
layout: lecture
---

## The Django and the Apps

A Django project is a web application powered by the Django web framework.

Django apps are small libraries designed to represent a single aspect of a project. A Django project is made up of many Django apps. Some of those apps are internal to the project and will never be reused; others are third-party Django packages.


## The Golden Rule of Django App Design

James Bennett is a Django core developer. He taught us everything that we know about
good Django app design. We quote him:

> “The art of creating and maintaining a good Django app is that it should follow the truncated Unix philosophy according to Douglas McIlroy: ‘Write programs that do one thing and do it well.”’


## Naming the Apps

* nazov by mal byt jednoduchy, ako napriklad `blog`, `polls`, `users` a pod

* mnozne cislo miesto jednotneho, aj ked samozrejme budu existovat vynimky
    * podobne ako pri REST API

* niekde sa da stretnut s postfixom `_app`, aby bolo zrejme, ze sa jedna o aplikaciu


## Size of the Apps

Try and keep your apps small. Remember, it’s better to have many small apps than to have
a few giant apps.


## Additional Resources

* [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) - kapitola c. 4

