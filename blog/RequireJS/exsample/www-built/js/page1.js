requirejs(["./common"],function(e){requirejs(["app/main1"])}),define("../page1",function(){}),define("app/controller/c1",["./Base"],function(e){var n=new e("Controller 1");return n}),define("app/model/m1",["./Base"],function(e){var n=new e("This is the data for Page 1");return n}),define("app/main1",["require","jquery","./lib","./controller/c1","./model/m1"],function(e){var n=e("jquery"),r=e("./lib"),o=e("./controller/c1"),i=e("./model/m1");o.setModel(i),n(function(){o.render(r.getBody())})});