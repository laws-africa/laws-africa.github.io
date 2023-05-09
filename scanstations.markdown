---
title: Scan Stations
lead: Laws.Africa's world-wide information digitisation network.
layout: simple
stations:
- name: Scan Station Cape Town
  location: Cape Town, South Africa
  launch_date: 2019-01-01
  coords: -33.9576164, 18.4629253

- name: Scan Station Berlin
  location: Berlin, Germany
  launch_date: 2023-01-12
  coords: 52.5065133, 13.1445545

map_js:
- <script defer src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
- |-
  <script defer>
    var map = L.map('map').setView([15.1021, -40.2812], 2);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    const stations = Array.from(document.getElementsByClassName('station'))

    function scrollToElement (element) {
      stations.forEach(station => {
        station.classList.remove('bg-lawsafrica-pale-red')
      })
      element.classList.add('bg-lawsafrica-pale-red');
      const rect = element.getBoundingClientRect();
      const targetPosition = Math.floor(rect.top - element.offsetTop - element.offsetHeight);
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }

    stations.forEach(station => {
      var marker = L.marker(station.dataset.coords.split(',')).addTo(map)
      station.classList.remove('bg-lawsafrica-pale-red')
      marker.on('click', function () {
        scrollToElement(station)
      });
    })
  </script>
---

<div>
  <header class="py-5 bg-lawsafrica-pale-red">
    <div class="container">
      <h1 class="display-4 mb-4">{{ page.title }}</h1>
      <p class="lead">
        Our Scan Stations are a world-wide network of digitisation centers. Our expert staff and partners collect, scan and digitise African legal information including judgments, legislation, gazettes and law reports.
      </p>
    </div>
  </header>

  <div id="map"></div>

  <section class="py-5">
    <div class="container">
    <div class="row justify-content-center">
      {% for station in page.stations %}
        <div class="col-sm-6">
          <div class="card mb-2 station" data-coords="{{ station.coords }}">
            <div class="card-body">
              <h5 class="card-title">{{ station.name }}</h5>
              <div class="card-text"><b>Location:</b> {{ station.location }}</div>
              <div class="card-text"><b>Launch date:</b> {{ station.launch_date }}</div>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
    </div>
  </section>
</div>
