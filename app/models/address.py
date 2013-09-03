from schematics.models import Model
from schematics.types import StringType,EmailType, GeoPointType

class AddressModel(Model):
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



