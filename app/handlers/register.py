from app import *

class RegisterHandler(AppHandler):
  def get(self):  
    data = Data()
    if self.get_argument('builder', None):
      data.form = model_form ( BuilderModel() )
      return self.render('register_builder.html', _d = data)
    else: 
      data.form = model_form ( BuyerModel() )
      return self.render('register.html', _d = data)
