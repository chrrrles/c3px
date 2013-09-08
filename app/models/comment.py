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
from user import UserModel # this is the 'poster'

class CommentModel(BaseModel):
  timestamp = DateTimeType(
    required=True, 
    serialized_name="Comment Date")

  comment = StringType(
    required=True,
    serialized_name = "Comment" )

  commenter = EmailType(
    required = True,
    serialized_name = "Commenter")

  subject = ObjectIdType(
    required=True,
    serialized_name = "Internal ID of Subject")
    
  active = BooleanType(default=True)  # so commenter or admin can soft-delete messages
