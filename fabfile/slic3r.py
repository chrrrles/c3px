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

from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *

slic3r_url = "http://dl.slic3r.org/linux/slic3r-linux-x86-0-9-10b.tar.gz"

def ensure():
  if not is_installed():
    puts ("Installing Slic3r")
    install()
  puts ("Slic3r is installed")

def is_installed():
  return file_exists('/web/slic3r/bin/slic3r')

def install():
  package_update()
  dir_ensure('/web/slic3r', owner='c3px') 
  run('wget -O /tmp/slic3r.tgz  %s' % slic3r_url)
  with cd('/web/slic3r'), settings(user='c3px'):
    run("tar --strip-components=1 -xzf /tmp/slic3r.tgz -C ./")
  file_unlink('/tmp/slic3r.tgz')

