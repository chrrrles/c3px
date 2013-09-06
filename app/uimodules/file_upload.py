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

class FileUploadModule(UIModule):

  def css_files(self):  
    return '/static/fineuploader/css/fineuploader-3.8.2.min.css'

  def javascript_files(self):
    return '/static/fineuploader/js/jquery.fineuploader-3.8.2.min.js'
      

  def embedded_javascript(self):
    return """    
$(document).ready(function () {
  $('#upload-files').fineUploader({
    request: {
      endpoint: '/asset'
    },
    editFilename: {
      enabled: true
    },
    validation: {
      allowedExtensions: ['jpeg', 'jpg', 'gif', 'png', 'stl']
    },
    deleteFile : {
      enabled: true,
      endpoint: '/asset'
    },
    autoUpload: false
  }).on('complete', function(event, id, fileName, responseJSON) {
    if (responseJSON.success) {
      $(this).append('<img class="img-rounded" src="/asset/'+responseJSON.newUuid +'/thumbnail" alt="' + fileName + '">');
    }
  });

  $('#triggerUpload').click(function() {
    $('#upload-files').fineUploader('uploadStoredFiles');
  });
})
    """

  def render(self):
    return self.render_string("inc/file_upload.html")


