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
    buscaElevacion(posicion);
}

function creaLugarJSON () {
  posicion = punto.getPosition();
  var lugar = {};
  lugar['nombre'] = $('#id_nombre').val();
  lugar['direccion'] = $('#id_direccion').val();
  lugar["latitud"] = posicion.lat();
  lugar["longitud"]= posicion.lng();
  lugar["altitud"] = elevacion;
  lugar["tipo"] = $('#id_tipo').val();
  return lugar;
}

function guardarLugar (punto) {
  $.ajax({
    data: {ruta: creaLugarJSON(), token: token},
    dataType: 'json',
    type: 'post',
    url: '',
    success: function(json){
     toastr.success('El lugar ha sido guardado', 'Genial :D');
    },
    error: function(){
      toastr.error('Ha ocurrio un error', 'Oh, no!')
    }
  });
}

function buscaElevacion (punto) {
  elevator = new google.maps.ElevationService();
  elevator.getElevationForLocations({'locations': [punto]}, guardaElevacion);
}

function guardaElevacion (results,status) {
  if (status == google.maps.ElevationStatus.OK) {
      if (results[0]) {
        elevacion = results[0].elevation;
      }else{
        elevacion = 0;
      } 
    }else{
      elevacion = 0;
    }
}