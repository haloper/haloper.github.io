var source = {
		data: [],
		length: -1,
		config: null,
		keywords: [],
		index: 0,
		init: function() {
			return $.ajax({
	            type:"GET",
	            url:"local/config.json"
			}).done(function(json) {
				if(typeof json == "string") {
					source.config = $.parseJSON(json);
				}
				else if(typeof json == "object") {
					source.config = json;
				}
				return new Promise(function(success) {
					success();
				});
			});
		},
		load: function(obj) {
			var keyword = obj.keyword;
			return $.ajax({
				type:"GET",
	            url:source.config.request_url
			}).then(function(txt) {
				var array = txt.trim().split("\n");
				var keyword;
				for(var  i=0;i<array.length;i++) {
					if(array[i] && array[i].trim() != "" && !array[i].trim().startsWith("#")) {
						if(array[i].startsWith("*")) { //Keyword
							keyword = array[i].substring(1);
							source.keywords[source.keywords.length] = keyword;
						}
						else if(array[i].startsWith("@")) { //Question
							source.data[source.data.length] = {
									keyword : keyword,
									question : array[i].substring(1)
							}
						}
						else if(array[i].startsWith("$")) { //Answer
							source.data[source.data.length - 1].answer = array[i].substring(1);
						}
					}
				}
				source.length = source.data.length; 
				source.next();
				return new Promise(function(success) {
					success();
				});
			});
		},
		next: function() {
			source.index = Math.floor(Math.random() * source.length);
			return {
				keyword: source.data[source.index].keyword,
				question: source.data[source.index].question,
				answer: source.data[source.index].answer
			}
		}
}
