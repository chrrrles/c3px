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

from os import path, unlink
from uuid import uuid1
import subprocess

# [XXX] FUGLY hardcoding these values...
dir_in = path.abspath('utils/tmp/input')
dir_out = path.abspath('utils/tmp/output')
render_blend = path.abspath('utils/render.blend') 
render_python = path.abspath('utils/viz.py')
blender = path.abspath('../blender/blender')

def render_stl(data):
  fname = str(uuid1())
  outfile = path.join(dir_out, fname)
  infile = path.join(dir_in, fname)
   
  try:  
    open(path.join(dir_in, fname),'w').write(data) 
  except:
    return False

  command = "%s -b %s -P %s %s %s" % (
    blender, render_blend, render_python, infile, outfile)

  subprocess.check_output(command.split())

  try:
    result = open(outfile).read()
  except:
    unlink(infile)
    return False

  unlink(outfile)
  unlink(infile)

  return result
