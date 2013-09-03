from app import *

class UploadHandler(AppHandler):
  def prepare(self):
    if self.request.files is not None:
      for o in self.request.files:
        if len(self.request.files[o]) > 0:
          self.file = self.request.files[o][0]
          break
    if self.file is None:
      self.send_error(400)
      return

  #[XXX] Need to store files in GridFS... and also use the library, not calling scripts
  @asynchronous
  @tornado.gen.coroutine
  def post(self):
    name = uuid.uuid4().__str__()
    size = len(self.file.body)
    path = os.path.join (self.upload_dir(), name)
    try:
      f = open(path,'w')
      result = yield f.write(self.file.body)
    except:
      self.write_error(1, err="Error Saving File!")
    else:
      doc = {
        'filename' : self.file.filename,
        'size' : len(self.file.body),
        'content_type' : self.file.content_type,
        'path' : name }
      #obj = FileModel(props)
      result =  self.db.files.insert(doc, manipulate=True)
      print result
      self.write(result)


