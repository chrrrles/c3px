from tornado.web import UIModule

class NavigationModule(UIModule):

  def render(self, **kwargs):
    return self.render_string('inc/navigation.html', **kwargs)

  def embedded_javascript(self):
    return """
$(function(){
  $("#logout").click(function(a){
    $("#logout_form").submit();
    return false;
  });
});
    """

  def html_body(self):
    return """
<form method="post" id="logout_form" action="/logout">
  <input type="hidden" name="logout" value="logout"></input>
</form>
    """
