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
