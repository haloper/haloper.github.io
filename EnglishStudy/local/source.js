var source = {
		data: [],
		length: -1,
		config: null,
		keywords: [],
		index: 0,
		init: function(url) {
			if(!url) {
				url = "local/word.json";
			}
			return $.ajax({
	            type:"GET",
	            url:url
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
			}).fail(function(data, error) {
                alert(error);
            });

		},
		load: function(obj) {
			source.data = [];
			source.keywords = [];
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
							var answer = array[i].substring(1);
							for(var j=source.data.length - 1;j>=0;j--) {
								if(!source.data[j].answer) {
									source.data[j].answer = answer;
								}
								else {
									break;
								}
							}
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
			if(source.config.orderby === "asc") {
				if(++source.index >= source.length) source.index = 0;
			}
			else if(source.config.orderby === "desc") {
				if(--source.index < 0) source.index = source.length - 1;
			}
			else {
				source.index = Random(1, source.length - 1, 2);
			}
			return {
				keyword: source.data[source.index].keyword,
				question: source.data[source.index].question,
				answer: source.data[source.index].answer
			}
		}
}
