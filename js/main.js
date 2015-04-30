$(function(){
	events.binding();
	$("#answer").hide();
	source.init().then(function() {
		load();
	});
	
});

function load() {
	source.load({keyword: "have"}).then(function() {
		next();
	});
}

function next() {
	$("#answer").hide();
	var data = source.next();
	$("#question").html(data.question + (data.keyword ? " (Keyword : " + data.keyword + ")" : "") );
	$("#answer").html(data.answer);
}

var events = {
		binding: function() {
			$("#check").bind("click", this.clickCheck);
			$("#next").bind("click", this.clickNext);
			$("#reload").bind("click", this.clickReload);
		},
		clickCheck: function(event) {
			$("#answer").show();
		},
		clickNext: function(event) {
			next();
		},
		clickReload: function(event) {
			load();
		}
	};
