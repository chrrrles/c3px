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

from fabric.api import *
from fabric.api import env

from . import (app,python, mongodb,vagrant, firewall)

env.hosts = ['192.241.218.220']
env.user = 'root'

def v():
  vagrant.ensure()
  env.user = 'vagrant'
  env.hosts = ['127.0.0.1']
  env.port = 2222
  env.key_filename = 'secrets/vagrant.rsa' 

def deploy():
  app.ensure()

# force install/update of firewalling software
def firewall_install():
  firewall.install()


