from cuisine import *
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import *

def ensure():
  if is_installed():
    puts ("Fossil already installed")
    return
  else:
    puts ("Installing Fossil")
    install()

def is_installed():
  return file_exists("/home/fossil/repos/c3px.fossil")

def write_xinetd():
  file_write("/etc/xinetd.d/fossil", text_strip_margin(
    """
    |service http-alt
    |{
    |  port = 8080
    |  socket_type = stream
    |  wait = no
    |  user = root
    |  server = /usr/bin/fossil
    |  server_args = http /home/fossil/repos/c3px.fossil
    |}"""
  ))

def install():
  package_update()
  package_ensure(["fossil","xinetd"])
  dir_ensure ("/home/fossil/repos")
  write_xinetd()
  if not confirm ("Have you uploaded c3px.fossil to /home/fossil/repos/?", default=False):
    puts ("Exiting Now")
    return
  # xinetd has no status, so no upstart_ensure()
  run ("/etc/init.d/xinetd restart")
