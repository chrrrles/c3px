from schematics.models import Model
from schematics.types import StringType, FloatType,EmailType
from schematics.exceptions  import ValidationError

#from lib.cc import country_codes
country_codes = {'US': 'USA',
  'CA': 'Canada'}


class TestModel(Model): 
  content = StringType()

class RfpModel(Model):
  email = EmailType ( required=True) 
  email.max_length = 40

  firstname = StringType ( required=True)
  firstname.max_length=40

  lastname = StringType ( required=True)
  lastname.max_length=40

  street1 = StringType (required=True)  
  street1.max_length=40

  street2 = StringType ()
  street2.max_length=40

  city = StringType ( required=True)
  city.max_length=40

  state = StringType ( required=True)
  state.max_length=2

  country = StringType ( required=True, default="US", choices=country_codes)

  final_filename =  StringType()
  final_filename.hidden = True

class BuyerModel(Model):
  email = StringType ( required=True) 
  firstname = StringType ( required=True)
  lastname = StringType ( required=True)
  street1 = StringType (required=True)  
  street2 = StringType ()
  city = StringType ( required=True)
  state = StringType ( required=True)
  country = StringType ( required=True,default="US")
