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
