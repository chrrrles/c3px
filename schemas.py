from schematics.models import Model
from schematics.types import StringType,EmailType, IntType
from schematics.exceptions  import ValidationError

#from lib.cc import country_codes
country_codes = {'US': 'USA',
  'CA': 'Canada'}


class TestModel(Model): 
  content = StringType()

class RfpModel(Model):
  email = EmailType ( required=True) 
  email.max_length = 40
  email.serialized_name = "Email"

  firstname = StringType ( required=True)
  firstname.max_length=40
  firstname.serialized_name = "First Name"

  lastname = StringType ( required=True)
  lastname.max_length=40
  lastname.serialized_name = "Last Name"

  street1 = StringType (required=True)  
  street1.max_length=40
  street1.serialized_name = "Street 1"

  street2 = StringType ()
  street2.max_length=40
  street2.serialized_name = "Street 2"

  city = StringType ( required=True)
  city.max_length=40
  city.serialized_name = "City"

  state = StringType ( required=True)
  state.max_length=2
  state.serialized_name = "State"

  file_id = IntType( required=True)
  file_id.serialized_name = "File"

  postal_code = StringType ( required=True)
  postal_code.max_length=10
  postal_code.serialized_name = "Zip/Postal Code"

  country = StringType ( required=True, default="US", choices=country_codes)
  country.serialized_name = "Country"


class BuyerModel(Model):
  email = StringType ( required=True) 
  firstname = StringType ( required=True)
  lastname = StringType ( required=True)
  street1 = StringType (required=True)  
  street2 = StringType ()
  city = StringType ( required=True)
  state = StringType ( required=True)
  country = StringType ( required=True,default="US")
