$(document).on("ready",cargar);

var puntos = [];
var ruta = null
function cargar() {
    var myOptions = {
   		zoomControlOptions: {
      		style: google.maps.ZoomControlStyle.llenarComboOrigen
      		},
      	zoom: 14,
      	center: new google.maps.LatLng(19.540649,-96.926408),
      	mapTypeId: google.maps.MapTypeId.HYBRID
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
	google.maps.event.addListener(map, 'click', function(e) {
          agrega_punto(e.latLng);
        });    
}


function agrega_punto(posicion)
{
	marker= new google.maps.Marker({
        position: posicion, 
        map: map
        });
    puntos.push(posicion);
    dibujarPuntos();
}

function dibujarPuntos(){

  if (puntos.length<2)
    return;
  if (ruta == null)
   ruta = new google.maps.Polyline({
    path: puntos,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2,
    map: map
  });
 else{
    
    ruta.setPath(puntos);

 }
}