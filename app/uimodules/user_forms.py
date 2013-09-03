from tornado.web import UIModule

class BillingDetailsFormModule(UIModule):
  def render (self, billing):
    return self.render_string("inc/billing_details_form.html", billing=billing)

class UserFormModule(UIModule):
  def render (self, user):
    return self.render_string("inc/user_form.html", user=user)

class AddressFormModule(UIModule):
  def render (self, address):
    return self.render_string("inc/address_form.html", address=address)

