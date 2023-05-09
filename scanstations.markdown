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
map_js:
- <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
- |-
  <script>
    var map = L.map('map').setView([0.1021, -40.2812], 3);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    const coords = Array.from(document.getElementsByClassName('station-coords'))

    function scrollToElement (element) {
      coords.forEach(coord => {
        coord.offsetParent.classList.remove('highlight-background')
      })
      element.offsetParent.classList.add('highlight-background');
        const rect = element.getBoundingClientRect();
        const targetPosition = Math.floor(rect.top - element.offsetTop - element.offsetHeight);
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
    }

    coords.forEach(coord => {
      var marker = L.marker(coord.textContent.split(', ')).addTo(map)
      coord.classList.remove('highlight-background')
      marker.on('click', function () {
        scrollToElement(coord)
      });
    })
  </script>
---

<div>
  <header class="py-5 bg-lawsafrica-pale-red">
    <div class="container">
      <h1 class="display-4 mb-4">{{ page.title }}</h1>
      <p class="lead">
        {{ page.lead }}
      </p>
    </div>
  </header>

  <div id="map"></div>

  <section class="py-5">
    <div class="container">
    <div class="row justify-content-center">
      {% for station in page.stations %}
        <div class="card col mx-2">
        <div class="card-body">
          <h5 class="card-title">{{ station.name }}</h5>
          <div class="card-text"><b>Location:</b> {{ station.location }}</div>
          <div class="card-text"><b>Launch Date:</b> {{ station.launch_date }}</div>
          <div class="card-text"><b>Coordinates:</b> <span class="station-coords">{{ station.coords }}</span></div>
        </div>
        </div>
      {% endfor %}
    </div>
    </div>
  </section>
</div>
