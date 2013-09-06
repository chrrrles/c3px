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

class RfpFormModule(UIModule):


  def embedded_javascript(self):
    # Collapsible fieldsets
    r = """
$(function () {
  $(document).on('click','fieldset.collapsible > legend', function() {
    var $this = $(this);
    var $divs = $this.siblings();
    var $legend = $this.find('i');

      $divs.toggle();

    if ($legend.hasClass("icon-caret-right")) {
      $legend.removeClass("icon-caret-right").addClass("icon-caret-down");
    }
    else {
       $legend.removeClass("icon-caret-down").addClass("icon-caret-right");
    }
  });
});
"""
    r += """
$(function () {
  $('#fileupload').fileupload({
    dataType: 'json',
    done: function (e, data) {
      $.each(data.result.files, function (index, file) {
        $('<p/>').text(file.name).appendTo(document.body);
      });
    }
  });
});"""

    return r

  def embedded_css(self):
    # Collapsible fieldsets
    r = """
fieldset.collapsible > div {
  display: none;
}"""
    return r

  def render (self, form):
    return self.render_string("inc/rfp_form.html", form=form)

