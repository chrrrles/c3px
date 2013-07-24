import tornado.web, tornado.ioloop, tornado.httpserver
import tornado.template as template
import motor
import os

from app import uimodules
from app.handlers import RfpHandler

static_path =os.path.join(os.getcwd(), 'app/lib/static')
debug=True,
routes = [ 
  ('/',RfpHandler), 
  ('/static/(.*)',tornado.web.StaticFileHandler, {'path':static_path})]
db = motor.MotorClient().open_sync().c3px

application = tornado.web.Application(routes,db = db,ui_modules=uimodules, debug=debug) 
if __name__ == "__main__":
  tornado.httpserver.HTTPServer(application).listen(8888)
  tornado.ioloop.IOLoop.instance().start()

