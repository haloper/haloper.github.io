$(function(){
	main.eventBinding();
	$("#answer").hide();
	source.init().then(function() {
		main.load()
	});
	
});


var main = {
		eventBinding: function() {
			$("#check").bind("click", this.check);
			$("#next").bind("click", this.next);
			$("#reload").bind("click", this.reload);
		},
		check: function(event) {
			$("#answer").show();
		},
		next: function(event) {
			$("#answer").hide();
			var data = source.next();
			$("#question").html(data.question);
			$("#answer").html(data.answer);
			if(data.keyword) {
				$("#keyword").html(data.keyword);
				$("#keyword").parent().show();
			}
			else {
				$("#keyword").parent().hide();
			}
			$("#text").val("");
		},
		load: function(event) {
			source.load({keyword: "have"}).then(function() {
				main.next();
				$("#total").text(source.length);
			});
		}
	};
