from tornado.web import UIModule

class FileUpload(UIModule):

  def css_files(self):  
    return '/static/blueimp/css/jquery.fileupload-ui.css'

  def javascript_files(self):
    return [
      '/static/js/jquery-ui.min.js',
      '/static/blueimp/js/load-image.min.js',
      '/static/blueimp/js/canvas-to-blob.min.js',
      '/static/blueimp/js/jquery.iframe-transport.js',
      '/static/blueimp/js/jquery.fileupload.js',
      '/static/blueimp/js/jquery.fileupload-process.js',
      '/static/blueimp/js/jquery.fileupload-image.js',
      '/static/blueimp/js/jquery.fileupload-audio.js',
      '/static/blueimp/js/jquery.fileupload-video.js',
      '/static/blueimp/js/jquery.fileupload-validate.js']

  def embedded_javascript(self):
    return """    
$(function () {
    'use strict';
    // Change this to the location of your server-side upload handler:
    var url = window.location.hostname === 'blueimp.github.io' ?
                '//jquery-file-upload.appspot.com/' : 'fileupload/',
        uploadButton = $('<button/>')
            .addClass('btn')
            .prop('disabled', true)
            .text('Processing...')
            .on('click', function () {
                var $this = $(this),
                    data = $this.data();
                $this
                    .off('click')
                    .text('Abort')
                    .on('click', function () {
                        $this.remove();
                        data.abort();
                    });
                data.submit().always(function () {
                    $this.remove();
                });
            });
    $('#fileupload').fileupload({
        url: url,
        dataType: 'json',
        autoUpload: true,
        acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i,
        maxFileSize: 5000000, // 5 MB
        // Enable image resizing, except for Android and Opera,
        // which actually support image resizing, but fail to
        // send Blob objects via XHR requests:
        disableImageResize: /Android(?!.*Chrome)|Opera/
            .test(window.navigator.userAgent),
        previewMaxWidth: 100,
        previewMaxHeight: 100,
        previewCrop: true
    }).on('fileuploadadd', function (e, data) {
        data.context = $('<div/>').appendTo('#files');
        $.each(data.files, function (index, file) {
            var node = $('<p/>')
                    .append($('<span/>').text(file.name));
            if (!index) {
                node
                    .append('<br>')
                    .append(uploadButton.clone(true).data(data));
            }
            node.appendTo(data.context);
        });
    }).on('fileuploadprocessalways', function (e, data) {
        var index = data.index,
            file = data.files[index],
            node = $(data.context.children()[index]);
        if (file.preview) {
            node
                .prepend('<br>')
                .prepend(file.preview);
        }
        if (file.error) {
            node
                .append('<br>')
                .append(file.error);
        }
        if (index + 1 === data.files.length) {
            data.context.find('button')
                .text('Upload')
                .prop('disabled', !!data.files.error);
        }
    }).on('fileuploadprogressall', function (e, data) {
        var progress = parseInt(data.loaded / data.total * 100, 10);
        $('#progress .bar').css(
            'width',
            progress + '%'
        );
    }).on('fileuploaddone', function (e, data) {
        $.each(data.result.files, function (index, file) {
            var link = $('<a>')
                .attr('target', '_blank')
                .prop('href', file.url);
            $(data.context.children()[index])
                .wrap(link);
        });
    }).on('fileuploadfail', function (e, data) {
        $.each(data.result.files, function (index, file) {
            var error = $('<span/>').text(file.error);
            $(data.context.children()[index])
                .append('<br>')
                .append(error);
        });
    }).prop('disabled', !$.support.fileInput)
        .parent().addClass($.support.fileInput ? undefined : 'disabled');
});"""

  def render(self):
    return self.render_string("templates/inc/file_upload.html")

class RfpItems(UIModule):

  def embedded_css(self):
    pass

  def embedded_javascript(self):
    pass 

  def render(self):
    return self.render_string("templates/inc/rfp_items.html", rfp_items=rfp_items)

class RfpForm(UIModule):


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
    return self.render_string("templates/inc/rfp_form.html", form=form)

