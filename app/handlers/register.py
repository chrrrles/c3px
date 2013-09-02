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

  @tornado.web.asynchronous
  @tornado.gen.engine
  def post(self):
    if self.current_user:  # no double-dipping
      self.redirect('/')
      return

    if self.get_argument('builder', None):
      builder = BuilderModel(self._args())
      try: 
        builder.validate()
      except ValidationError:
        form = model_form(builder)()
        form.validate() # hate having to call this here
        return self.render('register_builder.html', form=form)
      else:
        self.db.builders.insert(builder.serialize(), callback="_on_response")

    else: # you are a buyer then
      buyer = BuyerModel(self._args())
      try:
        buyer.validate()
      except ValidationError: 
        form = model_form(buyer)
        buyer_form = form()
        buyer_form.validate()
        return self.render('register.html', form = buyer_form)
      else:
        self.db.buyers.insert(buyer.serialize(), callback="_on_response")

  def _on_response(self, result, error):
    if error:
      raise tornado.web.HTTPError(500, error)
    else:
      self.redirect('/')
        
