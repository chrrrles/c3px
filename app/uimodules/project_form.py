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

class ProjectFormModule(UIModule):

  def render (self, project):
    return self.render_string("inc/project_form.html", project=project)

  def embedded_javascript(self):
    return """ 
$(function () {
  'use strict'
  $("button#submit").click(function(){
    var error = false;
    var fields = {
      'name' : 'project name',
      'description' : 'project description' }
    $.each(fields, function(k,v){
      if ($('#'+k).val() == ""){
        error = true;
        $('#'+k).after('<span class="error">Please enter a '+v+'.</span>');
      }
    });
    if (error){return false;}
  });
}); """
