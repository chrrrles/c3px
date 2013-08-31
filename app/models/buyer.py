from schematics.models import Model
from schematics.types import StringType, EmailType
from schematics.types.compound import ModelType
from address import AddressModel
from contact import ContactModel

class BuyerModel(Model):
  contact = ModelType (ContactModel, required=True)
  contact.serialized_name = "Contact Details"

  billing_address = ModelType (AddressModel, required=True )
  billing_address.serialized_name = "Billing Address"

  delivery_address = ModelType (AddressModel, required=True )
  delivery_address.serialized_name = "Delivery Address"

