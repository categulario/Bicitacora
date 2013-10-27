
function cargar(funcion) {
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
    funcion(e.latLng);
  });    
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




