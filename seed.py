from pymongo import MongoClient
from app.models import *
import config.seed_data as s
from random import sample,randint

db = MongoClient().c3px

num_buyers = 200
num_bidders = 50

emails = []  # maintain list of unique email addresses

def Address():
  street1 = "%d %s %s" % (randint(1,8888), sample(s.street_names,1)[0], sample(s.road_types,1)[0])
  city = sample(s.cities,1)[0]
  state = sample(s.states,1)[0]
  zipcode = sample(s.states[state],1)[0] 
  return AddressModel(dict(
    street1 = street1,
    city = city,
    state = state,
    zipcode = zipcode))
  
def User():
  fname = sample (s.firstnames,1)[0]
  lname = sample (s.lastnames,1)[0]
  email_host = sample (s.email_hosts,1)[0]
  email = "%s.%s@%s" % (fname.lower(),lname.lower(), email_host) 
  while email in emails:
    email = "%s.%s%d@%s" % (fname.lower(),lname.lower(),randint(1,100),email_host) 
  emails.append(email)
  return UserModel({
    'firstname' : fname,
    'lastname' : lname,
    'email' : email })

def seed_buyers():
  for n in range(num_buyers):
    buyer = BuyerModel(dict(
      user = User(),
      billing_address = Address(),
      # ten percent have different delivery address  
      delivery_address = Address() if randint(0,10) == 9 else None ))
    db.buyers.insert(buyer.serialize())

def seed_bidders():
  for n in range(num_bidders):
    user = User()
    address = Address()
    billing_details = BillingDetailsModel(dict(
      paypal_id = user.email) ) 

    bidder = BidderModel(dict(
      user = user,
      address = address,
      billing_details = billing_details))
    db.bidders.insert(bidder.serialize())

def seed(): 
  seed_buyers()
  seed_bidders()

if __name__ == "__main__":  
  seed()


