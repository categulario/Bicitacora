$(document).on("ready",cargar(agrega_punto));

var punto = null;
var token;

function agrega_punto(posicion){
	if ( punto == null)
 		punto = new google.maps.Marker({
        position: posicion, 
        map: map
        });
 	else
 		punto.setPosition(posicion);

}

function creaLugarJSON () {
  var lugar = {};
  lugar['nombre'] = "";
  lugar['direccion'] ="";
  lugar["latitud"] = 0;
  lugar["longitud"]= 0;
  lugar["altitud"] = 1420;
  lugar["tipo"] = 1;
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