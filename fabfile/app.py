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

from . import (mongodb, python, fossil, firewall, redis, blender)

def ensure():
  # let's make sure all this is installed before we do anything
  python.ensure()
  mongodb.ensure()
  fossil.ensure()
  user_setup()
  redis.ensure()
  blender.ensure()
  firewall.ensure()
  if not is_installed():
    puts ("Installing App and dependencies...")
    install()
  puts ("App is installed...")  
  deploy()

def is_installed():
  return dir_exists('/web/3drfp')

def install():
  dir_ensure('/web/3drfp', owner='c3px')

  with cd('/web/3drfp/'), settings(user='c3px'):
    run ('fossil open /home/fossil/repos/c3px.fossil')
  
  with cd('/web/3drfp'), settings(user='c3px'):
    run ('virtualenv ./venv')
    run ('./venv/bin/pip install -r requirements.txt')
    run (' nohup ./venv/bin/python main.py &')

# [XXX] oops - i still manually set up my public key
# need to set up user.py  to set up the c3px user properly
def user_setup():
  user_ensure('c3px',home="/web")
  with mode_sudo():
    dir_ensure('/web', owner='c3px', group='c3px')

def deploy(): 
  with cd('/web/3drfp'), settings(user='c3px'):
    run ('fossil update')
    run ('./venv/bin/pip install -r requirements.txt')
    run ('killall python', warn_only=True) # man this is dangerous, but wehey YOLO!
    run ('killall rqworker', warn_only=True) # again this is dangerous, but wehey YOLO!
    run ('nohup ./venv/bin/rqworker &')
    run ('nohup ./venv/bin/python main.py &')
