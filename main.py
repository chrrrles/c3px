import tornado.web, tornado.ioloop, tornado.httpserver
import tornado.template as template
from  motor import MotorClient
import os

from app import uimodules
from app.handlers import *

cwd = os.getcwd()
static_path =os.path.join(cwd, 'app/lib/static')
template_path = os.path.join(cwd, "app/templates")
debug=True,
routes = [ 
  ('/',HomeHandler), 
  ('/about', AboutHandler), 
  ('/register', RegisterHandler), 
  ('/rfps', RfpHandler), 
  ('/builders', BuilderHandler), 
  ('/create', CreateRfpHandler), 
  ('/upload/', UploadHandler),
  ('/static/(.*)',tornado.web.StaticFileHandler, {'path':static_path})]
db = MotorClient().open_sync().c3px


application = tornado.web.Application(routes,db = db,ui_modules=uimodules, debug=debug, upload_dir="uploads", template_path=template_path) 
if __name__ == "__main__":
  tornado.httpserver.HTTPServer(application).listen(8888)
  tornado.ioloop.IOLoop.instance().start()

