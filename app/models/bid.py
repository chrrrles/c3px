from schematics.models import Model
from schematics.types import StringType, FloatType, DateTimeType, DecimalType
from schematics.types.compound import ListType, ModelType
from bidder import BidderModel
from comment import CommentModel
from rfp import RfpModel

class BidModel(Model):
  bidder = ModelType(
    BidderModel, 
    serialized_name="Bidder",
    required=True )

  rfp = ModelType(
    RfpModel,
    serialized_name="RFP",
    required=True )

  cost_build = DecimalType( 
    required=True,
    serialized_name="Bid Price", 
    min_value=0.01 )

  cost_shipping = DecimalType(
    required=True,
    serialized_name="Shipping Cost", 
    min_value=0.00 ) 

  timestamp = DateTimeType(
    serialized_name="Date of Bid", 
    required=True )

  note_bidder = StringType(
    serialized_name="Note from Bidder")

  comments = ListType(
    ModelType(CommentModel), 
    serialized_name = "Comments about Bid")
