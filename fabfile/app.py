from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *

from . import (mongodb, python)

def ensure():
  if is_installed():
    puts ("App is already installed")  
    return
  puts ("Installing App and dependencies...")
  install()

def is_installed():
  return dir_exists('/web/3drfp')

def install():
  python.ensure()
  mongodb.ensure()
  user_setup()
  package_ensure('git')

  with cd('/web') and settings(user='c3px'):
    run ('git clone git@github.com:chrrrles/c3px.git 3drfp')
  
  with cd('/web/3drfp') and settings(user='c3px'):
    run ('virtualenv ./venv')
    run ('./venv/bin/pip install -r requirements.txt')
    run ('nohup ./venv/bin/python app.py &')

# [XXX] oops - i still manually set up my public key
# need to set up user.py  to set up the c3px user properly
def user_setup():
  user_ensure('c3px',home="/web")
  with mode_sudo():
    dir_ensure('/web', owner='c3px', group='c3px')
