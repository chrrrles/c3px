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

def ensure():
  if is_installed():
    puts ("Fossil installed...")
  else:
    puts ("Installing Fossil")
    install()
  # xinetd has no status, so no upstart_ensure()
  run ("/etc/init.d/xinetd restart")

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
