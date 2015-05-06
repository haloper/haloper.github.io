$(function(){
	main.eventBinding();
	$("#answer").hide();
	source.init().then(function() {
		main.load()
	});
	
});


var main = {
		LINKED_WORD_FORMAT: "<a href='http://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query={{keyword}}' target='naver_dictionary'>{{keyword}}</a>",
		eventBinding: function() {
			$("#check").bind("click", this.check);
			$("#next").bind("click", this.next);
			$("#reload").bind("click", this.reload);
			$("#last").bind("click", this.last)
			$("#text").bind("change", this.writing);			
		},
		check: function(event) {
			$("#answer").show();
		},
		next: function(event) {
		 var data = source.next();
			
			$("#answer").hide();
			
			$("#lastAnswer").html("").hide();
			if(localStorage["question" + source.index]) {
							$("#lastAnswer").html(localStorage["question" + source.index]);
							$("#last").show();
			}
			else {
			 			$("#last").hide();
			}

			$("#question").html(main.toLink(data.question));
			$("#answer").html(main.toLinke(data.answer));
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
		},
		writing: function(event) {
					localStorage.setItem("question" + source.index, $("#text").val());
							},
		last: function(event) {
					$("#lastAnswer").show();
		},
		toLink: function(text) {
				var words = text.split(" ");
				var linkedSentence = "";
				for(var i=0;i<words.length;i++) {
					linkedSentence += main.LINKED_WORD_FORMAT.replace(/{{keyword}}/g, words[i]) + " ";
				}
				return linkedSentence.trim();
		}		
	};
