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


