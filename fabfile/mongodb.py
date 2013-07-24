from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *
import string

def ensure():
  if is_installed():
    return
  install()

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
