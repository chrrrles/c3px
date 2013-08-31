from app import *

class RegisterHandler(AppHandler):
  def get(self):  
    data = Data()
    if self.get_argument('builder', None):
      form = model_form ( BuilderModel() )
      return self.render('register_builder.html', form = form())
    else: 
      form = model_form ( BuyerModel() )
      return self.render('register.html', form = form())
