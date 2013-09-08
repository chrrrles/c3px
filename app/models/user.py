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

class UserModel(BaseModel):
  username = StringType (
    default = '',
    serialized_name = "Username",
    max_length = 40 )

  firstname = StringType ( 
    default = '',
    serialized_name = "First Name",
    max_length = 40 )

  lastname = StringType ( 
    default='',
    serialized_name = "Last Name",
    max_length = 40 )

  email = EmailType ( 
    required=True, 
    serialized_name = "Email")
 
  password = StringType (
    required=True,
    min_length = 6,
    max_length = 30,
    serialized_name = "Password" )

  phone = StringType (  
    default = '',
    serialized_name = 'Phone Number',
    max_length=30 )

  date_create = DateTimeType(required=False)

  join_hash = StringType()

  activated = BooleanType (
    default = False,
    serialized_name = "Activated Account" )

