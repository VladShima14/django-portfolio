$(document).ready(function(){
	$(function() {
		$('.article h2').hover(function() {
			$(this).css('color', '#909090');
		}, function() {
			$(this).css('color', '#010101');
		});
	});

	$(function() {
		$('.description').hover(function() {
			$(this).parent().children('.article h2').css('color', '#909090');
		}, function() {
			$(this).parent().children('.article h2').css('color', '#010101');
		});
	});
}); 