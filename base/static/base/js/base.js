Notification.requestPermission(function(perm) {
	if (perm === "granted") {
		send_alerts();
	}
});

function send_alerts(){
	$(".alert").each(function(){
		$(this).css({'display': 'none'});
		$(this).find('.message').each(function(){
			var notification = new Notification($(this).data('tag'), {
				icon: "icon.png",
				body: $(this).text()
			});
		});
	});
}

$('[data-toggle="tooltip"]').tooltip();

$(function(){
	var url = window.location.origin + "/manager:keyword_detail";
	$.getJSON(url, {"slug":"sdsd"},function(data){
		console.log(data.url);
	});
});