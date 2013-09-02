from tornado.web import UIModule

class BillingDetailsFormModule(UIModule):
  def render (self, billing):
    return self.render_string("inc/billing_details_form.html", billing=billing)

class ContactFormModule(UIModule):
  def render (self, contact):
    return self.render_string("inc/contact_form.html", contact=contact)

class AddressFormModule(UIModule):
  def render (self, address):
    return self.render_string("inc/address_form.html", address=address)

