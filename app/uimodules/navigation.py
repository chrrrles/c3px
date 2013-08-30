from tornado.web import UIModule

class NavigationModule(UIModule):

  def render(self):
    return self.render_string('inc/navigation.html')
