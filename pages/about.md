---
layout: page
title: About
permalink: /about/
weight: 3
---

# **About Me**

Hi, I am **{{ site.author.name }}**.<br>
I built this site to present my work in software engineering, data visualization, and web development.

My recent work here focuses on turning datasets into clear, interactive explanations using Python, Altair, Vega-Lite, and HTML. I am especially interested in projects where code and communication matter equally: cleaning data, shaping a visual story, and then shipping it as a usable web page.

<div class="row">
{% include about/skills.html title="Programming Skills" source=site.data.programming-skills %}
{% include about/skills.html title="Other Skills" source=site.data.other-skills %}
</div>

<div class="row">
{% include about/timeline.html %}
</div>
