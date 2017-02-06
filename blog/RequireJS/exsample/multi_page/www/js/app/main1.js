define(["jquery", "app/lib", "app/controller/c1", "app/model/m1", "backbone", "underscore"],
  function ($, lib, controller, model, backbone, underscore) {

    //A fabricated API to show interaction of
    //common and specific pieces.
    controller.setModel(model);
    $(function () {
        controller.render(lib.getBody());

        //Display backbone and underscore versions
        $('body')
            .append('<div>backbone version: ' + backbone.VERSION + '</div>')
            .append('<div>underscore version: ' + underscore.VERSION + '</div>');
    });
});
