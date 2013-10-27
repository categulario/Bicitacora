$(document).on("ready",cargar(inicializar));
$(document).on("ready",getRuta);
function inicializar (posicion) {

}

function getRuta () {
  $.ajax({
    dataType: 'json',
    type: 'get',
    url: '/api/r/rutas',
    success: function(rutas){
    	dibujarRutas(rutas);
    }
  });
}

function dibujarRutas(rutas){
	colors = ['#FF0000','#00FF00', '#0000FF'];
  	for (i in rutas){
  		ruta = [];
  		puntos = rutas[i].puntos;
  		for ( punto in puntos){
  			lat = puntos[punto].latitud;
  			lng = puntos[punto].longitud;
  			ruta.push(new google.maps.LatLng(lat,lng));

  		}
	  	new google.maps.Polyline({
	    	path: ruta,
	    	strokeColor: colors[i],
	    	strokeOpacity: 1.0,
	    	strokeWeight: 2,
	    	map: map
	  	});
  	}

}