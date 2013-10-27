$(document).on("ready",cargar);

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

function cargar() {
  //getToken();
  var myOptions = {
   	zoomControlOptions: {
      style: google.maps.ZoomControlStyle.llenarComboOrigen
    },
    zoom: 14,
    center: new google.maps.LatLng(19.540649,-96.926408),
    mapTypeId: google.maps.MapTypeId.HYBRID
  };
  map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
	google.maps.event.addListener(map, 'click', function(e) {
    agrega_punto(e.latLng);
  });    
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

function getToken () {
  $.ajax({
    dataType: 'json',
    type: 'post',
    url: 'api/token',
    success: function(json){
      token = json;
      }
  });
}

function guardarLugar (punto) {
    $.ajax({
    data: {ruta: creaLugarJSON(), token: token}
    dataType: 'json',
    type: 'post',
    url: '',
    success: function(json){
     console.log(json);
    }
  });
}

function guardarRuta () {
  $.ajax({
    data: {ruta: creaRutaJSON(), token: token}
    dataType: 'json',
    type: 'post',
    url: '',
    success: function(json){
     console.log(json);
    }
  });
}



