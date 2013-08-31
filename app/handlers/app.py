# again, so we can just do `from app import *`
from tornado.web import RequestHandler
from .. models import *
import tornado.web
from tornado.web import asynchronous
from .. lib.ormwtf import model_form
import os,random,uuid
import tornado.gen as gen
from schematics.exceptions import ValidationError

# ugly, I know
class Data:
  pass

# from http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python/652284#652284
class AutoVivification(dict):
  """Implementation of perl's autovivification feature."""
  def __getitem__(self, item):
    try:
      return dict.__getitem__(self, item)
    except KeyError:
      value = self[item] = type(self)()
      return value

#[XXX] This is some scary shit.  Secure it from user fudge!
def vivify(source):
  dest = AutoVivification()
  for k in source.keys():
    if k.find('-'):
      keys = k.split('-')
      s = "dest"
      for n in range(len(keys)):
        s += "[\"%s\"]" % keys[n]
      s += " = \"%s\"" % source[k] 
      exec (s)
    else:
      dest[k] = source[k]
  return dest

class AppHandler(RequestHandler):
  def initialize(self):
    self.db = self.settings['db']
  
  # self._args lovin -- we are creating a multidimensional dict
  def _args(self):
    a =  { k: self.get_argument(k) for k in self.request.arguments }
    return vivify(a)

  def upload_dir(self):
    return self.settings['upload_dir']
       
