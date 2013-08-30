from app import *

class RfpHandler(AppHandler):

  def get(self):
    self.render('rfp.html')
