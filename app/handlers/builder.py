from app import *

class BuilderHandler (AppHandler):
  def get(self):  
    self.render('builders.html')
