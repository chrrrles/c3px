from tornado.web import UIModule

class AddressFormModule(UIModule):
  def render (self, address):
    return self.render_string("inc/address_form.html", address=address)

