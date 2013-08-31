from schematics.models import Model
from schematics.types import StringType,EmailType

class AddressModel(Model):
  street1 = StringType (required=True)  
  street2 = StringType ()
  city = StringType ( required=True)
  state = StringType ( required=True)
  country = StringType ( required=True,default="US")
  zipcode = StringType(required=True)
