$(function(){
	main.eventBinding();
	$("#answer").hide();
	reloadingSource();
	
});

function reloadingSource(config) {
	source.init(config).then(function() {
		main.load()
	});
}


var main = {
		LINKED_WORD_FORMAT: "<a href='http://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query={{keyword}}' target='naver_dictionary'>{{keyword}}</a>",
		GOOGLE_TRANSLATE: "https://translate.google.co.kr/#en/ko/",
        IMAGE_SEARCH: "<a href='https://www.google.co.kr/search?q={{keyword}}&newwindow=1&source=lnms&tbm=isch&sa=X' target='google_image'>Image</a>",
        position : '',
		eventBinding: function() {
			$("#check").bind("click", this.check);
			$("#next").bind("click", this.next);
			$("#reload").bind("click", this.reload);
			$("#last").bind("click", this.last)
			$("#text").bind("change", this.writing);
			$("#sourceSelect").bind("change", this.sourceChange);
            $("#changePosition").bind("click", this.changePosition);
		},
		check: function(event) {
			$("#answer").show();
            $("#image").show();
		},
        changePosition: function(event) {
            if(main.position != 'reverse') {
                main.position = 'reverse';
            }
            else {
                main.position = '';
            }
            localStorage['position'] = main.position;
        },
		next: function(event) {
			var data = source.next();
			
			$("#answer").hide();
            $("#image").hide();
			
			$("#lastAnswer").html("").hide();
			if(localStorage["question" + source.index]) {
				$("#lastAnswer").html(localStorage[$("#sourceSelect").val() + source.index]);
				$("#last").show();
			}
			else {
				$("#last").hide();
			}
			
			$("#question").html(main.toLink(main.position != 'reverse' ? data.question : data.answer));
			$("#answer").html(main.toLink(main.position != 'reverse' ? data.answer : data.question));
            $("#image").html(main.IMAGE_SEARCH.replace(/{{keyword}}/g, data.answer.trim()));
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
                main.position = localStorage['position'];
				main.next();
				$("#total").text(source.length);
			});
		},
		writing: function(event) {
			localStorage.setItem($("#sourceSelect").val() + source.index, $("#text").val());
			$("#googleTrans").attr("href", main.GOOGLE_TRANSLATE + encodeURI($("#text").val()));
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
		},
		sourceChange: function(event) {
			reloadingSource($("#sourceSelect").val());
		}
	};
