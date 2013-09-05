from schematics.models import Model
from schematics.types import StringType,EmailType, IntType, DateTimeType, BooleanType
from schematics.types.compound import ListType, ModelType
from schematics.exceptions  import ValidationError
from file import FileModel
from comment import CommentModel
from buyer import BuyerModel

class RfpModel(Model):

  owner = ModelType(
    BuyerModel,
    required=True,
    serialized_name = "Requester" )

  files = ListType(
    ModelType( FileModel),
    serialized_name="RFP Files")

  timestamp = DateTimeType(
    serialized_name="RFP Date" )

  active = BooleanType(
    serialized_name="Active", 
    default=False,
    required=True )

  description = StringType(
    serialized_name="Description of RFP" )

  comments = ListType(  
    ModelType(CommentModel),
    required=False,
    serialized_name = "Comments about RFP" )
