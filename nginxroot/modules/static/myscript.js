$(document).ready(function(){
	$( ".form1" ).on( "submit", function( event ) {
		event.preventDefault();
		var formData = $( this ).serialize();
		console.log(formData)
		var str = "http://127.0.0.1:5000/delete?" + formData
		$.ajax({
			method:"GET",
	        url:str
	    }).done(function(data) {
	        console.log("Response",data);
	 		$("#content").html(data)   
	    });;
	});
});	

