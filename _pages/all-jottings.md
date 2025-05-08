---
permalink: /all-jottings/
title: "所有随笔"
excerpt: "所有随笔列表"
author_profile: true
---

<div class="jottings-archive">
  {% assign jottings = site.jottings | sort: 'date' | reverse %}
  {% for jotting in jottings %}
    <div class="jotting-item">
      <h2 class="jotting-title">
        <a href="{{ jotting.url | relative_url }}">{{ jotting.title }}</a>
      </h2>
      <p class="jotting-date">
        <time datetime="{{ jotting.date | date_to_xmlschema }}">{{ jotting.date | date: "%Y年%m月%d日" }}</time>
      </p>
      <div class="jotting-excerpt">
        {{ jotting.content | strip_html | truncate: 200 }}
      </div>
      <p class="jotting-read-more">
        <a href="{{ jotting.url | relative_url }}">阅读全文 &raquo;</a>
      </p>
    </div>
  {% endfor %}
</div> 