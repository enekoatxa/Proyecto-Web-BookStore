$(document).ready(function() {
$('a.contenidoAjax').each(function(){
	var href = $(this).attr("href");
    href = href.replace("libros", "ajax");
    $(this).qtip({
    content: {
      url: href,
      method: 'get'
 	}
  });
}); 
}); 