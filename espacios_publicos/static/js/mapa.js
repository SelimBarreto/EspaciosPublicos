function initMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: { lat: 19.432608, lng: -99.133209 }  // Centro de la CDMX
    });

    // Añadir marcador para la instalación deportiva
    const marker = new google.maps.Marker({
        position: { lat: latitud, lng: longitud },  // Variables de latitud y longitud dinámicas
        map: map,
        title: nombre_instalacion
    });
}
