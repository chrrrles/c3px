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

  result = open(outfile).read()
  unlink(outfile)
  unlink(infile)

  return result
