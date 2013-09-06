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
from schematics.types import StringType, IntType, UUIDType, EmailType, BooleanType

from .. lib.mongo import ObjectIdType


class FileModel(Model):
  filename = StringType(
    serialized_name = "File Name",
    max_length=255)

  size = IntType( 
    serialized_name = "File Size" ) 

  content_type = StringType(
    serialized_name = "File Type" )

  public_id = UUIDType(
    serialized_name = "Published Object ID" )

  object_id = ObjectIdType(
    serialized_name = 'Internal Object ID')

  owner = EmailType(
    serialized_name = "Owner ID")

  public = BooleanType (  
    default=True, 
    serialized_name = "Publicly Visible")

