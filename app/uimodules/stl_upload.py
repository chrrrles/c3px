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

class StlUploadModule(UIModule):

  def css_files(self):  
    return '/static/fineuploader/css/fineuploader-3.8.2.min.css'

  def javascript_files(self):
    return '/static/fineuploader/js/jquery.fineuploader-3.8.2.min.js'

  def embedded_javascript(self):
    return """    
$(document).ready(function () {
  $('#uploader').fineUploader({
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
    autoUpload: true
  }).on('complete', function(event, id, fileName, xhr) {
    if (xhr.success) {
      $("#upload_thumbnails").append('\
<li id="upload_thumbnail_'+id+'"> \
  <div class="thumbnail" > \
    <img class="img-rounded" src="/asset/'+xhr.newUuid +'/thumbnail" alt="' + fileName + '"> \
    <h4>'+fileName+'</h4>\
  </div> \
</li> ');
    }
  }).on('deleteComplete', function(event, id, xhr, isError){
    if ( !isError ){
      $('#upload_thumbnail_'+id).remove();
    }
  });
  // Make sure we submit at least one STL File
  $("button#submit").click(function(){
    var items = $("#uploader").fineUploader('getUploads');
    var send = false;
    var uploads = [];
    items.forEach(function(item,n){
      if (item.status == "upload successful"){
        uploads.push(item.uuid)
        if (item.name.split('.')[1].toLowerCase() == "stl"){
          send = true;
        }
      }
    });
    $(previously_uploaded).each(function(n,item){
      uploads.push(item);
      send = true;
    });
    if (send){
      uploads.forEach(function(upload,n){
        $("#project_form").append('<input type="hidden" name="uploads[]" value="'+upload+'"> ');
      });
    }
    else{
      $("#alert").removeClass('hidden');
      $("#alert").append("You must upload at least 1 STL file")
      setTimeout(function(){
        $("#alert").empty();
        $("#alert").addClass('hidden');
      },5000)
      return false;
    }
  });

  $(previously_uploaded).each(function(n,upload){
    $.get('/asset/'+upload+'/info','', function(xhr) {
      $("#upload_thumbnails").append('\
<li id="previously_uploaded_'+upload+'"> \
  <div class="thumbnail" > \
    <img class="img-rounded" src="/asset/'+upload +'/thumbnail" alt="' + xhr.filename + '"> \
    <h4>'+xhr.filename+'</h4>\
    <h5>Previously Uploaded</h5>\
    <h5>size: '+xhr.size+'</h5> \
  </div> \
</li> ');
    })
  }); 
})
    """

  def render(self,uploads=[]):
    return self.render_string("inc/file_upload.html", uploads=uploads)


