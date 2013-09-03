from schematics.models import Model
from schematics.types import StringType, EmailType, URLType
from schematics.types.compound import ModelType, ListType

from address import AddressModel
from user import UserModel
from comment import CommentModel

class BuyerModel(Model):
  user = ModelType (
    UserModel, 
    required=True, 
    serialized_name="User Details")

  billing_address = ModelType (
    AddressModel, 
    required=True, 
    serialized_name = "Billing Address")

  delivery_address = ModelType (
    AddressModel, 
    required=False,  # False means same as billing address
    serialized_name = "Delivery Address")

  comments = ListType(  
    ModelType(CommentModel),
    required=False,
    serialized_name = "Comments about Buyer" )

  website = URLType(
    required=False,
    verify_exists=True,
    serialized_name = "Website" )

  description = StringType (
    required=False,
    serialized_name = "Buyer Description" )
