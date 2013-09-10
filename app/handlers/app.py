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

# again, so we can just do `from app import *`
import functools
import os, random, uuid, urllib
import bcrypt, datetime

from bson.binary import Binary

from tornado.web import RequestHandler
from tornado.web import asynchronous
from tornado.ioloop import IOLoop
import tornado.gen 
from tornado.options import options
from tornado.escape import url_escape, url_unescape, xhtml_escape, xhtml_unescape

from schematics.exceptions import ValidationError
from  .. lib.ormwtf import model_form
from .. import helpers

from .. models import *

# for queueing
from redis import Redis
from rq import Queue


# Wrapper functions for authentication
def auth_only(f):
  @functools.wraps(f)
  @tornado.gen.coroutine
  def wrapper(self, *args, **kwargs):
    self._auto_finish = False
    self.current_user = yield self.get_current_user_async()

    if not self.current_user:
      self.redirect(self.get_login_url() + '?' + 
        urllib.urlencode({'_next': self.request.uri}))
    else:
      f(self, *args, **kwargs)
  return wrapper
          
def auth_redir(f):
  @functools.wraps(f)
  @tornado.gen.coroutine
  def wrapper(self, *args, **kwargs):
    self._auto_finish = False
    self.current_user = yield self.get_current_user_async()
    if self.current_user:
      self.redirect('/')
    else:
      f(self, *args, **kwargs)
  return wrapper


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
  return dict(dest)

class AppHandler(RequestHandler):
  current_user = None

  @property
  def reserved_names(self):
    reserved_names = ['new', 'create', 'save', 'update','delete']
    return reserved_names

  # Redis Queue... whew!
  @property
  def q(self):
   return Queue (connection=Redis()) 

  @property
  def db(self): 
    return self.settings['db']

  @property
  def smtp(self):
    return self.settings['smtp']

  @tornado.gen.coroutine
  def get_current_user_async(self):
    email = self.get_secure_cookie("current_user") or False
    if not email:
      raise tornado.gen.Return(None)
    else:
      user = yield self.db.users.find_one({"email": email})
      raise tornado.gen.Return(user)

  def get_template_namespace(self):
    namespace = super(AppHandler, self).get_template_namespace()
    namespace.update({
      'options' : options,
      'helpers' : helpers})
    return namespace
  
  # self._args lovin -- we are creating a multidimensional dict
  @property
  def _args(self):
    a =  { k: self.get_argument(k) for k in self.request.arguments }
    #return vivify(a)
    return a

  @tornado.gen.coroutine
  @tornado.web.asynchronous
  def render(self, template_name,**kwargs):
    current_user = yield self.get_current_user_async()
    kwargs.update({
      'current_user': current_user,
      'url_path': helpers.Url(self.request.uri).path,
    })
    super(AppHandler, self).render(template_name, **kwargs)
