---
layout: archive
title: "Jottings"
permalink: /jottings/
author_profile: true
---

{% raw %}
A place for my thoughts and reflections.

## All Jottings

<ul>
{% for post in site.jottings reversed %}
  {% include archive-single.html %}
{% endfor %}
</ul>
{% endraw %}