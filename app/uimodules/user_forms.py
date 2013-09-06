# Copyright (c) 2013 - The C3PX authors.
#
# This file is part of C3PX.
#
# C3PX is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as 
# published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
#
# C3PX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public 
# License along with C3PX.  If not, see <http://www.gnu.org/licenses/>.

from tornado.web import UIModule

class BillingDetailsFormModule(UIModule):
  def render (self, billing):
    return self.render_string("inc/billing_details_form.html", billing=billing)

class UserFormModule(UIModule):
  def render (self, user):
    return self.render_string("inc/user_form.html", user=user)

  def embedded_javascript(self):
    return """
$(function () {
  'use strict'
  $("button#submit").click(function(){
    var error = false;
    var firstname = $("#firstname").val();
    var lastname = $("#lastname").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var check = $("#check").val();

    if (firstname == ''){ 
      $("#firstname").after('<span class="error">Please enter a first name.</span>');
      error = true;
    } 

    if (lastname == ''){ 
      $("#lastname").after('<span class="error">Please enter a last name.</span>');
      error = true;
    } 

    if (email == ''){ 
      $("#email").after('<span class="error">Please enter an email.</span>');
      error = true;
    } 

    if (password == ''){ 
      $("#password").after('<span class="error">Please enter a password.</span>');
      error = true;
    } 

    else if (password != check ) {
      $("#password_check").after('<span class="error">Passwords do not match.</span>');
      error = true;
    }
    if(error == true) {return false;}
  });
}); """

class AddressFormModule(UIModule):
  def render (self, address):
    return self.render_string("inc/address_form.html", address=address)

