from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *

from . import (mongodb, python, fossil, firewall, redis)

def ensure():
  if not is_installed():
    puts ("Installing App and dependencies...")
    install()
  else:
    puts ("App is installed...")  
  deploy()

def is_installed():
  return dir_exists('/web/3drfp')

def install():
  python.ensure()
  mongodb.ensure()
  fossil.ensure()
  user_setup()
  redis.ensure()
  firewall.ensure()
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
