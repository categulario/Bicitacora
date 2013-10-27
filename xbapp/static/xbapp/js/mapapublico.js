$(document).on("ready",cargar(inicializar));

function inicializar (posicion) {

}

function getRuta () {
  $.ajax({
    dataType: 'json',
    type: 'get',
    url: '/api/r/rutas',
    success: function(json){
      toastr.success('La ruta ha sido guardada', 'Genial :D');
    },error: function(){
      toastr.error('Ha ocurrio un error u.u', 'Oh, no!');
    }
  });
}