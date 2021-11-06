---
layout: page
title: My Books
sidebar_link: true
permalink: /books/
---
<style>
.row {
    display: flex;
}

.cover {
    flex: 43%;
}

.info {
    flex: 57%;
}

 /* Style buttons */
 .btn {
    background-color: DodgerBlue;
    border: none;
    color: white;
    padding: 8px 20px;
    cursor: pointer;
    font-size: 20px;
    border-radius: 5px;
    width: 120px;
    font-size: large;
 }

 /* Darker background on mouse-over */
 .btn:hover {
    background-color: RoyalBlue;
 } 

 /* book's meta information */
 .meta {
    font-size: small;
 }
</style>

I wrote few books. Mostly in Slovak language.

{% assign books = site.books | sort: "year" | reverse  %}

{% for book in books %}

<div class="row">
    <div class="cover">
        <img src="../images/{{ book.cover }}" alt="{{ book.title }}" />
    </div>
    <div class="info">
        <h2>{{ book.title }}</h2>
        <p class="meta">
            <b>{{ book.authors }}</b>, 
            {{ book.year }},
            ISBN: {{ book.formats[0].isbn }},
            {{ book.formats[0].pages }} strán
        </p>

        <p>
            {{ book.content }}
        </p>

        {% for format in book.formats %}
            <a href="{{ format.url }}">
             <button class="btn"><i class="fa fa-download"></i> {{ format.format | upcase }}</button>
             </a>&nbsp;
        {% endfor %}
    </div>
</div>
<hr/>

{% endfor %}

