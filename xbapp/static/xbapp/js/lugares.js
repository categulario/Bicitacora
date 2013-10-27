$(document).on("ready",cargar(agrega_punto));

var punto = null;
var token;
var elevacion = 0;
function agrega_punto(posicion){
	if ( punto == null)
 		punto = new google.maps.Marker({
        position: posicion, 
        map: map,
        icon: "/static/xbapp/images/taller.png"
        });
 	else
 		punto.setPosition(posicion);
    $('#id_latitud').val(posicion.lat());
    $('#id_longitud').val(posicion.lng());
    buscaElevacion(posicion);
}


function buscaElevacion (punto) {
  elevator = new google.maps.ElevationService();
  elevator.getElevationForLocations({'locations': [punto]}, guardaElevacion);
}

function guardaElevacion (results,status) {
  if (status == google.maps.ElevationStatus.OK) {
      if (results[0]) {
        $('#id_altitud').val(results[0].elevation);
      }else{
        $('#id_altitud').val("");
      } 
    }else{
      $('#id_altitud').val("");
    }
}