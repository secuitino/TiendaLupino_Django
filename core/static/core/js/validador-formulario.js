$(function(){

	//Jquery - Validate

	//version traducida

	jQuery.extend(jQuery.validator.messages, {
  	required: "Este campo es obligatorio.",
  	remote: "Por favor, rellena este campo.",
  	email: "Por favor, escribe una dirección de correo válida",
  	url: "Por favor, escribe una URL válida.",
  	date: "Por favor, escribe una fecha válida.",
  	dateISO: "Por favor, escribe una fecha (ISO) válida.",
  	number: "Por favor, escribe un número entero válido.",
  	digits: "Por favor, escribe sólo dígitos.",
  	creditcard: "Por favor, escribe un número de tarjeta válido.",
  	equalTo: "Por favor, escribe el mismo valor de nuevo.",
  	accept: "Por favor, escribe un valor con una extensión aceptada.",
  	maxlength: jQuery.validator.format("Por favor, no escribas más de {0} caracteres."),
  	minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
  	rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
  	range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
  	max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
  	min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
	});

	//fin version traducida

	var validador = $("#formulario-ingresar-instrumento").validate({

		rules:{
			nombreInstrumento:{
				required:true,
				minlength:3,
				maxlength:80
			}, 
			tipoinstrumento:{
				required:true
			},
			precioinstrumento:{
				required:true,
				number:true,
				min:1
			},
			descripcion:{
				required:true, 
				minlength:5,
				maxlength:200
			},
			stockinstrumento:{
				required:true,
				number:true
			}

		}

	});


	var validador = $("#formulario-Contacto").validate({

		rules:{
			nombreContacto:{
				required:true,
				minlength:3,
				maxlength:80,
				remote:true
			}, 
			emailContacto:{
				required:true,
				email: true
			},
			telefonoContacto:{
				required:true,
				number:true,
			},
			mensajeContacto:{
				required:true, 
				minlength:10,
				maxlength:200
			},
		
		}

	});


	$("#btnSubirInstrumento").click(function(){

		if(validador.form()){

		}

	}); 

	$("#btnEnviar-contacto").click(function(){

		if(validador.form()){

		}

	}); 



}); 
