$('document').ready(function (){
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', funtion(data)
	  {
	      $('DIV#hello').text(data.hello);
	  });
});
