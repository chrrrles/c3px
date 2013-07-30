import os,random,string
import tornado.web
from tornado.web import RequestHandler, asynchronous
import tornado.gen as gen
from lib.ormwtf import model_form
from schemas import RfpModel,BuyerModel
from lib import skein
import uuid
    
# the object we pass to the templates/views
class Data:
  pass

# Images + STL files 

class AppHandler(RequestHandler):
  def db(self):
    return self.settings['db']

  def upload_dir(self):
    return self.settings['upload_dir']
       

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
  @gen.coroutine
  def post(self):
    print self.file.filename, self.file.content_type, len(self.file.body)  
    name = uuid.uuid4().__str__()
    size = len(self.file.body)
    path = os.path.join (self.upload_dir, name)
    try:
      f = open(path,'w')
      f.write(self.file.body)
    except:
      self.write_error(1, err="Error Saving File!")
    else:
      files = self.db['files']
      obj = FileModel()
      obj.name = self.file.filename
      obj.size = size
      obj.content_type= self.file.content_type
      obj.path = path
      files.insert(obj.serialize(), callback = "_on_response")

  def _on_response(self, result, error):
    if error:
      raise tornado.web.HTTPError(500, error)
    else:
      self.write(result)
    

class RfpHandler(AppHandler):
  def _args(self):
    { k: self.get_argument(k) for k in self.request.arguments }

  def get(self):
    obj = RfpModel()
    form = model_form(obj)
    data = Data
    data.form = form()
    data.message = "New Form"
    self.render( 'templates/rfp.html',_d=data) 

  @asynchronous
  def post(self):
    _d = Data()
    rfps = self.db['rfps']
    args = { k: self.get_argument(k) for k in self.request.arguments } 
    print "self.request.arguments: %s" % args     
    obj = RfpModel(args)
    form = model_form(obj)()
    if not form.validate():
      _d.form = form
      self.render( 'templates/rfp.html', _d=_d)
    else: 
      try:
        file1 = self.request.files['file1'][0]
      except KeyError:
        _d.form = form
        self.render( 'templates/rfp.html', _d =_d )
      original_fname = file1['filename']
      #if original_fname.split('.')[-1].lower() != "stl"
      extension = os.path.splitext(original_fname)[1]
      fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
      final_filename= fname+extension
      output_file = open("uploads/" + final_filename, 'w')
      output_file.write(file1['body'])
      obj.final_filename = final_filename
      rfps.insert(obj.serialize(),callback="_on_response")

  def _on_response(self, result, error):
    if error:
      raise tornado.web.HTTPError(500, error)
    else:
      self.redirect('/')
      #self.render( 't/rfp.html',message="Success",form = model_form(RfpModel)()) 

