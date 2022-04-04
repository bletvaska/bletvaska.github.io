---
layout: default
title: Microservices with FastAPI
description: |
    About microservices written in FastAPI.
courseid: fastapi
---
{% assign lectures = site.pages | where: "courseid", page.courseid | where: 'layout', 'lecture' | sort: "order" %}

{% assign slides = site.pages | where: "courseid", page.courseid | where: 'layout', 'slide' | sort: "order" %}

# {{ page.title }}

{{ page.description }}

[slides]({{ slides[0].url }})

Project Github: [https://github.com/bletvaska/fishare](https://github.com/bletvaska/fishare)

## TOC

{% for lecture in lectures %}

1. **[{{ lecture.title }}]({{ lecture.url }})**

   {{ lecture.description }}

{% endfor %}


## Additional 

### REST Best Practices

* https://medium.com/@mwaysolutions/10-best-practices-for-better-restful-api-cbe81b06f291
* https://florimond.dev/en/posts/2018/08/restful-api-design-13-best-practices-to-make-your-users-happy/
* https://www.partech.nl/nl/publicaties/2020/07/9-trending-best-practices-for-rest-api-development#
* https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
* [FastAPI - A python framework | Full Course](https://www.youtube.com/watch?v=7t2alSnE2-I) - sice nepomenuva dobre endpointy a par dalsich veci, ale par inych veci sa da odkukat
