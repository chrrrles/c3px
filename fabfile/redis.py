from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *
import string

def ensure():
  if is_installed():
    puts ("Redis installed...")
  else:
    puts ("Installing Redis")
    install()
  upstart_ensure('redis-server')
    

def is_installed():
  # is this here?
  return file_exists('/etc/redis.conf') 
  

def install():
  package_ensure('redis-server')
