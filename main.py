import tornado.web, tornado.ioloop, tornado.httpserver
import tornado.template as template
from  motor import MotorClient
import os

from app import uimodules
from app.handlers import RfpHandler, UploadHandler

static_path =os.path.join(os.getcwd(), 'app/lib/static')
debug=True,
routes = [ 
  ('/',RfpHandler), 
  ('/upload/', UploadHandler),
  ('/static/(.*)',tornado.web.StaticFileHandler, {'path':static_path})]
db = MotorClient().open_sync().c3px


application = tornado.web.Application(routes,db = db,ui_modules=uimodules, debug=debug, upload_dir="uploads") 
if __name__ == "__main__":
  tornado.httpserver.HTTPServer(application).listen(8888)
  tornado.ioloop.IOLoop.instance().start()

