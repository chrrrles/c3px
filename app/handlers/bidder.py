from app import *

class BidderHandler (AppHandler):
  def get(self):  
    self.render('bidders.html')
