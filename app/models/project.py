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

from base import *
from file import FileModel
from comment import CommentModel
from buyer import BuyerModel

class ProjectModel(BaseModel):

  owner = EmailType(
    required=True,
    serialized_name = "Project Owner" )

  name = StringType(
    required=True,
    serialized_name = "Project Name",
    max_length=60,
    min_length=4) 

  timestamp = DateTimeType(
    serialized_name="Project Date" )

  active = BooleanType(
    serialized_name="Active", 
    default=False )

  public = BooleanType(
    serialized_name="Publically Visible", 
    default=True )

  description = StringType(
    serialized_name="Description of Project" )

  delivery_time = IntType(
    serialized_name="Days to Delivery After Winning Bid",
    default = 7,
    choices = {
      2: 'Two',
      3: 'Three',
      7: 'Week',
      14: 'Two Weeks',
      30: 'Month'})



