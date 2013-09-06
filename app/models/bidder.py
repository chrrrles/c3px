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
