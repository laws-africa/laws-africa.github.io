---
title: Scan Stations
lead: Something about scan stations.
layout: simple
stations:
- name: Scan Station Cape Town
  location: Cape Town, South Africa
  staff: X, Y and Z
  launch_date: 2019-01-01
  coords: 0.123, -25.678
- name: Scan Station Two
  location: A place
  staff: A, B and C
  launch_date: 2022-01-01
  coords: 10.345, -35.678
---

<div>
  <header class="py-5 bg-lawsafrica-pale-red">
    <div class="container">
      <h1 class="display-4 mb-4">foo</h1>
      <p class="lead">
        stuff
      </p>
    </div>
  </header>

  <section class="py-5">
    <div class="container">
    <ul>
      {% for station in page.stations %}
        <li>{{ station.name }}</li>
      {% endfor %}
    </ul>
    </div>
  </section>
</div>
