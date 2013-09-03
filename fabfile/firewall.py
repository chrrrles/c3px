from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *

def ensure():
  if is_installed():
    puts ("Firewall/Fail2Ban installed...")
  else:
    puts ("Installing Firewall/Fail2Ban")
    install()
  upstart_ensure('fail2ban')

def is_installed():
  return dir_exists("/home/fail2ban")

def install():
  package_update()
  package_ensure(["fail2ban"])
