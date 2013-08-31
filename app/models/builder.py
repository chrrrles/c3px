from schematics.models import Model
from schematics.types import StringType,EmailType
from schematics.types.compound import ModelType
from address import AddressModel

class BuilderModel(Model):
  email = EmailType ( required=True) 
  paypal_id = EmailType (required=True)
  firstname = StringType ( required=True)
  lastname = StringType ( required=True)
  address = ModelType (AddressModel, required=True)
