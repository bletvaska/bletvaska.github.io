---
layout: default
title: My Talks
sidebar_link: true
---

# My Talks

List of my latest talks. Mostly in Slovak language.


{% assign year = 9999 %}
{% assign slides = site.pages | where: "layout", "slide" | where: "categories", "talk" | sort: "date" | reverse  %}

{% for item in slides %}
{% assign item_year = item.date | date: "%Y" | plus: 0 %}

{% if year > item_year %}
{% assign year = item_year %}
## {{ year }}
{% endif %}

{% include talk.html item=item %}

{% endfor %}

