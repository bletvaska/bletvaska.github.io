---
layout: default
title: My Talks
sidebar_link: true
---

# My Talks

{% assign year = 9999 %}
{% assign slides = site.pages | where: "layout", "slide" | where: "categories", "talk" | sort: "date" | reverse  %}

{% for item in slides %}
{% assign item_year = item.date | date: "%Y" | plus: 0 %}

{% if year > item_year %}
{% assign year = item_year %}
## {{ year }}
{% endif %}

<div>
<b><a href="{{ item.url }}">{{ item.title }}</a></b> (<a href="{{ item.event.url }}">{{ item.event.title }}</a>) 

<p>{{ item.description }}</p>
</div>

{% endfor %}

