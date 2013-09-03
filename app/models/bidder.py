from schematics.models import Model
from schematics.types import StringType,EmailType, URLType
from schematics.types.compound import ModelType,ListType
from address import AddressModel
from billing_details import BillingDetailsModel
from user import UserModel
from comment import CommentModel

class BidderModel(Model):
  user = ModelType (
    UserModel, 
    required=True, 
    serialized_name = "User Details" )

  address = ModelType (
    AddressModel, 
    required=True,
    serialized_name = "Address" )

  billing_details = ModelType ( 
    BillingDetailsModel, 
    required=True, 
    serialized_name = "Billing Details" )

  comments = ListType(  
    ModelType(CommentModel),
    required=False,
    serialized_name = "Comments about Bidder" )

  website = URLType(
    required=False,
    verify_exists=True,
    serialized_name = "Website" )

  description = StringType (
    required=False,
    serialized_name = "Bidder Description" )
