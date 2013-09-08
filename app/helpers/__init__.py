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

# -*- coding: utf-8 *-*
from __future__ import division
import string
import random
import hashlib



def generate_string(size=20,
  chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def generate_md5(input_text=generate_string()):
  return hashlib.md5(input_text).hexdigest()


def humanize_bytes(B, precision=1):
  abbrevs = (
    (1<<50L, 'PB'),
    (1<<40L, 'TB'),
    (1<<30L, 'GB'),
    (1<<20L, 'MB'),
    (1<<10L, 'kB'),
    (1, 'bytes')
  )
  B = int(B)
  if B == 1:
    return '1 byte'
  for factor, suffix in abbrevs:
    if B >= factor:
      break
  return '%.*f %s' % (precision, B / factor, suffix)


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
