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

