# -*- coding: utf-8 *-*
import string
import random
import hashlib



def generate_string(size=20,
  chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def generate_md5(input_text=generate_string()):
  return hashlib.md5(input_text).hexdigest()

import cgi
import urllib
import urlparse


class Url(object):

  def __init__(self, url):
    (self.scheme, self.netloc, self.path, self.params, self.query,
      self.fragment) = urlparse.urlparse(url)
    self.args = dict(cgi.parse_qsl(self.query))

  def __str__(self):
    self.query = urllib.urlencode(self.args)
    return urlparse.urlunparse((self.scheme, self.netloc, self.path,
      self.params, self.query, self.fragment))
