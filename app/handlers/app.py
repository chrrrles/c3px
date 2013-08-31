# again, so we can just do `from app import *`
from tornado.web import RequestHandler
from .. models import *
import tornado.web
from tornado.web import asynchronous
from .. lib.ormwtf import model_form
import os,random,uuid
import tornado.gen as gen

# ugly, I know
class Data:
  pass

class AppHandler(RequestHandler):
  def initialize(self):
    self.db = self.settings['db']
  
  # self._args lovin
  def _args(self):
    { k: self.get_argument(k) for k in self.request.arguments }

  def upload_dir(self):
    return self.settings['upload_dir']
       
