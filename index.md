---
layout: index
title: My Homepage
---

![Mirek na Hackathone](images/mirek.na.hackathone.jpg)

Yes, that's me. Welcome to my homepage.

## Latest Talks

{% assign slides = site.pages | where: "layout", "slide" | where: "categories", "talk" | sort: "date" | reverse | slice: 0, 3 %}

{% for item in slides %}
* [{{ item.title }}]({{ item.url }})
{% endfor %}

