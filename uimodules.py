from tornado.web import UIModule

class RfpForm(UIModule):
  def render (self, form):
    return self.render_string("templates/inc/rfp_form.html", form=form)

