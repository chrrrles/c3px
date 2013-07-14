import os,random,string
import tornado.web
from tornado.web import RequestHandler
from lib.ormwtf import model_form
from schemas import RfpModel,BuyerModel
from lib import skein
    
class RfpHandler(RequestHandler):
  def _args(self):
    { k: self.get_argument(k) for k in self.request.arguments }

  def get(self):
    obj = RfpModel()
    RfpForm = model_form(obj)
    self.render( 't/rfp.html',message = "New form", form = RfpForm()) 

  @tornado.web.asynchronous
  def post(self):
    rfps = self.settings['db']['rfps']
    args ={ k: self.get_argument(k) for k in self.request.arguments } 
    print "self.request.arguments: %s" % args     
    obj = RfpModel(args)
    print "obj.email: %s " % obj.email 
    form = model_form(obj)()
    print "form.email: %s " % form.email 
    if not form.validate():
      self.render( 't/rfp.html', message="Errors!", form=form)
    else: 
      try:
        file1 = self.request.files['file1'][0]
      except KeyError:
        self.render( 't/rfp.html', message="Please upload a file!", form=form)
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

