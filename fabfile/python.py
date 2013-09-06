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

prequisites = ['build-essential', 'python-dev', 'libpng-dev',  
  'libbz2-dev', 'zlib1g-dev', 'libfreetype6-dev', 'libjpeg8-dev']

def ensure():
  if not is_installed():
   puts("Installing python support...")
   install()
  else:
    puts("Python and tools already installed")

def is_installed():
  return file_exists("/usr/local/bin/virtualenv")

def install():
  package_update()
  install_prerequisites()
  install_pip()
  install_virtualenv()

def install_prerequisites(): # we need to get PIL prequisites...
  package_ensure(prequisites)

  # this is annoying -- PIL is hardcoded to search in /usr/lib for prequisites...
  from os.path import join
  src = '/usr/lib/i386-linux-gnu'
  dst = '/usr/lib'
  for f in ['libfreetype.so', 'libjpeg.so', 'libz.so']:
    file_link(join(src,f), join(dst,f))

def install_pip():
  package_ensure("python-pip")

def install_virtualenv():
  sudo("pip install virtualenv")
