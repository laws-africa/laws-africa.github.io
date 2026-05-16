---
title: Scan Stations
lead: Laws.Africa's world-wide information digitisation network.
stations:
- name: Scan Station Accra
  location: Accra, Ghana
  coords: 5.6037, -0.1870
- name: Scan Station Berlin
  location: Berlin, Germany
  launch_date: 2023
  coords: 52.5065133, 13.1445545
- name: Scan Station Cape Town
  location: Cape Town, South Africa
  launch_date: 2019
  coords: -33.9576164, 18.4629253
- name: Scan Station Dar es Salaam
  location: Dar es Salaam, Tanzania
  launch_date: null
  coords: -6.7924, 39.2083
- name: Scan Station Johannesburg
  location: Johannesburg, South Africa
  launch_date: null
  coords: -26.2041, 28.0473
- name: Scan Station Kampala
  location: Kampala, Uganda
  launch_date: null
  coords: 0.3476, 32.5825
- name: Scan Station Lagos
  location: Lagos, Nigeria
  launch_date: null
  coords: 6.5244, 3.3792
- name: Scan Station Lilongwe
  location: Lilongwe, Malawi
  launch_date: null
  coords: -13.9626, 33.7741
- name: Scan Station Lusaka
  location: Lusaka, Zambia
  launch_date: null
  coords: -15.3875, 28.3228
- name: Scan Station Mauritius
  location: Mauritius
  launch_date: null
  coords: -20.3484, 57.5522
- name: Scan Station Montréal
  location: Montréal, Canada
  launch_date: null
  coords: 45.5017, -73.5673
- name: Scan Station Victoria
  location: Victoria, Seychelles
  launch_date: null
  coords: -4.6191, 55.4513
map_js:
- <script defer src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
  crossorigin=""></script>
- "<script defer>\n  var map = L.map('map').setView([15.0, 20.0], 2);\n\n  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',\
  \ {\n    maxZoom: 19,\n    attribution: '&copy; <a href=\"http://www.openstreetmap.org/copyright\"\
  >OpenStreetMap</a>'\n  }).addTo(map);\n\n  const stations = Array.from(document.getElementsByClassName('station'))\n\
  \n  function scrollToElement (element) {\n    stations.forEach(station => {\n  \
  \    station.classList.remove('bg-lawsafrica-pale-red')\n    })\n    element.classList.add('bg-lawsafrica-pale-red');\n\
  \    const rect = element.getBoundingClientRect();\n    const targetPosition = Math.floor(rect.top\
  \ - element.offsetTop - element.offsetHeight);\n    window.scrollTo({\n      top:\
  \ targetPosition,\n      behavior: 'smooth'\n    });\n  }\n\n  stations.forEach(station\
  \ => {\n    var marker = L.marker(station.dataset.coords.split(',')).addTo(map)\n\
  \    station.classList.remove('bg-lawsafrica-pale-red')\n    marker.on('click',\
  \ function () {\n      scrollToElement(station)\n    });\n  })\n</script>"
header_class: bg-lawsafrica-pale-red
slug: scanstations
save_as: scanstations.html
url: /scanstations.html
template: scanstations
---
