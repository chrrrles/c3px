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
