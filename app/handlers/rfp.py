from app import *

class BrowseRfpHandler(AppHandler):

  def get(self):
    self.render('rfp_browse.html')


class CreateRfpHandler(AppHandler):

  @auth_only
  def get(self):
    self.render( 'rfp_create.html') 

  @auth_only
  @tornado.web.asynchronous
  @tornado.gen.engine
  def post(self):
    self.render('rfp_create.html')
