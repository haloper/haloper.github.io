define(["module", "jquery", "require", "backbone", "underscore"],
  function (module, $, require) {
    let userName = module.config().userName;
    $(function () {
        $('body')
            .append('<div>backbone version: ' + Backbone.VERSION + '</div>')
            .append('<div>underscore version: ' + _.VERSION + '</div>')
            .append('<div>require version: ' + require.VERSION + '</div>')
            .append('<div>userName ' + userName + '</div>');
    });
});
