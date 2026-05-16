window.addEventListener("DOMContentLoaded", function () {
  var mapElement = document.getElementById("map");

  if (!mapElement || typeof L === "undefined") {
    return;
  }

  var map = L.map("map").setView([15.0, 20.0], 2);

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  var stations = Array.from(document.getElementsByClassName("station"));

  function scrollToElement(element) {
    stations.forEach(function (station) {
      station.classList.remove("bg-lawsafrica-pale-red");
    });

    element.classList.add("bg-lawsafrica-pale-red");

    var rect = element.getBoundingClientRect();
    var targetPosition = Math.floor(rect.top - element.offsetTop - element.offsetHeight);
    window.scrollTo({
      top: targetPosition,
      behavior: "smooth",
    });
  }

  stations.forEach(function (station) {
    var marker = L.marker(station.dataset.coords.split(",")).addTo(map);
    station.classList.remove("bg-lawsafrica-pale-red");
    marker.on("click", function () {
      scrollToElement(station);
    });
  });
});
