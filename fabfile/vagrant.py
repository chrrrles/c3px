from cuisine import *
from fabric.api import *
from fabric.context_managers import *
import os

vagrant_init = 'vagrant init precise64 http://ergonlogic.com/files/boxes/debian-current.box' 

def ensure():
  if not installed():
    install()
  local('vagrant up')


def installed():
  result =  local('vagrant status',capture=True)
  if result.find('not created') > 0:
    return false
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
  
  return 

