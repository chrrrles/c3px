# again, so we can just do `from app import *`
import functools
import os, random, uuid, urllib

from tornado.web import RequestHandler
from tornado.web import asynchronous
import tornado.gen 
import tornado.escape
from tornado.options import options
from motor import Op

from schematics.exceptions import ValidationError
from  .. lib.ormwtf import model_form
from .. import helpers

from .. models import *

# Wrapper functions for authentication
def auth_only(f):
  @functools.wraps(f)
  @tornado.gen.engine
  def wrapper(self, *args, **kwargs):
    self._auto_finish = False
    self.current_user = yield tornado.gen.Task(self.get_current_user_async)
    if not self.current_user:
      self.redirect(self.get_login_url() + '?' + 
        urllib.urlencode({'_next': self.request.uri}))
    else:
      f(self, *args, **kwargs)
  return wrapper
          
def auth_redir(f):

  @functools.wraps(f)
  @tornado.gen.engine
  def wrapper(self, *args, **kwargs):
    self._auto_finish = False
    self.current_user = yield tornado.gen.Task(self.get_current_user_async)
    if self.current_user:
      self.redirect('/')
    else:
      f(self, *args, **kwargs)
  return wrapper

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
  current_user = None

  @property
  def db(self): 
    return self.settings['db']

  @property
  def smtp(self):
    return self.settings['smtp']

  @tornado.gen.engine
  def get_current_user_async(self, callback):
    email = self.get_secure_cookie("current_user") or False
    if not email:
      callback(None)
    else:
      callback((yield Op(self.db.users.find_one,{"email": email})))

  def get_template_namespace(self):
    namespace = super(AppHandler, self).get_template_namespace()
    namespace.update({
      'options' : options,
      'helpers' : helpers})
    return namespace
  
  # self._args lovin -- we are creating a multidimensional dict
  def _args(self):
    a =  { k: self.get_argument(k) for k in self.request.arguments }
    #return vivify(a)
    return a

  def upload_dir(self):
    return self.settings['upload_dir']

  @tornado.gen.engine
  @tornado.web.asynchronous
  def render(self, template_name,**kwargs):
    kwargs.update({
      'current_user':
        (yield tornado.gen.Task(self.get_current_user_async)),
      'url_path': helpers.Url(self.request.uri).path,
    })
    super(AppHandler, self).render(template_name, **kwargs)
       
