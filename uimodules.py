from tornado.web import UIModule

class RfpItems(UIModule):

  def embedded_css(self):
    pass

  def embedded_javascript(self):
    pass 

  def render(self):
    return self.render_string("templates/inc/rfp_items.html", rfp_items=rfp_items)

class RfpForm(UIModule):

  def javascript_files(self):
    return [
      "/static/js/jquery-ui.min.js",
      "/static/js/jquery.iframe-transport.js",
      "/static/js/jquery.fileupload.js"]

  def embedded_javascript(self):
    # Collapsible fieldsets
    r = """
$(function () {
  $(document).on('click','fieldset.collapsible > legend', function() {
    var $this = $(this);
    var $divs = $this.siblings();
    var $legend = $this.find('i');

      $divs.toggle();

    if ($legend.hasClass("icon-caret-right")) {
      $legend.removeClass("icon-caret-right").addClass("icon-caret-down");
    }
    else {
       $legend.removeClass("icon-caret-down").addClass("icon-caret-right");
    }
  });
});
"""
    r += """
$(function () {
  $('#fileupload').fileupload({
    dataType: 'json',
    done: function (e, data) {
      $.each(data.result.files, function (index, file) {
        $('<p/>').text(file.name).appendTo(document.body);
      });
    }
  });
});"""

    return r

  def embedded_css(self):
    # Collapsible fieldsets
    r = """
fieldset.collapsible > div {
  display: none;
}"""
    return r

  def render (self, form):
    return self.render_string("templates/inc/rfp_form.html", form=form)

