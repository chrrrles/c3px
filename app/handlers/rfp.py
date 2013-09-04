from app import *

class BrowseRfpHandler(AppHandler):

  def get(self):
    self.render('rfp_browse.html')


class CreateRfpHandler(AppHandler):

  @auth_only
  def get(self):
    obj = RfpModel()
    form = model_form(obj, exclude=['files'])
    data = Data
    data.form = form()
    self.render( 'rfp_create.html',_d=data) 

  @auth_only
  @asynchronous
  def post(self):
    _d = Data()
    args = { k: self.get_argument(k) for k in self.request.arguments } 
    obj = RfpModel(args)
    form = model_form(obj)()
    if not form.validate():
      _d.form = form
      self.render( 'rfp_create.html', _d=_d)
    else: 
      try:
        file1 = self.request.files['file1'][0]
      except KeyError:
        _d.form = form
        self.render( 'rfp_create.html', _d =_d )
      original_fname = file1['filename']
      #if original_fname.split('.')[-1].lower() != "stl"
      extension = os.path.splitext(original_fname)[1]
      fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
      final_filename= fname+extension
      output_file = open("uploads/" + final_filename, 'w')
      output_file.write(file1['body'])
      obj.final_filename = final_filename
      self.db.rfps.insert(obj.serialize(),callback="_on_response")

  def _on_response(self, result, error):
    if error:
      raise tornado.web.HTTPError(500, error)
    else:
      self.redirect('/')
      #self.render( 't/rfp.html',message="Success",form = model_form(RfpModel)()) 
