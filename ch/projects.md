---
layout: page
title: 项目
permalink: /ch/projects/
description:
nav: true
nav_order: 3
display_categories: [work, fun]
horizontal: false
lang: zh
---

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  <!-- Filter for Chinese projects -->
  {% assign categorized_projects = site.projects | where: "category", category | where: "lang", "zh" %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  
  <!-- Check if there are any Chinese projects in this category -->
  {% if sorted_projects.size > 0 %}
    <!-- Generate cards for each project -->
    {% if page.horizontal %}
    <div class="container">
      <div class="row row-cols-1 row-cols-md-2">
      {% for project in sorted_projects %}
        {% include projects_horizontal.liquid %}
      {% endfor %}
      </div>
    </div>
    {% else %}
    <div class="row row-cols-1 row-cols-md-3">
      {% for project in sorted_projects %}
        {% include projects.liquid %}
      {% endfor %}
      </div>
    {% endif %}
  {% else %}
   <p>暂无中文详细介绍。</p>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->
<!-- Filter for Chinese projects -->
{% assign sorted_projects = site.projects | where: "lang", "zh" | sort: "importance" %}

  {% if sorted_projects.size > 0 %}
    <!-- Generate cards for each project -->
    {% if page.horizontal %}
      <div class="container">
        <div class="row row-cols-1 row-cols-md-2">
        {% for project in sorted_projects %}
          {% include projects_horizontal.liquid %}
        {% endfor %}
        </div>
      </div>
    {% else %}
      <div class="row row-cols-1 row-cols-md-3">
        {% for project in sorted_projects %}
          {% include projects.liquid %}
        {% endfor %}
      </div>
    {% endif %}
  {% else %}
      <p>暂无中文详细介绍，请切换至英文版查看。</p>
  {% endif %}
{% endif %}
</div>
