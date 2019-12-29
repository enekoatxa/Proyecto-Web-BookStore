$(document).ready(function() {
	var flag=true;
	$("#tablaLibros").hide();

	$("#btnLibros").click( function () {
		if(flag){
			$("#tablaLibros").show("slow");	
			flag=!flag;
		}
		else{
			$("#tablaLibros").hide("slow");	
			flag=!flag;
		}
	});
	
	$("#portadaLibro").hover( function () {
        $("#portadaLibro").css("height",500);
	}, function (){
		$("#portadaLibro").css("height",400);
	});
});


