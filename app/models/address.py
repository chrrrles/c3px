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

class AddressModel(BaseModel):
  street1 = StringType (
    required=True, 
    serialized_name = "Street Line 1", 
    max_length = 60 )  

  street2 = StringType (
    serialized_name = "Street Line 2",
    max_length = 60 )

  city = StringType ( 
    required=True, 
    serialized_name = "City",
    max_length = 60)

  state = StringType ( 
    required=True, 
    serialized_name = "State",
    max_length="2")

  country = StringType (
    required=True,
    default="US",
    serialized_name = "Country Code",
    max_length = 2 )

  zipcode = StringType(
    required=True, 
    serialized_name = "Postal Code",
    max_length = 12 )

  geopoint = GeoPointType(  
    required=False,
    serialized_name = "Geolocation" )



