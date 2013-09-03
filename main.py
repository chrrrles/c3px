import tornado.web, tornado.ioloop, tornado.httpserver
import tornado.template as template
from  motor import MotorClient
import os
from tornado.options import (define, options)

from app import uimodules
from app.handlers import *

cwd = os.getcwd()
static_path =os.path.join(cwd, 'app/lib/static')
template_path = os.path.join(cwd, "app/templates")

# email options
define('email_template_path', default=os.path.join (template_path,'email'), type=str)
define('smtp_host', default='smtp.gmail.com',type=str)
define('smtp_username', default='c3px', type=str)
define('smtp_password', default='change this or define in a conf file',type=str)
define('smtp_port', default=587, type=int)
define('smtp_use_tls', default=True, type=bool)
define('email_title', default="3DRFP", type=str)
define('base_url', default="https://3drfp.com", type=str)


debug=True,
routes = [ 
  ('/',HomeHandler), 
  ('/about', AboutHandler), 
  ('/register', RegisterHandler), 
  ('/rfps', RfpHandler), 
  ('/bidder', BidderHandler), 
  ('/create', CreateRfpHandler), 
  ('/upload/', UploadHandler),
  ('/static/(.*)',tornado.web.StaticFileHandler, {'path':static_path})]
db = MotorClient().open_sync().c3px


application = tornado.web.Application(
  routes,
  db = db,
  ui_modules=uimodules, 
  debug=debug, 
  upload_dir="uploads", 
  template_path=template_path ) 
if __name__ == "__main__":
  tornado.httpserver.HTTPServer(application).listen(8888)
  tornado.ioloop.IOLoop.instance().start()

