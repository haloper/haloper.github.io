define(["jquery", "app/lib", "app/controller/c2", "app/model/m2"],
  function ($, lib, controller, model, require) {

    //A fabricated API to show interaction of
    //common and specific pieces.
    controller.setModel(model);
    $(function () {
        controller.render(lib.getBody());
    });
});
