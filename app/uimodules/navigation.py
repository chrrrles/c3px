from tornado.web import UIModule

class NavigationModule(UIModule):

  def render(self, **kwargs):
    return self.render_string('inc/navigation.html', **kwargs)
