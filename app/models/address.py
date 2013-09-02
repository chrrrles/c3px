from schematics.models import Model
from schematics.types import StringType,EmailType

class AddressModel(Model):
  street1 = StringType (required=True)  
  street1.serialized_name = "Street Line 1"
  street1.max_length = 60
  street2 = StringType ()
  street2.serialized_name = "Street Line 2"
  street2.max_length = 60
  city = StringType ( required=True)
  city.serialized_name = "City"
  city.max_length = 60
  state = StringType ( required=True)
  state.serialized_name = "State"
  state.max_length="2"
  country = StringType (required=True,default="US")
  country.serialized_name = "Country Code"
  country.max_length = 2
  zipcode = StringType(required=True)
  zipcode.serialized_name = "Zip Code"
  zipcode.max_length = 12
