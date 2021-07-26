---
title: Publications
date: 2021-06-18 11:29:00 +02:00
position: 6
header_class: bg-lawsafrica-pale-red
navbar_item: publications
layout: slim
---

{% assign pubs = site.publications | where: "latest_version", true %}
{% for pub in pubs %}
  <div class="card mb-3">
    <div class="card-body">
      <h3 class="mt-0"><a href="{{ pub.url }}">{{ pub.title }}</a></h3>
      <div class="text-muted">{{ pub.date|date:"%e %b %Y"}}</div>
      <div>{{ pub.lead }}</div>
    </div>
  </div>
{% endfor %}
