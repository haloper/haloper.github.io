define(["module", "jquery", "text!res/copyright.txt", "backbone", "underscore"],
  function (module, $, copyright) {
    let userName = module.config().userName;
    $(function () {
        $('body')
            .append('<div>backbone version: ' + Backbone.VERSION + '</div>')
            .append('<div>underscore version: ' + _.VERSION + '</div>')
            .append('<div>userName ' + userName + '</div>')
            .append('<div>' + copyright + '</div>');
    });
});
