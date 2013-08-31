from schematics.models import Model
from schematics.types import StringType,EmailType
from schematics.types.compound import ModelType
from address import AddressModel
from billing_details import BillingDetailsModel
from contact import ContactModel

class BuilderModel(Model):
  contact = ModelType (ContactModel, required=True)
  contact.serialized_name = "Contact Details"

  address = ModelType (AddressModel, required=True)
  address.serialized_name = "Address"

  billing_details = ModelType ( BillingDetailsModel, required=True)
  billing_details.serialized_name = "Billing Details"
