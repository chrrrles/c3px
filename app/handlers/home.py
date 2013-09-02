from app import *

# For rendering the home/splash page
class HomeHandler(AppHandler):
  def get(self):
    self.render('home.html') 

# Another 'static' page handler
class AboutHandler(AppHandler):
  def get(self):
    self.render('about.html') 
