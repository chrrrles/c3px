from tornado.web import UIModule

class RfpItems(UIModule):

  def embedded_css(self):
    pass

  def embedded_javascript(self):
    pass 

  def render(self):
    return self.render_string("templates/inc/rfp_items.html", rfp_items=rfp_items)

