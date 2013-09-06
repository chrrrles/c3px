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

blender_url = "http://mirror.cs.umn.edu/blender.org/release//Blender2.68/blender-2.68a-linux-glibc211-i686.tar.bz2"

def ensure():
  if not is_installed():
    puts ("Installing blender")
    install()
  puts ("Blender is installed")

def is_installed():
  return file_exists('/web/blender/blender')

def install():
  package_update()
  package_ensure('blender')  
  package_remove('blender') # hah!  we just want the deps
  dir_ensure('/web/blender', owner='c3px') 
  run('wget -O /tmp/blender.tbz2  %s' % blender_url)
  with cd('/web/blender'), settings(user='c3px'):
    run("tar --strip-components=1 -xjf /tmp/blender.tbz2 -C ./")
  file_unlink('/tmp/blender.tbz2')

