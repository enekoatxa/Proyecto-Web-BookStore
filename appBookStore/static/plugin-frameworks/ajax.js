$(document).ready(function() {

  $('#contenidoAjax').qtip(
  {
    var href = $(this).attr("href");
    href = href.replace("libros", "ajax");
    content: {
      url: href,
      method: 'get'
   }
  });

});