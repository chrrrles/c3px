from schematics.models import Model
from schematics.types import StringType,EmailType

class BuyerModel(Model):
  email = EmailType ( required=True) 
  firstname = StringType ( required=True)
  lastname = StringType ( required=True)
  street1 = StringType (required=True)  
  street2 = StringType ()
  city = StringType ( required=True)
  state = StringType ( required=True)
  country = StringType ( required=True,default="US")
