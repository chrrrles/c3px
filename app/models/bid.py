# Copyright (c) 2013 - The C3PX authors.
#
# This file is part of C3PX.
#
# C3PX is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as 
# published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
#
# C3PX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public 
# License along with C3PX.  If not, see <http://www.gnu.org/licenses/>.

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
