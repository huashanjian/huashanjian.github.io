---
permalink: /resources/
title: "Resources"
description: "Open materials, talks, and teaching artifacts by Junhua Yao."
excerpt: "Public-facing resources, talks, and notes."
layout: editorial
kicker: "Open materials"
lede: "Slides, teaching artifacts, and public notes for readers who want accessible entry points into embodied intelligence and world models."
---

{% assign home = site.data.home %}

<div class="editorial-copy">
  <p>I treat public materials as part of the research loop. If an idea cannot be explained clearly to a curious reader, it is often not ready for stronger claims either.</p>
  <p>This page collects the public-facing materials I am building while my formal research profile is still taking shape.</p>
</div>

<div class="resource-grid resource-grid--featured">
  {% for item in home.resources.items %}
    <article class="resource-card">
      <div class="resource-card__preview resource-card__preview--soft">
        <p>{{ item.preview }}</p>
        <strong>{{ item.audience }}</strong>
      </div>
      <div class="resource-card__body">
        <p class="stack-card__eyebrow">{{ item.type }}</p>
        <h2>{{ item.title }}</h2>
        <p>{{ item.description }}</p>
        <div class="button-row button-row--compact">
          {% for link in item.links %}
            {% if link.external %}
              {% assign resource_page_href = link.url %}
            {% else %}
              {% assign resource_page_href = link.url | relative_url %}
            {% endif %}
            <a
              class="button-link button-link--ghost"
              href="{{ resource_page_href }}"
              {% if link.external %}target="_blank" rel="noopener noreferrer"{% endif %}
            >
              {{ link.label }}
            </a>
          {% endfor %}
        </div>
      </div>
    </article>
  {% endfor %}
</div>

<section class="editorial-subsection">
  <p class="section-kicker">Featured outputs</p>
  <h2>Work that already exists in public</h2>

  <div class="resource-grid">
    {% for item in home.featured_outputs %}
      <article class="resource-card">
        <div class="resource-card__preview">
          <p>{{ item.type }}</p>
          <strong>{{ item.status }}</strong>
        </div>
        <div class="resource-card__body">
          <h3>{{ item.title }}</h3>
          <p>{{ item.description }}</p>
          <div class="button-row button-row--compact">
            {% for link in item.links %}
              {% if link.external %}
                {% assign output_page_href = link.url %}
              {% else %}
                {% assign output_page_href = link.url | relative_url %}
              {% endif %}
              <a
                class="button-link button-link--ghost"
                href="{{ output_page_href }}"
                {% if link.external %}target="_blank" rel="noopener noreferrer"{% endif %}
              >
                {{ link.label }}
              </a>
            {% endfor %}
          </div>
        </div>
      </article>
    {% endfor %}
  </div>
</section>
