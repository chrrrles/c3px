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
import string

def ensure():
  if is_installed():
    puts ("Mongodb installed...")
  else:
    puts ("Installing Mongodb")
    install()
  upstart_ensure('mongodb')
    

def is_installed():
  # probably a better test exists
  return file_exists('/etc/mongodb.conf') 
  

def install():
  sudo ('apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10')
  sudo ('touch /etc/apt/sources.list.d/10gen.list')
  with mode_sudo():
    file_update( "/etc/apt/sources.list.d/10gen.list",   
      lambda _:text_ensure_line( _, "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen"))
  package_update()
  package_ensure('mongodb-10gen')
