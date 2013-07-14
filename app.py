import tornado.web, tornado.ioloop, tornado.httpserver
import tornado.template as template
from handlers import RfpHandler
import motor
import os

static_path = os.path.join(os.getcwd(), 'lib/static')
routes = [ 
  ('/',RfpHandler), 
  ('/static/(.*)',tornado.web.StaticFileHandler, {'path':static_path})]
db = motor.MotorClient().open_sync().c3px

application = tornado.web.Application(routes,db = db ) 
if __name__ == "__main__":
  tornado.httpserver.HTTPServer(application).listen(8888)
  tornado.ioloop.IOLoop.instance().start()




  
