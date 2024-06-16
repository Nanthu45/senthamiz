// Initialize the map and set its view
var map = L.map('mapid').setView([20.5937, 78.9629], 4); // Centered on India, zoom level 4

// Define tile layers
var osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
var esriLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}');
var terrainLayer = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png');
var satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}');

// Add the initial tile layer to the map
map.addLayer(satelliteLayer);

// Define base layers for the layer control
var baseLayers = {
    "OpenStreetMap": osmLayer,
    "Esri Street Map": esriLayer,
    "OpenTopoMap": terrainLayer,
    "Esri Satellite": satelliteLayer
};

// Add the layer control to the map
L.control.layers(baseLayers).addTo(map);

// Retrieve latitude, longitude, and popup content from HTML data attributes
var markerElement = document.getElementById('marker');
var lat = parseFloat(markerElement.dataset.lat);
var lon = parseFloat(markerElement.dataset.lon);
var address = markerElement.dataset.address;
var popupContent = markerElement.innerHTML; // Use the hidden content for the popup

if (!isNaN(lat) && !isNaN(lon)) {
    // Set the map view to the marker's coordinates and zoom level 10
    map.setView([lat, lon], 10);

    // Create a marker with a popup
    var marker = L.marker([lat, lon]).addTo(map)
        .bindPopup(popupContent)
        .openPopup(); // Open the popup by default
}

// ***************************************************************


                                                            // Reload Map to India

var reloadButton = L.Control.extend({
    options: {
        position: 'topright' 
    },
    onAdd: function (map) {
        var container = L.DomUtil.create('div', 'reload-button');
        var button = L.DomUtil.create('button', '', container);
        button.innerHTML = 'Reload Map';
        button.style.fontSize = '12px'; // Adjust the font size
        button.style.padding = '4px 8px'; // Adjust the padding
        
        // Send the button to the back
        container.style.zIndex = '1000'; // Set a high z-index to ensure it's behind other elements

        L.DomEvent.on(button, 'click', function () {
            map.setView([20.5937, 78.9629], 4); 
        });
        return container;
    }
});
map.addControl(new reloadButton());


// *********************************************************************













































  
