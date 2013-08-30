from fabric.api import *
from fabric.api import env

from . import (app,python, mongodb,vagrant)

env.hosts = ['192.241.218.220']
env.user = 'root'

def v():
  vagrant.ensure()
  env.user = 'vagrant'
  env.hosts = ['127.0.0.1']
  env.port = 2222
  env.key_filename = 'secrets/vagrant.rsa' 

def deploy():
  app.deploy()

def push(refresh=False):
  app.deploy(refresh)

def python_ensure():
  python.ensure()

