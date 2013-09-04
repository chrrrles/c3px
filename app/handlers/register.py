from app import *

class RegisterHandler(AppHandler):
  def get(self):  
    form = model_form ( UserModel() )
    return self.render('register.html', form = form())

  @tornado.web.asynchronous
  @tornado.gen.engine
  def post(self):
    if self.current_user:  # no double-dipping
      self.redirect('/')
      return

    if self.get_argument('bidder', None):
      bidder = BidderModel(self._args())
      try: 
        bidder.validate()
      except ValidationError:
        form = model_form(bidder)()
        form.validate() # hate having to call this here
        return self.render('register_bidder.html', form=form)
      else:
        self.db.bidders.insert(bidder.serialize(), callback="_on_response")

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
        
