# Copyright (c) 2013 - The C3PX authors.
#
# This file is part of C3PX.
#
# C3PX is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as 
# published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
#
# C3PX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public 
# License along with C3PX.  If not, see <http://www.gnu.org/licenses/>.

import os, base64

import tornado.web, tornado.ioloop, tornado.httpserver
import tornado.template as template
from  motor import MotorClient
from tornado.options import (define, options)

from app import uimodules
from app.handlers import *

cwd = os.getcwd()
static_path =os.path.join(cwd, 'static')
template_path = os.path.join(cwd, "app/templates")

# email options -- redefine in conf file
define('email_template_path', default=os.path.join (template_path,'email'), type=str)
define('smtp_host', default='smtp.gmail.com',type=str)
define('smtp_username', default='c3px', type=str)
define('smtp_password', default='secret',type=str)
define('smtp_port', default=587, type=int)
define('smtp_use_tls', default=True, type=bool)
define('email_title', default="3DRFP", type=str)

# general options
define('base_url', default="https://3drfp.com", type=str)
define('title', default="3DRFP", type=str)
define('cookie_secret', default='', type=str)

if not options.cookie_secret:
  options.cookie_secret = base64.b64encode(os.urandom(32))


debug=True,
routes = [ 
  ('/',HomeHandler), 
  ('/login',LoginHandler), 
  ('/logout',LogoutHandler), 
  ('/about', AboutHandler), 
  ('/register', RegisterHandler), 
  ('/me/profile', UserProfileHandler), 
  ('/me/settings', UserSettingsHandler), 
  ('/me/projects/(.*)', UpdateProjectHandler), 
  ('/user/(.*)/(.*)', ViewProjectHandler), 
  ('/user/(.*)', ViewUserProjectHandler), 
  ('/project/', BrowseProjectHandler), 
  ('/asset', AssetHandler),
  ('/asset/(.*)/(.*)', AssetHandler),
  ('/asset/(.*)', AssetHandler),
  ('/static/(.*)',tornado.web.StaticFileHandler, {'path':static_path})]

db = MotorClient().open_sync().c3px


application = tornado.web.Application(
  routes,
  db = db,
  ui_modules=uimodules, 
  debug=debug, 
  login_url = '/login',
  template_path=template_path,
  cookie_secret = options.cookie_secret
) 
if __name__ == "__main__":
  tornado.httpserver.HTTPServer(application).listen(8888)
  tornado.ioloop.IOLoop.instance().start()

