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
from fabric.context_managers import *
import os

vagrant_init = 'vagrant init precise64 http://ergonlogic.com/files/boxes/debian-current.box' 

def ensure():
  if not installed():
    puts ("Installing Vagrant...")
    install()
  else:
    puts ("Vagrant installed...")
  local('vagrant up')


def installed():
  result =  local('vagrant status',capture=True)
  if result.find('not created') > 0:
    return False
  return True

def install():
  local('vagrant up')
  local("""vagrant ssh -c "rm -f .ssh/vagrant*" """)
  #local("""vagrant ssh -c "head -n 1 .ssh/authorized_keys > .ssh/authorized_keys" """)
  local("""vagrant ssh -c "ssh-keygen -f .ssh/vagrant.rsa -t rsa -N '' " """)
  key = local("vagrant ssh -c 'cat .ssh/vagrant.rsa'", capture=True)
  local ("vagrant ssh -c 'cat .ssh/vagrant.rsa.pub >> .ssh/authorized_keys'")

  open('secrets/vagrant.rsa','w').write (key)
  os.chmod('secrets/vagrant.rsa', 0400)
  

