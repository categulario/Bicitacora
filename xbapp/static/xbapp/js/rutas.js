$(document).on("ready",cargar(agrega_punto));

var puntos = [];
var ruta = null;
var elevaciones = [];
var token;

function agregaElevacion (results,status) {
  if (status == google.maps.ElevationStatus.OK) {
      if (results[0]) {
        elevaciones.push(results[0].elevation);
      }else{
        elevaciones.push(0);
      } 
    }else{
      elevaciones.push(0);
    }
}

function agrega_punto(posicion){
  marker= new google.maps.Marker({
        position: posicion, 
        map: map
        });
  puntos.push(posicion);
  buscaElevacion(posicion);
  dibujarPuntos();
}

function buscaElevacion (punto) {
  elevator = new google.maps.ElevationService();
  elevator.getElevationForLocations({'locations': [punto]}, agregaElevacion);
}

function creaRutaJSON () {
  var ruta = {};
  ruta["hora_inicio"] = null;
  ruta["hora_fin"] = null;
  puntos_b = [];
  for(punto in puntos){
    puntos_b.push({"latitud": puntos[punto].lat,"longitud":puntos[punto].lng, "altitud":elevaciones[punto]});
  }
  ruta["puntos"] = puntos_b;
  ruta["longitud"] = getLongitud();
  ruta["desplazamiento"] = getDesplazamiento();
  return ruta;
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

function getLongitud () {
  distancia = 0;
  for (i = 0; i< puntos.length-1; i++){
    distancia += google.maps.geometry.spherical.computeDistanceBetween(puntos[i], puntos[parseInt(i)+1]);
  }
  return distancia;
}

function getDesplazamiento () {
  return google.maps.geometry.spherical.computeDistanceBetween(puntos[0], puntos[puntos.length-1]);
}

function guardarRuta () {
  $.ajax({
    data: {ruta: creaRutaJSON(), token: token},
    dataType: 'json',
    type: 'post',
    url: '',
    success: function(json){
      toastr.success('La ruta ha sido guardada', 'Genial :D');
    },error: function(){
      toastr.error('Ha ocurrio un error u.u', 'Oh, no!')
    }
  });
}