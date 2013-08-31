from schematics.models import Model
from schematics.types import StringType, EmailType
from schematics.types.compound import ModelType
from address import AddressModel

class BuyerModel(Model):
  email = EmailType ( required=True ) 
  firstname = StringType ( required=True )
  lastname = StringType ( required=True )
  billing_address = ModelType (AddressModel, required=True )
  delivery_address = ModelType (AddressModel, required=True )

